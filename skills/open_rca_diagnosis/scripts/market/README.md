# Market场景分析脚本

## 数据结构
- 服务层指标: metric_service.csv (service, timestamp, rr, sr, mrt, count)
- 容器层指标: metric_container.csv (timestamp, cmdb_id, kpi_name, value)  
- 链路追踪: trace_span.csv (timestamp, cmdb_id, trace_id, span_id, duration, status_code)
- 日志: log_service.csv, log_proxy.csv (timestamp, cmdb_id, value)

## 脚本使用

### 服务层分析
```bash
python scripts/market/analyze_metric.py \
  --file metric_service.csv \
  --start "2022-03-20 09:00:00" \
  --end "2022-03-20 09:30:00"
```

### 容器层分析
```bash
python scripts/market/analyze_container.py \
  --file metric_container.csv \
  --start "2022-03-20 09:00:00" \
  --end "2022-03-20 09:30:00" \
  --component shippingservice
```

### 链路追踪分析
```bash
python scripts/market/analyze_trace.py \
  --file trace_span.csv \
  --time-range "1647738000000,1647739800000" \
  --errors-by-component
```

### 日志分析
```bash
python scripts/market/analyze_log.py \
  --file log_service.csv \
  --time-range "1647738000,1647739800" \
  --component shippingservice \
  --errors
```