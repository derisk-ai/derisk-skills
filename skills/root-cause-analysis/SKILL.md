# Root Cause Analysis (RCA) - Core Skill

## Table of Contents
1. [RCA Fundamentals](#rca-fundamentals)
2. [Investigation Techniques](#investigation-techniques)
3. [Evidence Collection](#evidence-collection)
4. [Analysis Methods](#analysis-methods)
5. [OpenDeRisk Multi-Agent RCA](#openderisk-multi-agent-rca)
6. [RCA Report Writing](#rca-report-writing)

---

## RCA Fundamentals

### Key Principles

1. **Focus on Systems, Not People**: Blame-free culture
2. **Find Actual Causes, Not Symptoms**: Dig deeper
3. **Document Everything**: Evidence chain is critical
4. **Consider Multiple Causes**: Complex systems have complex failures
5. **Prevent Recurrence**: Actions must prevent future incidents

### RCA vs Troubleshooting

| RCA | Troubleshooting |
|-----|-----------------|
| Finds underlying cause | Fixes immediate problem |
| Prevents recurrence | Restores service |
| Long-term focus | Short-term focus |
| Systematic approach | Quick resolution |
| Documentation heavy | Action heavy |

---

## Investigation Techniques

### 1. The 5 Whys Method

**Example: Database Outage**
```markdown
Problem: Database is down

Why? → Database process crashed
  Why? → Out of memory error
    Why? → Memory leak in connection pooling
      Why? → Connections not being released
        Why? → Missing try-finally blocks in code
          Root Cause: Improper resource management in recent deployment
```

**Best Practices:**
- Start with a precise problem statement
- Ask "why" for each answer
- Stop when you reach an actionable root cause
- Document the full chain
- Consider parallel causes

### 2. Fishbone (Ishikawa) Diagram

```
                        Effect: Service Outage
                               |
        People                 |                Technology
        - On-call training     |                - Server capacity
        - Communication        |                - Database version
                              /|\               - Network config
        -------------------  / | \  -------------------
                            /  |  \
        Process            /   |   \          Environment
        - Deployment      /    |    \         - Cloud provider
        - Monitoring     /     |     \        - External deps
        - Alerting      /      |      \       - Traffic spike
```

**Categories (4 M's + E):**
- **Man**: People, skills, training
- **Method**: Processes, procedures
- **Machine**: Technology, tools, infrastructure
- **Materials**: Data, dependencies, resources
- **Environment**: External factors

### 3. Timeline Analysis

**Timeline Template:**
```markdown
# Incident Timeline - Service Outage 2025-01-15

## Pre-Incident (Normal State)
- 2025-01-15 12:00 - All services healthy
- 2025-01-15 12:30 - Routine deployment begins

## Incident Detection
- 2025-01-15 13:15 - First error alerts triggered
- 2025-01-15 13:17 - Customer complaints received
- 2025-01-15 13:18 - On-call engineer paged

## Investigation
- 2025-01-15 13:20 - Logs show database connection errors
- 2025-01-15 13:25 - Recent deployment identified as suspect
- 2025-01-15 13:30 - Code review reveals connection leak

## Mitigation Attempts
- 2025-01-15 13:35 - Attempted service restart (failed)
- 2025-01-15 13:40 - Rollback initiated
- 2025-01-15 13:45 - Rollback completed

## Resolution
- 2025-01-15 13:50 - Service restored
- 2025-01-15 14:00 - Full monitoring confirms stability

## Total Incident Duration: 35 minutes
## Customer Impact: 15 minutes of degraded service
```

### 4. Fault Tree Analysis

**Example: API Response Time Degradation**
```
                    Slow API Response
                           |
              +------------+------------+
              |                         |
         High Latency              Timeout Errors
              |                         |
        +-----+-----+             +-----+-----+
        |           |             |           |
   DB Queries   Network      Connection   Query
   Slow         Issues       Pool Full    Timeout
```

---

## Evidence Collection

### Log Analysis

**Key Log Sources:**
1. **Application Logs**: Error messages, stack traces
2. **System Logs**: OS-level events
3. **Access Logs**: Request patterns, user actions
4. **Audit Logs**: Configuration changes
5. **Container Logs**: Docker/Kubernetes events

**Log Correlation Example:**
```bash
# Correlate logs by request ID
grep "request-id-12345" application.log system.log access.log

# Timeline view
journalctl --since "2025-01-15 13:00" --until "2025-01-15 14:00"

# Error pattern detection
grep -E "ERROR|FATAL|Exception" app.log | sort | uniq -c
```

### Metrics Analysis

**Key Metrics:**
- **Request Rate**: Sudden spikes or drops
- **Error Rate**: Percentage of failed requests
- **Response Time**: P50, P95, P99 latencies
- **Resource Utilization**: CPU, memory, disk I/O
- **Database Metrics**: Query time, connection count

**Using OpenDeRisk Data-Agent:**
```python
from openderisk import DataAgent

# Collect and analyze metrics
metrics = DataAgent().collect_metrics(
    sources=["prometheus", "cloudwatch"],
    time_range="incident_window",
    metrics=[
        "http_request_duration_seconds",
        "error_rate",
        "cpu_usage_percent",
        "db_connection_count"
    ]
)

# Detect anomalies
anomalies = DataAgent().detect_anomalies(
    metrics=metrics,
    baseline_window="1_week",
    sensitivity="high"
)
```

### Distributed Tracing

**Using Traces for RCA:**
```python
# OpenDeRisk trace analysis
from openderisk import SREAgent

# Get trace for failed request
trace = SREAgent().get_trace(
    trace_id="abc-123",
    service="payment-service"
)

# Identify bottlenecks
bottlenecks = SREAgent().analyze_trace(
    trace=trace,
    threshold_ms=1000
)

# Output:
# Span: database_query - Duration: 5200ms (SLOW)
# Span: external_api_call - Duration: 3800ms (SLOW)
```

### Code Analysis

**Using Code-Agent:**
```python
from openderisk import CodeAgent

# Identify problematic code
code_issues = CodeAgent().analyze(
    repository="app-repo",
    commit_range="v1.2.3...v1.2.4",  # Recent deployment
    focus_areas=[
        "database_connections",
        "memory_management",
        "error_handling"
    ]
)

# Find specific patterns
patterns = CodeAgent().find_patterns(
    code_issues,
    patterns=[
        "unclosed_connections",
        "infinite_loops",
        "race_conditions"
    ]
)
```

---

## Analysis Methods

### Correlation Analysis

**Correlate Multiple Data Sources:**
```python
from openderisk import DataAgent

# Correlate logs, metrics, and traces
correlation = DataAgent().correlate(
    data_sources={
        "logs": error_logs,
        "metrics": performance_metrics,
        "traces": distributed_traces,
        "events": deployment_events
    },
    time_window="incident_window"
)

# Identify patterns
patterns = correlation.find_patterns([
    "deployment_preceded_errors",
    "metric_spike_with_errors",
    "trace_shows_bottleneck"
])
```

### Change Analysis

**Identify Recent Changes:**
```markdown
# Change Timeline

## Code Deployments
- 2025-01-15 12:30 - payment-service v1.2.4
  - Changed: Connection pooling logic
  - Author: developer@company.com
  - PR: #1234

## Configuration Changes
- 2025-01-15 11:00 - Increased database max_connections
  - Changed by: sre@company.com
  - Ticket: OPS-567

## Infrastructure Changes
- 2025-01-14 16:00 - Database instance upgraded
  - Type: db.t3.medium → db.t3.large
  - Changed by: Auto-scaling policy

## Dependency Changes
- 2025-01-14 10:00 - Updated postgres driver
  - Version: 8.7.1 → 8.8.0
  - Automatic dependency update
```

### Hypothesis Testing

**Scientific Approach:**
```markdown
# Hypothesis: Connection leak caused database exhaustion

## Test 1: Verify connection leak
Method: Monitor connection count during load test
Expected: Connections increase without being released
Result: ✅ CONFIRMED - Connections plateau at max

## Test 2: Identify leak location
Method: Code analysis of recent changes
Expected: Missing connection.close() in new code
Result: ✅ CONFIRMED - Missing try-finally in PR #1234

## Test 3: Reproduce in staging
Method: Deploy suspect code to staging, run load test
Expected: Same connection exhaustion occurs
Result: ✅ CONFIRMED - Reproduced in 15 minutes

## Conclusion: Root cause identified
```

---

## OpenDeRisk Multi-Agent RCA

### Agent Collaboration Workflow

```python
from openderisk import (
    SREAgent,
    CodeAgent,
    DataAgent,
    ReportAgent,
    VisAgent
)

# 1. SRE-Agent: Initial investigation
sre_agent = SREAgent()
sre_findings = sre_agent.investigate({
    "incident_id": "INC-2025-0115-001",
    "time_range": "2025-01-15 13:00 to 14:00",
    "affected_services": ["payment-service", "user-service"],
    "symptoms": ["high error rate", "slow response time"]
})

# SRE-Agent Output:
# - Error spike at 13:15
# - Database connection errors
# - Recent deployment at 12:30
# - Hypothesis: Code change introduced issue

# 2. Code-Agent: Analyze recent changes
code_agent = CodeAgent()
code_findings = code_agent.deep_dive({
    "repository": "payment-service",
    "commit_range": "v1.2.3...v1.2.4",
    "focus": sre_findings.suspect_areas,
    "analysis_type": "connection_management"
})

# Code-Agent Output:
# - PR #1234 modified connection pooling
# - Missing try-finally blocks
# - Connections not released on exception
# - Root cause identified in DatabaseService.java:142

# 3. Data-Agent: Validate hypothesis
data_agent = DataAgent()
validation = data_agent.validate_hypothesis({
    "hypothesis": "Connection leak from PR #1234",
    "evidence": [sre_findings, code_findings],
    "metrics": ["db_connection_count", "error_rate"],
    "correlation_window": "incident_window"
})

# Data-Agent Output:
# - Connection count matches deployment timeline
# - Error rate correlates with connection exhaustion
# - Pattern confirmed: leak → exhaustion → errors
# - Confidence: 95%

# 4. Vis-Agent: Visualize evidence chain
vis_agent = VisAgent()
evidence_chain = vis_agent.create_evidence_chain({
    "findings": [sre_findings, code_findings, validation],
    "visualization_type": "timeline_with_annotations"
})

# 5. Report-Agent: Generate RCA report
report_agent = ReportAgent()
rca_report = report_agent.generate({
    "template": "rca_report",
    "findings": [sre_findings, code_findings, validation],
    "evidence_chain": evidence_chain,
    "include_recommendations": True
})

print(rca_report)
```

### Automated Evidence Chain

**OpenDeRisk Evidence Visualization:**
```
Timeline: 2025-01-15

12:30 ━━┓
         ┃ Deployment: payment-service v1.2.4
         ┃ PR #1234: Modified connection pooling
         ┃
13:15    ┃━━━┓ Evidence: Error spike detected
         ┃   ┃ Metric: error_rate 0.1% → 15%
         ┃   ┃
         ┃   ┃━━━┓ Evidence: Database errors
         ┃   ┃   ┃ Log: "Too many connections"
         ┃   ┃   ┃
         ┃   ┃   ┃━━━┓ Evidence: Connection leak
         ┃   ┃   ┃   ┃ Code: Missing connection.close()
         ┃   ┃   ┃   ┃
         ┃   ┃   ┃   ┗━━━ ROOT CAUSE IDENTIFIED
         ┃   ┃   ┃
13:40    ┃   ┃   ┗━━━┓ Action: Rollback to v1.2.3
         ┃   ┃       ┃
13:50    ┃   ┗━━━━━━━┛ Resolution: Service restored
         ┃
         ┗━━━━━━━━━━━━━ Total Incident: 35 minutes
```

---

## RCA Report Writing

### Report Structure

```markdown
# Root Cause Analysis Report

## Incident Summary
- **Incident ID**: INC-2025-0115-001
- **Date**: 2025-01-15
- **Duration**: 35 minutes (13:15 - 13:50 UTC)
- **Impact**: 15 minutes degraded service, ~500 failed transactions
- **Severity**: P1 (High)

## Executive Summary
Payment service experienced high error rates due to database connection
exhaustion caused by a connection leak introduced in v1.2.4 deployment.

## Timeline
[Detailed timeline as shown above]

## Root Cause
Missing connection.close() in exception handling path introduced in PR #1234,
leading to connection leak and eventual database connection pool exhaustion.

## Contributing Factors
1. Insufficient code review (missing try-finally check)
2. No load testing in staging environment
3. Missing monitoring alert for connection pool usage

## Evidence
### 1. Error Logs
[Log excerpts showing connection errors]

### 2. Code Diff
[Code showing missing try-finally]

### 3. Metrics
[Graphs showing connection count and error rate]

### 4. Traces
[Distributed trace showing database timeouts]

## Resolution
Rolled back to v1.2.3 at 13:40, service restored by 13:50.

## Permanent Fix
- [ ] Fix connection leak in code
- [ ] Add comprehensive tests
- [ ] Deploy with monitoring

## Preventive Measures
1. **Immediate**:
   - Add pre-deployment checklist for connection management
   - Enable connection pool monitoring alerts

2. **Short-term** (1 week):
   - Implement automated load testing in CI/CD
   - Add static code analysis for resource leaks

3. **Long-term** (1 month):
   - Enhance code review guidelines
   - Implement chaos engineering for connection failures

## Lessons Learned
1. Resource management must be validated in all code paths
2. Load testing is critical before production deployment
3. Monitoring should include resource pool metrics

## Follow-up Actions
- [ ] JIRA-123: Implement connection leak fix (Owner: Dev Team, Due: 2025-01-20)
- [ ] JIRA-124: Add load testing to CI/CD (Owner: Platform Team, Due: 2025-01-25)
- [ ] JIRA-125: Update code review checklist (Owner: Eng Manager, Due: 2025-01-18)

## Report Metadata
- **Author**: SRE Team
- **Reviewed By**: Engineering Manager, CTO
- **Date**: 2025-01-16
- **Next Review**: 2025-02-15 (30 days)
```

### Best Practices for RCA Reports

✅ **DO:**
- Be factual and objective
- Include evidence for all claims
- Focus on systems, not people
- Provide actionable recommendations
- Set deadlines for follow-up actions
- Share learnings with the team

❌ **DON'T:**
- Blame individuals
- Make assumptions without evidence
- Skip the evidence chain
- Leave actions unassigned
- Write and forget (track follow-up)

---

## Quick Reference

### RCA Checklist
- [ ] Define the problem clearly
- [ ] Establish incident timeline
- [ ] Collect all evidence (logs, metrics, traces, code)
- [ ] Apply RCA methods (5 Whys, Fishbone, etc.)
- [ ] Identify root cause(s)
- [ ] Validate hypothesis with data
- [ ] Document findings
- [ ] Create action items
- [ ] Share learnings
- [ ] Track preventive measures

### Common Pitfalls
1. Stopping at symptoms instead of root causes
2. Blaming people instead of systems
3. Not collecting sufficient evidence
4. Skipping the validation step
5. Poor documentation
6. No follow-up on action items

### Integration Points
- [Risk Assessment](../risk-assessment/): Identify systemic risks
- [Incident Response](../incident-response/): Initial handling
- [Monitoring & Alerting](../monitoring-alerting/): Detection
- [Remediation & Recovery](../remediation-recovery/): Fix implementation
