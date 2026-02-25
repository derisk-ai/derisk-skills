#!/usr/bin/env python3
"""
Log Analysis Tool for OpenRCA
日志分析工具 - 分析错误日志和关键信息

Usage:
    python analyze_log.py --file <log_csv> --time-range <start>,<end>
    
Examples:
    # 分析时间范围内的错误日志
    python analyze_log.py --file log_service.csv --time-range "1647781200,1647784800" --errors
    
    # 搜索包含特定关键词的日志
    python analyze_log.py --file log_service.csv --search "error|exception"
    
    # 按组件统计日志
    python analyze_log.py --file log_service.csv --by-component
"""

import argparse
import pandas as pd
import sys
import re
from pathlib import Path


def search_logs(df: pd.DataFrame, pattern: str, case_sensitive: bool = False) -> pd.DataFrame:
    """搜索包含特定模式的日志"""
    if 'value' not in df.columns:
        print("错误: 缺少 'value' 列")
        return pd.DataFrame()
    
    flags = 0 if case_sensitive else re.IGNORECASE
    mask = df['value'].str.contains(pattern, regex=True, flags=flags, na=False)
    return df[mask]


def analyze_errors(df: pd.DataFrame) -> pd.DataFrame:
    """分析错误日志"""
    error_patterns = ['error', 'exception', 'fail', 'critical', 'fatal', 'timeout']
    pattern = '|'.join(error_patterns)
    return search_logs(df, pattern, case_sensitive=False)


def analyze_by_component(df: pd.DataFrame) -> pd.DataFrame:
    """按组件统计日志"""
    if 'cmdb_id' not in df.columns:
        print("错误: 缺少 'cmdb_id' 列")
        return pd.DataFrame()
    
    stats = df.groupby('cmdb_id').size().reset_index(name='log_count')
    stats = stats.sort_values('log_count', ascending=False)
    return stats


def main():
    parser = argparse.ArgumentParser(description='Log Analysis Tool for OpenRCA')
    parser.add_argument('--file', type=str, required=True, help='Log CSV file path')
    parser.add_argument('--time-range', type=str, help='Time range (start_ts,end_ts)')
    parser.add_argument('--errors', action='store_true', help='Find error logs')
    parser.add_argument('--search', type=str, help='Search pattern (regex)')
    parser.add_argument('--by-component', action='store_true', help='Group by component')
    parser.add_argument('--component', type=str, help='Filter by component name')
    parser.add_argument('--top', type=int, default=10, help='Top N results')
    parser.add_argument('--output', type=str, help='Output file path')
    
    args = parser.parse_args()
    
    path = Path(args.file)
    if not path.exists():
        print(f"错误: 文件不存在 {args.file}")
        sys.exit(1)
    
    df = pd.read_csv(args.file)
    print(f"加载日志数据: {len(df)} 条")
    print(f"列: {list(df.columns)}")
    
    if args.time_range:
        start, end = map(int, args.time_range.split(','))
        df = df[(df['timestamp'] >= start) & (df['timestamp'] <= end)]
        print(f"时间范围过滤后: {len(df)} 条")
    
    if args.component:
        df = df[df['cmdb_id'].str.contains(args.component, case=False, na=False)]
        print(f"组件过滤后: {len(df)} 条")
    
    if args.errors:
        print(f"\n{'='*60}")
        print("错误日志分析:")
        print(f"{'='*60}")
        errors = analyze_errors(df)
        print(f"错误日志数: {len(errors)}")
        
        if len(errors) > 0:
            print(f"\n按组件分布:")
            error_by_comp = errors['cmdb_id'].value_counts().head(args.top)
            print(error_by_comp.to_string())
            
            print(f"\n示例日志 (前{args.top}条):")
            for idx, row in errors.head(args.top).iterrows():
                ts = row.get('timestamp', 'N/A')
                comp = row.get('cmdb_id', 'N/A')
                value = row.get('value', '')[:100]
                print(f"  [{ts}] {comp}: {value}...")
        
        if args.output:
            errors.to_csv(args.output, index=False)
    
    elif args.search:
        print(f"\n{'='*60}")
        print(f"搜索结果 (pattern: {args.search}):")
        print(f"{'='*60}")
        results = search_logs(df, args.search)
        print(f"匹配日志数: {len(results)}")
        
        if len(results) > 0:
            print(f"\n示例 (前{args.top}条):")
            for idx, row in results.head(args.top).iterrows():
                ts = row.get('timestamp', 'N/A')
                comp = row.get('cmdb_id', 'N/A')
                value = row.get('value', '')[:100]
                print(f"  [{ts}] {comp}: {value}...")
        
        if args.output:
            results.to_csv(args.output, index=False)
    
    elif args.by_component:
        print(f"\n{'='*60}")
        print("按组件统计:")
        print(f"{'='*60}")
        stats = analyze_by_component(df)
        print(stats.head(args.top).to_string(index=False))
        
        if args.output:
            stats.to_csv(args.output, index=False)
    
    else:
        print(f"\n{'='*60}")
        print("日志概览:")
        print(f"{'='*60}")
        print(f"总日志数: {len(df)}")
        
        if 'cmdb_id' in df.columns:
            print(f"唯一组件数: {df['cmdb_id'].nunique()}")
            print(f"\nTop {args.top} 组件:")
            print(df['cmdb_id'].value_counts().head(args.top).to_string())
        
        print(f"\n示例日志 (前{args.top}条):")
        for idx, row in df.head(args.top).iterrows():
            ts = row.get('timestamp', 'N/A')
            comp = row.get('cmdb_id', 'N/A')
            value = row.get('value', '')[:80]
            print(f"  [{ts}] {comp}: {value}...")


if __name__ == '__main__':
    main()