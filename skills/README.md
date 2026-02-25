## Skills(技能)

We use Skills to organize the resources needed by the Agent. The resources included in Skills are as follows:

1. MCP Server
2. Tools/Scripts
3. Knowledge
4. Datasets For eval

## Content Schema 

In OpenDerisk Skills, we use the `SPEC` specification based on `markdown` text for skill organization and description, and strictly adhere to the [Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) specification published by Anthropics through relevant specifications. Based on domain considerations, we have made certain extensions.

### File Structure
```
skills/
├── logskill/
│   ├── SKILL.md
│   ├── KNOWLEDGE.md
│   ├── tools/
│   │   └── INDEX.md 
│   │   ├── __init__.py
│   │   └── logutil.py 
│   │   └── analysis.py 
│   ├── knowledge/
│   │   └── deepwiki.md 
│   │   └── error_code.md 
├── README.md
```

### Content Format 

#### SKILL.md
```
---
name: Log Operate and Analysis Statements
description: This skill can Analysis and operate log files
---

# Log Operate and Analysis Skill 

This skill provides system log operate and analysis for find the root cause of the system.

## Capabilities
- 

## How to Use

## Input Format

## Output Format

## Scripts

## Best Practices

## Limitations

```

#### Knowledge.md

```
---
name: Log Operate and Analysis Statements
description: This knowledge explain the background and log format
---

# Log Operate and Analysis Knowledge 

## Abstract

1. This microservice system is a banking platform.

2. The `metric_app.csv` file only contains four KPIs: rr, sr, cnt, and mrt,. In contrast, `metric_container.csv` records a variety of KPIs, such as CPU usage and memory usage. The specific names of these KPIs can be found in the `kpi_name` field.

3. In different telemetry files, the timestamp units and cmdb_id formats may vary:

- Metric: Timestamp units are in seconds (e.g., 1614787440).

- Trace: Timestamp units are in milliseconds (e.g., 1614787199628).

- Log: Timestamp units are in seconds (e.g., 1614787201).

4. Please use the UTC+8 time zone in all analysis steps since system is deployed in China/Hong Kong/Singapore."""

## Introduction

## Index
> The index can reference data in the knowledge base, which we manage using namespaces.
- `derisk-rag@log@schema`
- `dify-rag@rca@logs`
- `llama-rag@financial@pay`

## Best Practices

## Limitations

```

