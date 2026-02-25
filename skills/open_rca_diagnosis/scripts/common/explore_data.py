#!/usr/bin/env python3
"""
Data Explorer - 数据探索工具
探索CSV文件结构，帮助Agent了解数据模式

Usage:
    python explore_data.py --file <csv_path> [--sample-size 100]
"""

import argparse
import pandas as pd
import sys
from pathlib import Path
from collections import Counter


def explore_csv(file_path: str, sample_size: int = 100):
    """探索CSV文件结构"""
    path = Path(file_path)
    if not path.exists():
        print(f"错误: 文件不存在 {file_path}")
        return
    
    print(f"{'='*70}")
    print(f"数据探索报告: {path.name}")
    print(f"{'='*70}")
    
    df = pd.read_csv(file_path)
    
    print(f"\n## 基本信息")
    print(f"行数: {len(df):,}")
    print(f"列数: {len(df.columns)}")
    print(f"文件大小: {path.stat().st_size / 1024 / 1024:.2f} MB")
    
    print(f"\n## 列结构")
    print(f"列名: {list(df.columns)}")
    
    print(f"\n## 列类型")
    for col in df.columns:
        dtype = df[col].dtype
        null_count = df[col].isnull().sum()
        null_pct = null_count / len(df) * 100
        unique_count = df[col].nunique()
        print(f"  {col}: {dtype}, null={null_count}({null_pct:.1f}%), unique={unique_count}")
    
    print(f"\n## 数据样本 (前{sample_size}行)")
    print(df.head(sample_size).to_string())
    
    print(f"\n## 数值列统计")
    numeric_cols = df.select_dtypes(include=['number']).columns
    if len(numeric_cols) > 0:
        print(df[numeric_cols].describe().to_string())
    
    print(f"\n## 分类列分布 (Top 10)")
    for col in df.columns:
        if df[col].dtype == 'object' or df[col].nunique() < 20:
            value_counts = df[col].value_counts().head(10)
            if len(value_counts) > 1:
                print(f"\n  {col}:")
                for val, count in value_counts.items():
                    print(f"    {val}: {count} ({count/len(df)*100:.1f}%)")
    
    if 'timestamp' in df.columns:
        print(f"\n## 时间范围")
        ts = df['timestamp']
        print(f"  最小: {ts.min()}")
        print(f"  最大: {ts.max()}")
        print(f"  范围: {ts.max() - ts.min()} 单位")


def explore_directory(dir_path: str):
    """探索目录结构"""
    path = Path(dir_path)
    if not path.exists():
        print(f"错误: 目录不存在 {dir_path}")
        return
    
    print(f"{'='*70}")
    print(f"目录探索报告: {path}")
    print(f"{'='*70}")
    
    for root, dirs, files in path.rglob('*'):
        root = Path(root)
        csv_files = list(root.glob('*.csv'))
        if csv_files:
            print(f"\n{root.relative_to(path)}/")
            for f in csv_files:
                size_mb = f.stat().st_size / 1024 / 1024
                print(f"  {f.name}: {size_mb:.2f} MB")


def main():
    parser = argparse.ArgumentParser(description='Data Explorer for OpenRCA')
    parser.add_argument('--file', type=str, help='CSV file to explore')
    parser.add_argument('--dir', type=str, help='Directory to explore')
    parser.add_argument('--sample-size', type=int, default=100, help='Sample rows to show')
    
    args = parser.parse_args()
    
    if args.file:
        explore_csv(args.file, args.sample_size)
    elif args.dir:
        explore_directory(args.dir)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()