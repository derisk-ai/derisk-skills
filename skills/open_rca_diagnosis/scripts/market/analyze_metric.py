#!/usr/bin/env python3
"""
Metric Analyzer for OpenRCA - 服务指标分析工具
一次性完成：加载数据 + 计算阈值 + 过滤时间 + 检测异常

Usage:
    python analyze_metric.py --file metric_service.csv --start "2022-03-20 09:00:00" --end "2022-03-20 09:30:00"
    
Output: 直接输出分析结果到stdout，供Agent解析
"""

import argparse
import pandas as pd
import numpy as np
from datetime import datetime
import pytz
import sys
from pathlib import Path


def analyze_service_metrics(file_path: str, start_dt: datetime, end_dt: datetime):
    """分析服务层指标"""
    tz = pytz.timezone('Asia/Shanghai')
    start_ts = int(start_dt.timestamp())
    end_ts = int(end_dt.timestamp())
    
    df = pd.read_csv(file_path)
    
    print(f"{'='*70}")
    print(f"服务层指标分析报告")
    print(f"{'='*70}")
    print(f"数据文件: {file_path}")
    print(f"总数据量: {len(df)} 条")
    print(f"时间范围: {start_dt} ~ {end_dt}")
    print(f"分析时间: {datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}")
    
    print(f"\n{'#'*70}")
    print(f"# 第一步：计算全局阈值（使用完整数据）")
    print(f"{'#'*70}")
    
    thresholds = {}
    for col in ['rr', 'sr', 'mrt']:
        values = df[col].dropna()
        thresholds[col] = {
            'P95': np.percentile(values, 95),
            'P90': np.percentile(values, 90),
            'P75': np.percentile(values, 75),
            'P50': np.percentile(values, 50),
            'P25': np.percentile(values, 25),
            'P10': np.percentile(values, 10),
            'P5': np.percentile(values, 5)
        }
        print(f"{col}: P95={thresholds[col]['P95']:.2f}, P50={thresholds[col]['P50']:.2f}, P5={thresholds[col]['P5']:.2f}")
    
    print(f"\n{'#'*70}")
    print(f"# 第二步：过滤故障时间窗口数据")
    print(f"{'#'*70}")
    
    filtered = df[(df['timestamp'] >= start_ts) & (df['timestamp'] <= end_ts)]
    print(f"时间窗口内数据: {len(filtered)} 条")
    
    if len(filtered) == 0:
        print(f"警告: 指定时间范围内无数据！")
        print(f"数据时间范围: {df['timestamp'].min()} ~ {df['timestamp'].max()}")
        return
    
    print(f"\n{'#'*70}")
    print(f"# 第三步：检测异常 - 服务层")
    print(f"{'#'*70}")
    
    anomalies = []
    
    for service in filtered['service'].unique():
        svc_data = filtered[filtered['service'] == service]
        
        for kpi in ['rr', 'sr']:
            values = svc_data[kpi].dropna()
            if len(values) == 0:
                continue
            
            mean_val = values.mean()
            min_val = values.min()
            threshold_p5 = thresholds[kpi]['P5']
            
            if mean_val < threshold_p5:
                deviation = (threshold_p5 - mean_val) / threshold_p5
                anomalies.append({
                    'service': service,
                    'kpi': kpi,
                    'value': mean_val,
                    'min': min_val,
                    'threshold': threshold_p5,
                    'type': 'below',
                    'deviation': deviation
                })
        
        for kpi in ['mrt']:
            values = svc_data[kpi].dropna()
            if len(values) == 0:
                continue
            
            mean_val = values.mean()
            max_val = values.max()
            threshold_p95 = thresholds[kpi]['P95']
            
            if mean_val > threshold_p95:
                deviation = (mean_val - threshold_p95) / threshold_p95
                anomalies.append({
                    'service': service,
                    'kpi': kpi,
                    'value': mean_val,
                    'max': max_val,
                    'threshold': threshold_p95,
                    'type': 'above',
                    'deviation': deviation
                })
    
    if not anomalies:
        print(f"未检测到明显异常")
        print(f"\n建议：尝试放宽阈值（如使用P90替代P95）")
    else:
        anomalies.sort(key=lambda x: x['deviation'], reverse=True)
        
        print(f"\n检测到 {len(anomalies)} 个异常指标：\n")
        
        for i, a in enumerate(anomalies, 1):
            direction = '↓' if a['type'] == 'below' else '↑'
            extremum = f"min={a.get('min', a.get('max', 'N/A')):.2f}"
            print(f"{i}. [{a['service']}] {a['kpi']} {direction}")
            print(f"   均值={a['value']:.2f}, 阈值(P{'5' if a['type']=='below' else '95'})={a['threshold']:.2f}, {extremum}")
            print(f"   偏离程度: {a['deviation']*100:.1f}%")
            print()
    
    print(f"{'#'*70}")
    print(f"# 第四步：结论与建议")
    print(f"{'#'*70}")
    
    if anomalies:
        top = anomalies[0]
        print(f"\n最显著异常: {top['service']} - {top['kpi']}")
        print(f"偏离阈值: {top['deviation']*100:.1f}%")
        print(f"\n建议: 分析该服务的容器层指标和链路追踪")
    else:
        print(f"\n建议: 检查容器层资源指标 (CPU/Memory/Disk I/O)")


def main():
    parser = argparse.ArgumentParser(description='Metric Analyzer for OpenRCA')
    parser.add_argument('--file', type=str, required=True, help='Metric CSV file path (e.g., metric_service.csv)')
    parser.add_argument('--start', type=str, required=True, help='Start time (YYYY-MM-DD HH:MM:SS)')
    parser.add_argument('--end', type=str, required=True, help='End time (YYYY-MM-DD HH:MM:SS)')
    
    args = parser.parse_args()
    
    if not Path(args.file).exists():
        print(f"错误: 文件不存在 {args.file}")
        sys.exit(1)
    
    tz = pytz.timezone('Asia/Shanghai')
    start_dt = tz.localize(datetime.strptime(args.start, '%Y-%m-%d %H:%M:%S'))
    end_dt = tz.localize(datetime.strptime(args.end, '%Y-%m-%d %H:%M:%S'))
    
    analyze_service_metrics(args.file, start_dt, end_dt)


if __name__ == '__main__':
    main()