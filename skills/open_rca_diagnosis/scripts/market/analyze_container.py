#!/usr/bin/env python3
"""
Container Analyzer for OpenRCA - 容器资源指标分析工具
一次性完成：加载容器数据 + 计算阈值 + 过滤时间 + 检测资源异常

Usage:
    python analyze_container.py --file metric_container.csv --start "2022-03-20 09:00:00" --end "2022-03-20 09:30:00" --component shippingservice
"""

import argparse
import pandas as pd
import numpy as np
from datetime import datetime
import pytz
import sys
from pathlib import Path


# 资源类型关键词映射
RESOURCE_KEYWORDS = {
    'cpu': ['cpu', 'cpu_usage', 'cpu_seconds'],
    'memory': ['memory', 'mem'],
    'disk_read': ['disk_read', 'fs_read', 'io_read', 'read_bytes', 'fs_reads'],
    'disk_write': ['disk_write', 'fs_write', 'io_write', 'write_bytes', 'fs_writes'],
    'network': ['network', 'net', 'tcp', 'packet']
}


def classify_kpi(kpi_name: str) -> str:
    """分类KPI类型"""
    kpi_lower = kpi_name.lower()
    for res_type, keywords in RESOURCE_KEYWORDS.items():
        if any(kw in kpi_lower for kw in keywords):
            return res_type
    return 'other'


def analyze_container_metrics(file_path: str, start_dt: datetime, end_dt: datetime, component_filter: str = None):
    """分析容器层指标"""
    tz = pytz.timezone('Asia/Shanghai')
    start_ts = int(start_dt.timestamp())
    end_ts = int(end_dt.timestamp())
    
    df = pd.read_csv(file_path)
    
    print(f"{'='*70}")
    print(f"容器层资源指标分析报告")
    print(f"{'='*70}")
    print(f"数据文件: {file_path}")
    print(f"总数据量: {len(df)} 条")
    print(f"时间范围: {start_dt} ~ {end_dt}")
    print(f"分析时间: {datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}")
    
    df['resource_type'] = df['kpi_name'].apply(classify_kpi)
    
    if component_filter:
        df = df[df['cmdb_id'].str.contains(component_filter, case=False, na=False)]
        print(f"组件过滤: {component_filter}")
    
    print(f"\n{'#'*70}")
    print(f"# 第一步：统计组件和KPI")
    print(f"{'#'*70}")
    
    components = df['cmdb_id'].unique()
    print(f"容器数量: {len(components)}")
    
    kpi_types = df.groupby('resource_type')['kpi_name'].nunique()
    print(f"\n资源类型统计:")
    for res_type, count in kpi_types.items():
        print(f"  {res_type}: {count} 个KPI")
    
    print(f"\n{'#'*70}")
    print(f"# 第二步：过滤故障时间窗口")
    print(f"{'#'*70}")
    
    filtered = df[(df['timestamp'] >= start_ts) & (df['timestamp'] <= end_ts)]
    print(f"时间窗口内数据: {len(filtered)} 条")
    
    if len(filtered) == 0:
        print(f"警告: 指定时间范围内无数据！")
        return
    
    print(f"\n{'#'*70}")
    print(f"# 第三步：计算每个KPI的全局阈值")
    print(f"{'#'*70}")
    
    thresholds = {}
    for kpi_name in df['kpi_name'].unique():
        kpi_data = df[df['kpi_name'] == kpi_name]['value'].dropna()
        if len(kpi_data) > 0:
            thresholds[kpi_name] = {
                'P95': np.percentile(kpi_data, 95),
                'P90': np.percentile(kpi_data, 90),
                'P50': np.percentile(kpi_data, 50)
            }
    
    print(f"计算了 {len(thresholds)} 个KPI的阈值")
    
    print(f"\n{'#'*70}")
    print(f"# 第四步：检测异常容器")
    print(f"{'#'*70}")
    
    anomalies = []
    
    for cmdb_id in filtered['cmdb_id'].unique():
        container_data = filtered[filtered['cmdb_id'] == cmdb_id]
        
        for kpi_name in container_data['kpi_name'].unique():
            if kpi_name not in thresholds:
                continue
            
            kpi_data = container_data[container_data['kpi_name'] == kpi_name]['value'].dropna()
            if len(kpi_data) == 0:
                continue
            
            mean_val = kpi_data.mean()
            max_val = kpi_data.max()
            threshold_p95 = thresholds[kpi_name]['P95']
            
            if mean_val > threshold_p95:
                deviation = (mean_val - threshold_p95) / threshold_p95
                
                if deviation > 0.5:
                    resource_type = classify_kpi(kpi_name)
                    anomalies.append({
                        'cmdb_id': cmdb_id,
                        'kpi_name': kpi_name,
                        'resource_type': resource_type,
                        'value': mean_val,
                        'max': max_val,
                        'threshold': threshold_p95,
                        'deviation': deviation
                    })
    
    if not anomalies:
        print(f"未检测到明显的容器资源异常（偏离>50%）")
    else:
        anomalies.sort(key=lambda x: x['deviation'], reverse=True)
        
        print(f"\n检测到 {len(anomalies)} 个容器资源异常：\n")
        
        for i, a in enumerate(anomalies[:15], 1):
            print(f"{i}. [{a['cmdb_id']}] {a['resource_type']}")
            print(f"   KPI: {a['kpi_name'][:50]}...")
            print(f"   均值={a['value']:.2f}, 阈值(P95)={a['threshold']:.2f}, 最大={a['max']:.2f}")
            print(f"   偏离程度: {a['deviation']*100:.1f}%")
            print()
    
    print(f"{'#'*70}")
    print(f"# 第五步：结论与建议")
    print(f"{'#'*70}")
    
    if anomalies:
        resource_counts = {}
        for a in anomalies:
            res = a['resource_type']
            cmdb = a['cmdb_id']
            key = f"{cmdb}:{res}"
            resource_counts[key] = resource_counts.get(key, 0) + 1
        
        sorted_resources = sorted(resource_counts.items(), key=lambda x: x[1], reverse=True)
        
        print(f"\n异常组件分布:")
        for key, count in sorted_resources[:5]:
            print(f"  {key}: {count} 个异常KPI")
        
        top = anomalies[0]
        print(f"\n最显著异常: {top['cmdb_id']}")
        print(f"资源类型: {top['resource_type']}")
        print(f"偏离阈值: {top['deviation']*100:.1f}%")
        
        reason_mapping = {
            'cpu': 'container CPU load',
            'memory': 'container memory load',
            'disk_read': 'container read I/O load',
            'disk_write': 'container write I/O load',
            'network': 'container network issue'
        }
        print(f"可能原因: {reason_mapping.get(top['resource_type'], '未知资源问题')}")
    else:
        print(f"\n建议: 检查服务层业务指标或链路追踪")


def main():
    parser = argparse.ArgumentParser(description='Container Analyzer for OpenRCA')
    parser.add_argument('--file', type=str, required=True, help='Container metric file path')
    parser.add_argument('--start', type=str, required=True, help='Start time (YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('--end', type=str, required=True, help='End time (YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('--component', type=str, help='Filter by component name (e.g., shippingservice)')
    
    args = parser.parse_args()
    
    if not Path(args.file).exists():
        print(f"错误: 文件不存在 {args.file}")
        sys.exit(1)
    
    tz = pytz.timezone('Asia/Shanghai')
    start_dt = tz.localize(datetime.strptime(args.start, '%Y-%m-%d %H:%M:%S'))
    end_dt = tz.localize(datetime.strptime(args.end, '%Y-%m-%d %H:%M:%S'))
    
    analyze_container_metrics(args.file, start_dt, end_dt, args.component)


if __name__ == '__main__':
    main()