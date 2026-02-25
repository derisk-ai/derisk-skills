#!/usr/bin/env python3
"""
Time Converter for OpenRCA
时间转换工具 - 支持不同时间格式转换

Usage:
    python time_utils.py --to-timestamp "2022-03-20 09:00:00"
    python time_utils.py --to-datetime 1647781200
    python time_utils.py --range "2022-03-20 09:00:00" "2022-03-20 09:30:00"
"""

import argparse
from datetime import datetime
import pytz
import sys


def datetime_to_timestamp(dt_str: str, timezone: str = 'Asia/Shanghai') -> tuple:
    """日期时间字符串转时间戳"""
    tz = pytz.timezone(timezone)
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    dt = tz.localize(dt)
    
    ts_seconds = int(dt.timestamp())
    ts_milliseconds = int(dt.timestamp() * 1000)
    
    return ts_seconds, ts_milliseconds, dt


def timestamp_to_datetime(ts: int, timezone: str = 'Asia/Shanghai', unit: str = 's') -> str:
    """时间戳转日期时间字符串"""
    tz = pytz.timezone(timezone)
    
    if unit == 'ms':
        ts = ts / 1000
    
    dt = datetime.fromtimestamp(ts, tz=tz)
    return dt.strftime('%Y-%m-%d %H:%M:%S')


def main():
    parser = argparse.ArgumentParser(description='Time Converter for OpenRCA')
    parser.add_argument('--to-timestamp', type=str, help='Convert datetime to timestamp')
    parser.add_argument('--to-datetime', type=int, help='Convert timestamp to datetime')
    parser.add_argument('--range', type=str, nargs=2, help='Convert time range to timestamps')
    parser.add_argument('--unit', type=str, default='s', choices=['s', 'ms'], help='Timestamp unit')
    parser.add_argument('--timezone', type=str, default='Asia/Shanghai', help='Timezone')
    
    args = parser.parse_args()
    
    if args.to_timestamp:
        ts_s, ts_ms, dt = datetime_to_timestamp(args.to_timestamp, args.timezone)
        print(f"输入时间: {args.to_timestamp}")
        print(f"时区: {args.timezone}")
        print(f"秒级时间戳: {ts_s}")
        print(f"毫秒级时间戳: {ts_ms}")
        print(f"本地化时间: {dt}")
    
    elif args.to_datetime:
        dt_str = timestamp_to_datetime(args.to_datetime, args.timezone, args.unit)
        print(f"输入时间戳: {args.to_datetime} ({args.unit})")
        print(f"转换结果: {dt_str}")
        print(f"时区: {args.timezone}")
    
    elif args.range:
        start, end = args.range
        start_s, start_ms, _ = datetime_to_timestamp(start, args.timezone)
        end_s, end_ms, _ = datetime_to_timestamp(end, args.timezone)
        
        print(f"时间范围: {start} ~ {end}")
        print(f"时区: {args.timezone}")
        print(f"\n秒级时间戳:")
        print(f"  开始: {start_s}")
        print(f"  结束: {end_s}")
        print(f"\n毫秒级时间戳:")
        print(f"  开始: {start_ms}")
        print(f"  结束: {end_ms}")
        print(f"\n过滤条件(--filters):")
        print(f'  "timestamp>={start_s},timestamp<={end_s}"')
    
    else:
        parser.print_help()


if __name__ == '__main__':
    main()