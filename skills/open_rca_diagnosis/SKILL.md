---
name: open_rca_diagnosis
description: AI驱动的微服务故障根因分析技能，提供分析指导和场景化工具脚本
type: analysis
author: derisk
version: "2.0"
category: observability
tags:
  - rca
  - fault-diagnosis
  - observability
  - sre
  - microservices
scripts:
  common:
    - scripts/common/explore_data.py
    - scripts/common/time_utils.py
  market:
    - scripts/market/analyze_metric.py
    - scripts/market/analyze_container.py
    - scripts/market/analyze_trace.py
    - scripts/market/analyze_log.py
  bank: []
  telecom: []
---

# 故障根因分析技能 (Open RCA Diagnosis)

## 技能概述

本技能提供故障根因诊断的完整框架，包含两种分析方式：

### 方式一：使用场景化脚本（推荐）

每个场景提供专用的分析脚本，针对特定数据结构优化。

### 方式二：动态代码分析

使用通用工具探索数据结构，根据实际情况编写分析代码。

## 脚本目录结构

```
scripts/
├── common/                    # 通用工具
│   ├── explore_data.py        # 数据探索
│   └── time_utils.py          # 时间转换
├── market/                    # Market场景专用
│   ├── analyze_metric.py      # 服务指标分析
│   ├── analyze_container.py   # 容器资源分析
│   ├── analyze_trace.py       # 链路追踪分析
│   └── analyze_log.py         # 日志分析
├── bank/                      # Bank场景专用（待补充）
└── telecom/                   # Telecom场景专用（待补充）
```

---

## 方式一：场景化脚本使用

每个场景提供专用的分析脚本，具体使用方法见各场景规格文档：

| 场景 | 规格文档 | 可用脚本 |
|------|----------|----------|
| Market | `specs/market_spec.md` | analyze_metric, analyze_container, analyze_trace, analyze_log |
| Bank | `specs/bank_spec.md` | 待补充 |
| Telecom | `specs/telecom_spec.md` | 待补充 |

### 通用工具

**数据探索：**
```bash
python scripts/common/explore_data.py --dir /path/to/telemetry
python scripts/common/explore_data.py --file metric_service.csv
```

**时间转换：**
```bash
python scripts/common/time_utils.py --range "2022-03-20 09:00:00" "2022-03-20 09:30:00"
```

---

## 方式二：动态代码分析

当场景脚本不适用时，Agent可以：

### 1. 探索数据结构

```bash
python scripts/common/explore_data.py --file <数据文件>
```

**输出内容：**
- 行数、列数、文件大小
- 每列的数据类型、空值比例、唯一值数量
- 数据样本
- 数值列统计
- 分类列分布

### 2. 根据数据结构编写分析代码

使用IPython或Python脚本，参考以下模板：

```python
import pandas as pd
import numpy as np

# 1. 加载数据
df = pd.read_csv('<数据文件>')

# 2. 计算全局阈值（使用完整数据！）
threshold_p95 = df['<指标列>'].quantile(0.95)

# 3. 过滤时间窗口
start_ts = <开始时间戳>
end_ts = <结束时间戳>
filtered = df[(df['timestamp'] >= start_ts) & (df['timestamp'] <= end_ts)]

# 4. 检测异常
anomalies = filtered[filtered['<指标列>'] > threshold_p95]

# 5. 聚合分析
print(anomalies.groupby('<组件列>').agg({
    '<指标列>': ['mean', 'max', 'count']
}))
```

### 3. 关键分析原则

| 原则 | 说明 |
|------|------|
| 全局阈值 | 用完整数据计算阈值，不要用过滤后的数据 |
| 时区统一 | 使用UTC+8时区 |
| 层次化分析 | 服务层 → 容器层 → 节点层 |
| 交叉验证 | 指标 + 链路 + 日志 |

---

## 场景规格

详见 `specs/` 目录：
- `market_spec.md` - Market场景数据结构和候选根因
- `bank_spec.md` - Bank场景数据结构
- `telecom_spec.md` - Telecom场景数据结构

---

## 诊断工作流程

```
1. 确认场景 → 加载场景规格
     ↓
2. 数据探索 → 了解数据结构
     ↓
3. 时间转换 → 确定分析窗口
     ↓
4. 服务层分析 → 识别异常服务
     ↓
5. 容器层分析 → 定位异常容器和资源
     ↓
6. 链路验证 → 确认调用链故障点
     ↓
7. 日志验证 → 确认根因原因
     ↓
8. 生成报告
```

---

## 输出规范

```markdown
## 根因定位结果

**根因组件:** [组件ID]
**根因原因:** [原因描述]
**置信度:** [基于偏离程度]

### 分析过程
[按步骤描述分析结果和推理过程]

### 证据链
1. [服务层证据]
2. [容器层证据]
3. [链路/日志证据]
```

---

## 版本历史

| 版本 | 日期 | 更新内容 |
|------|------|----------|
| 2.0 | 2025-02 | 重构为场景化脚本 + 动态代码分析两种模式 |
| 1.0 | 2024-01 | 初始版本 |