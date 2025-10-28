# Root Cause Analysis (RCA)

**Deep research and analysis for incident root cause determination**

## Overview

This skill provides comprehensive guidance on conducting effective root cause analysis (RCA) for production incidents, system failures, and performance issues using OpenDeRisk's multi-agent approach and proven methodologies.

## When This Skill Activates

- "Find the root cause of this incident"
- "Analyze this production issue"
- "Why did the system fail?"
- "Conduct an RCA for this outage"
- "Investigate the cause of performance degradation"
- "Trace back this error to its source"

## Key Features

- **Multi-Agent Collaboration**: Leverage SRE-Agent, Code-Agent, and Data-Agent
- **Evidence Chain Visualization**: Track investigation path and findings
- **Log Analysis**: Correlation across distributed systems
- **Trace Analysis**: Distributed tracing for microservices
- **Code-Level Investigation**: Identify bugs and misconfigurations
- **Metric Correlation**: Link performance metrics to root causes
- **5 Whys Method**: Systematic questioning technique
- **Fishbone Diagrams**: Cause categorization and visualization

## Core RCA Methodologies

### 1. The 5 Whys
Ask "why" five times to drill down to the root cause:
```
Problem: Website is down
Why? → The database is not responding
Why? → The connection pool is exhausted
Why? → Too many long-running queries
Why? → Missing index on frequently queried column
Why? → Index was dropped during migration
Root Cause: Missing rollback of failed migration
```

### 2. Fishbone (Ishikawa) Diagram
Categorize potential causes:
- **People**: Skills, training, processes
- **Process**: Procedures, policies, workflows
- **Technology**: Hardware, software, infrastructure
- **Environment**: External factors, dependencies

### 3. Timeline Analysis
Create detailed incident timeline:
1. Normal operation baseline
2. First signs of degradation
3. Escalation points
4. Recovery attempts
5. Resolution

## OpenDeRisk Integration

### Multi-Agent RCA Workflow
```python
from openderisk import SREAgent, CodeAgent, DataAgent, ReportAgent

# SRE-Agent: Analyze logs and metrics
sre_analysis = SREAgent().investigate(
    logs=collect_logs(),
    metrics=collect_metrics(),
    traces=collect_traces()
)

# Code-Agent: Identify code issues
code_analysis = CodeAgent().analyze(
    repository="app-repo",
    commit_range="last_deployment",
    error_patterns=sre_analysis.errors
)

# Data-Agent: Correlation analysis
correlation = DataAgent().correlate(
    sre_findings=sre_analysis,
    code_findings=code_analysis
)

# Generate RCA report
rca_report = ReportAgent().generate_rca(
    findings=[sre_analysis, code_analysis, correlation],
    include_evidence_chain=True
)
```

## RCA Process Steps

### 1. Incident Detection
- Alert triggered
- User reports received
- Monitoring anomaly detected

### 2. Initial Response
- Assess impact and scope
- Begin timeline documentation
- Collect initial evidence

### 3. Investigation
- Analyze logs, metrics, traces
- Review recent changes
- Identify anomalies
- Form hypotheses

### 4. Root Cause Identification
- Test hypotheses
- Trace evidence chain
- Validate findings
- Document root cause

### 5. Resolution
- Implement fix
- Verify resolution
- Document solution

### 6. Post-Incident Review
- Write RCA report
- Identify preventive measures
- Update runbooks
- Share learnings

## Related Skills

- [Risk Assessment](../risk-assessment/) - Prevent future incidents
- [Incident Response](../incident-response/) - Handle active incidents
- [Monitoring & Alerting](../monitoring-alerting/) - Early detection
- [Remediation & Recovery](../remediation-recovery/) - Fix and prevent recurrence
