# Market Scene Specification - 电商场景规格

## 场景概述

本场景是一个电商平台微服务系统（Online Boutique），采用 Service Mesh 架构，具备故障转移机制。每个服务部署多个 Pod（容器）实例，分布于不同节点。

## 数据目录结构

```
{data_path}/
├── cloudbed-1/                    # 云环境 1
│   └── telemetry/
│       └── 2022_03_20/            # 按日期组织
│           ├── metric/
│           │   ├── metric_container.csv
│           │   ├── metric_mesh.csv
│           │   ├── metric_node.csv
│           │   ├── metric_runtime.csv
│           │   └── metric_service.csv
│           ├── trace/
│           │   └── trace_span.csv
│           └── log/
│               ├── log_proxy.csv
│               └── log_service.csv
├── cloudbed-2/                    # 云环境 2 (结构同上)
│   └── telemetry/...
```

## 数据模式定义

### 1. 容器层指标 (metric_container.csv)

| 字段名 | 类型 | 单位 | 描述 |
|--------|------|------|------|
| timestamp | int | 秒 | Unix 时间戳 |
| cmdb_id | string | - | 组件标识 (格式: `{node}-{x}.{service}-{x}`) |
| kpi_name | string | - | KPI 名称 |
| value | float | - | 指标值 |

**示例数据：**
```csv
timestamp,cmdb_id,kpi_name,value
1647781200,node-6.adservice2-0,container_fs_writes_MB./dev/vda,0.0
```

### 2. Service Mesh 指标 (metric_mesh.csv)

服务网格间通信指标。

| 字段名 | 类型 | 描述 |
|--------|------|------|
| timestamp | int | Unix 时间戳 (秒) |
| cmdb_id | string | Mesh 连接标识 (格式: `{pod}.source.{service}.{target-service}`) |
| kpi_name | string | KPI 名称 |
| value | float | 指标值 |

**示例数据：**
```csv
timestamp,cmdb_id,kpi_name,value
1647790380,cartservice-1.source.cartservice.redis-cart,istio_tcp_sent_bytes.-,1255.0
```

### 3. 节点层指标 (metric_node.csv)

| 字段名 | 类型 | 描述 |
|--------|------|------|
| timestamp | int | Unix 时间戳 (秒) |
| cmdb_id | string | 节点标识 (格式: `node-{x}`) |
| kpi_name | string | KPI 名称 |
| value | float | 指标值 |

**示例数据：**
```csv
timestamp,cmdb_id,kpi_name,value
1647705600,node-1,system.cpu.iowait,0.31
```

### 4. 运行时指标 (metric_runtime.csv)

JVM/应用运行时指标。

| 字段名 | 类型 | 描述 |
|--------|------|------|
| timestamp | int | Unix 时间戳 (秒) |
| cmdb_id | string | 应用标识 (格式: `{service}.{port}`) |
| kpi_name | string | KPI 名称 |
| value | float | 指标值 |

**示例数据：**
```csv
timestamp,cmdb_id,kpi_name,value
1647730800,adservice.ts:8088,java_nio_BufferPool_TotalCapacity.direct,57343.0
```

### 5. 服务层指标 (metric_service.csv)

服务级业务指标。

| 字段名 | 类型 | 单位 | 描述 |
|--------|------|------|------|
| service | string | - | 服务名称 (格式: `{service}-grpc`) |
| timestamp | int | 秒 | Unix 时间戳 |
| rr | float | % | 请求成功率 |
| sr | float | % | 服务成功率 |
| mrt | float | ms | 平均响应时间 |
| count | int | 次数 | 请求计数 |

**示例数据：**
```csv
service,timestamp,rr,sr,mrt,count
adservice-grpc,1647716400,100.0,100.0,2.429508196728182,61
```

### 6. 链路追踪 (trace_span.csv)

| 字段名 | 类型 | 描述 |
|--------|------|------|
| timestamp | int | Unix 时间戳 (毫秒) |
| cmdb_id | string | Pod 标识 (格式: `{service}-{x}`) |
| span_id | string | Span ID |
| trace_id | string | 追踪 ID |
| duration | int | 耗时 (ms) |
| type | string | 调用类型 |
| status_code | int | 状态码 |
| operation_name | string | 操作名称 |
| parent_span | string | 父 Span ID |

**示例数据：**
```csv
timestamp,cmdb_id,span_id,trace_id,duration,type,status_code,operation_name,parent_span
1647705600361,frontend-0,a652d4d10e9478fc,9451fd8fdf746a80687451dae4c4e984,49877,rpc,0,hipstershop.CheckoutService/PlaceOrder,952754a738a11675
```

### 7. 服务日志 (log_service.csv)

| 字段名 | 类型 | 描述 |
|--------|------|------|
| log_id | string | 日志 ID |
| timestamp | int | Unix 时间戳 (秒) |
| cmdb_id | string | Pod 标识 |
| log_name | string | 日志类型 |
| value | string | 日志内容 |

**示例数据：**
```csv
log_id,timestamp,cmdb_id,log_name,value
GIvpon8BDiVcQfZwJ5a9,1647705660,currencyservice-0,log_currencyservice-service_application,"severity: info, message: Getting supported currencies..."
```

### 8. 代理日志 (log_proxy.csv)

| 字段名 | 类型 | 描述 |
|--------|------|------|
| log_id | string | 日志 ID |
| timestamp | int | Unix 时间戳 (秒) |
| cmdb_id | string | Pod 标识 |
| log_name | string | 日志类型 |
| value | string | 日志内容 |

**示例数据：**
```csv
log_id,timestamp,cmdb_id,log_name,value
KN43pn8BmS57GQLkQUdP,1647761110,cartservice-1,log_cartservice-service_application,etCartAsync called with userId=3af80013-c2c1-4ae6-86d0-1d9d308e6f5b
```

## 候选根因组件

### Node 层组件

| 组件 ID | 描述 |
|---------|------|
| node-1 ~ node-6 | 6 个物理/虚拟机节点 |

### Pod 层组件 (Container)

| 服务 | Pod 列表 |
|------|----------|
| frontend | frontend-0, frontend-1, frontend-2, frontend2-0 |
| shippingservice | shippingservice-0/1/2, shippingservice2-0 |
| checkoutservice | checkoutservice-0/1/2, checkoutservice2-0 |
| currencyservice | currencyservice-0/1/2, currencyservice2-0 |
| adservice | adservice-0/1/2, adservice2-0 |
| emailservice | emailservice-0/1/2, emailservice2-0 |
| cartservice | cartservice-0/1/2, cartservice2-0 |
| productcatalogservice | productcatalogservice-0/1/2, productcatalogservice2-0 |
| recommendationservice | recommendationservice-0/1/2, recommendationservice2-0 |
| paymentservice | paymentservice-0/1/2, paymentservice2-0 |

### Service 层组件

| 组件 ID | 描述 |
|---------|------|
| frontend | 前端服务 |
| shippingservice | 配送服务 |
| checkoutservice | 结账服务 |
| currencyservice | 货币服务 |
| adservice | 广告服务 |
| emailservice | 邮件服务 |
| cartservice | 购物车服务 |
| productcatalogservice | 商品目录服务 |
| recommendationservice | 推荐服务 |
| paymentservice | 支付服务 |

## 候选根因原因

### Container 层原因

| 原因 |
|------|
| container CPU load |
| container memory load |
| container network packet retransmission |
| container network packet corruption |
| container network latency |
| container packet loss |
| container process termination |
| container read I/O load |
| container write I/O load |

### Node 层原因

| 原因 |
|------|
| node CPU load |
| node CPU spike |
| node memory consumption |
| node disk read I/O consumption |
| node disk write I/O consumption |
| node disk space consumption |

## 组件标识 (cmdb_id) 格式约定

| 数据类型 | cmdb_id 格式 | 示例 |
|----------|--------------|------|
| Container Metric | `{node}-{x}.{service}-{x}` | `node-1.adservice-0` |
| Node Metric | `{node}-{x}` | `node-1` |
| Service Metric | `{service}-grpc` | `adservice-grpc` |
| Runtime Metric | `{service}.{port}` | `adservice.ts:8088` |
| Mesh Metric | `{pod}.source.{service}.{target}` | `cartservice-1.source.cartservice.redis-cart` |
| Trace | `{service}-{x}` | `frontend-0` |
| Log | `{service}-{x}` | `currencyservice-0` |

## 时间戳单位约定

| 数据类型 | 时间戳单位 | 示例 |
|----------|------------|------|
| Metric | 秒 | 1647781200 |
| Trace | 毫秒 | 1647705600361 |
| Log | 秒 | 1647705660 |

## 时区设置

所有问题均使用 **UTC+8** 时间。

## 系统特点

1. **故障转移机制**：每个服务部署多个 Pod 实例
2. **双云环境**：数据分布在 cloudbed-1 和 cloudbed-2
3. **Service Mesh**：使用 Istio 进行服务网格治理
4. **层级关系**：Pod 部署在特定 Node 上，同一服务的所有 Pod 故障 => 服务级故障
5. **故障传播**：服务级故障可通过调用链传播到下游服务
6. **Pod = Container**：在此系统中 Pod 与 Container 概念等同

## 场景脚本使用

### 1. 服务层分析 (analyze_metric.py)

识别异常服务。

```bash
python scripts/market/analyze_metric.py \
  --file metric_service.csv \
  --start "2022-03-20 09:00:00" \
  --end "2022-03-20 09:30:00"
```

**参数说明：**
| 参数 | 说明 |
|------|------|
| `--file` | 服务层指标文件路径 |
| `--start` | 分析开始时间 (UTC+8) |
| `--end` | 分析结束时间 (UTC+8) |

**输出：** 异常服务列表，按偏离程度排序

### 2. 容器层分析 (analyze_container.py)

定位异常容器和资源瓶颈。

```bash
python scripts/market/analyze_container.py \
  --file metric_container.csv \
  --start "2022-03-20 09:00:00" \
  --end "2022-03-20 09:30:00" \
  --component shippingservice
```

**参数说明：**
| 参数 | 说明 |
|------|------|
| `--file` | 容器层指标文件路径 |
| `--start` | 分析开始时间 (UTC+8) |
| `--end` | 分析结束时间 (UTC+8) |
| `--component` | (可选) 过滤特定服务的容器 |

**输出：** 异常容器及其资源指标详情

### 3. 链路验证 (analyze_trace.py)

确认调用链故障点。

```bash
python scripts/market/analyze_trace.py \
  --file trace_span.csv \
  --time-range "1647738000000,1647739800000" \
  --errors-by-component
```

**参数说明：**
| 参数 | 说明 |
|------|------|
| `--file` | 链路追踪文件路径 |
| `--time-range` | 时间戳范围 (毫秒)，格式: `起始,结束` |
| `--errors-by-component` | 按组件聚合错误统计 |

**输出：** 错误 span 分布、耗时异常 span

### 4. 日志验证 (analyze_log.py)

确认根因原因。

```bash
python scripts/market/analyze_log.py \
  --file log_service.csv \
  --time-range "1647738000,1647739800" \
  --component shippingservice \
  --errors
```

**参数说明：**
| 参数 | 说明 |
|------|------|
| `--file` | 服务日志文件路径 |
| `--time-range` | 时间戳范围 (秒)，格式: `起始,结束` |
| `--component` | (可选) 过滤特定组件日志 |
| `--errors` | 只显示错误级别日志 |

**输出：** 错误日志摘要、关键错误信息

### 分析流程示例

```bash
# Step 1: 服务层分析 → 得到异常服务 (如 shippingservice)
python scripts/market/analyze_metric.py --file metric_service.csv --start "..." --end "..."

# Step 2: 容器层分析 → 得到异常容器和资源问题
python scripts/market/analyze_container.py --file metric_container.csv --component shippingservice --start "..." --end "..."

# Step 3: 链路验证 → 确认故障传播路径
python scripts/market/analyze_trace.py --file trace_span.csv --time-range "..."

# Step 4: 日志验证 → 确认根因原因
python scripts/market/analyze_log.py --file log_service.csv --component shippingservice --errors
```