#!/usr/bin/env python3
"""
Trace Analysis Tool for OpenRCA
链路追踪分析工具 - 分析调用链路和故障传播

Usage:
    python analyze_trace.py --file <trace_csv> --time-range <start>,<end>
    
Examples:
    # 分析时间范围内的trace
    python analyze_trace.py --file trace_span.csv --time-range "1647781200000,1647784800000"
    
    # 按组件统计错误
    python analyze_trace.py --file trace_span.csv --errors-by-component
    
    # 分析最慢的调用链
    python analyze_trace.py --file trace_span.csv --slow-traces --top 10
"""

import argparse
import pandas as pd
import sys
from pathlib import Path
from collections import defaultdict


def analyze_errors_by_component(df: pd.DataFrame) -> pd.DataFrame:
    """按组件统计错误"""
    errors = df[df['status_code'] != 0] if 'status_code' in df.columns else pd.DataFrame()
    
    if len(errors) == 0:
        print("未发现错误trace")
        return pd.DataFrame()
    
    error_stats = errors.groupby('cmdb_id').agg({
        'trace_id': 'count',
        'duration': ['mean', 'max']
    }).reset_index()
    
    error_stats.columns = ['cmdb_id', 'error_count', 'avg_duration', 'max_duration']
    error_stats = error_stats.sort_values('error_count', ascending=False)
    
    return error_stats


def analyze_slow_traces(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """分析最慢的trace"""
    if 'duration' not in df.columns:
        print("缺少 duration 列")
        return pd.DataFrame()
    
    slowest = df.nlargest(top_n, 'duration')[['trace_id', 'cmdb_id', 'duration', 'timestamp']]
    return slowest


def analyze_call_chain(df: pd.DataFrame, trace_id: str) -> pd.DataFrame:
    """分析单个trace的调用链"""
    trace_data = df[df['trace_id'] == trace_id].copy()
    
    if len(trace_data) == 0:
        print(f"未找到 trace_id: {trace_id}")
        return pd.DataFrame()
    
    if 'parent_span' in trace_data.columns and 'span_id' in trace_data.columns:
        trace_data = trace_data.sort_values('timestamp')
    
    return trace_data


def main():
    parser = argparse.ArgumentParser(description='Trace Analysis Tool for OpenRCA')
    parser.add_argument('--file', type=str, required=True, help='Trace CSV file path')
    parser.add_argument('--time-range', type=str, help='Time range (start_ms,end_ms)')
    parser.add_argument('--errors-by-component', action='store_true', help='Group errors by component')
    parser.add_argument('--slow-traces', action='store_true', help='Find slowest traces')
    parser.add_argument('--trace-id', type=str, help='Analyze specific trace')
    parser.add_argument('--top', type=int, default=10, help='Top N results')
    parser.add_argument('--output', type=str, help='Output file path')
    
    args = parser.parse_args()
    
    path = Path(args.file)
    if not path.exists():
        print(f"错误: 文件不存在 {args.file}")
        sys.exit(1)
    
    df = pd.read_csv(args.file)
    print(f"加载trace数据: {len(df)} 条")
    print(f"列: {list(df.columns)}")
    
    if args.time_range:
        start, end = map(int, args.time_range.split(','))
        df = df[(df['timestamp'] >= start) & (df['timestamp'] <= end)]
        print(f"时间范围过滤后: {len(df)} 条")
    
    if args.errors_by_component:
        print(f"\n{'='*60}")
        print("按组件统计错误:")
        print(f"{'='*60}")
        error_stats = analyze_errors_by_component(df)
        if len(error_stats) > 0:
            print(error_stats.to_string(index=False))
        
        if args.output:
            error_stats.to_csv(args.output, index=False)
    
    elif args.slow_traces:
        print(f"\n{'='*60}")
        print(f"最慢的 {args.top} 条trace:")
        print(f"{'='*60}")
        slowest = analyze_slow_traces(df, args.top)
        print(slowest.to_string(index=False))
        
        if args.output:
            slowest.to_csv(args.output, index=False)
    
    elif args.trace_id:
        print(f"\n{'='*60}")
        print(f"Trace调用链分析: {args.trace_id}")
        print(f"{'='*60}")
        chain = analyze_call_chain(df, args.trace_id)
        if len(chain) > 0:
            print(chain.to_string(index=False))
    
    else:
        print(f"\n{'='*60}")
        print("Trace概览:")
        print(f"{'='*60}")
        
        if 'status_code' in df.columns:
            errors = df[df['status_code'] != 0]
            print(f"总trace数: {df['trace_id'].nunique()}")
            print(f"总span数: {len(df)}")
            print(f"错误span数: {len(errors)}")
            print(f"错误率: {len(errors)/len(df)*100:.2f}%")
        
        if 'duration' in df.columns:
            print(f"\nDuration统计:")
            print(f"  平均: {df['duration'].mean():.2f}ms")
            print(f"  最大: {df['duration'].max():.2f}ms")
            print(f"  P95: {df['duration'].quantile(0.95):.2f}ms")
        
        print(f"\n组件分布 (前10):")
        print(df['cmdb_id'].value_counts().head(10).to_string())


if __name__ == '__main__':
    main()