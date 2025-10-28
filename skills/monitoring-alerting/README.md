# Monitoring & Alerting

**Intelligent monitoring, alerting, and anomaly detection**

## Overview

This skill provides guidance on implementing effective monitoring and alerting strategies for distributed systems. Covers metric selection, alert design, anomaly detection, and integration with OpenDeRisk for AI-powered insights.

## When This Skill Activates

- "Set up monitoring for my service"
- "Create alerts for anomalies"
- "What metrics should I monitor?"
- "Reduce alert fatigue"
- "Detect performance issues"
- "Configure observability"

## Key Features

- **Metric Selection**: Choosing the right metrics (RED, USE, Four Golden Signals)
- **Alert Design**: Writing effective alerts that reduce noise
- **Anomaly Detection**: ML-based detection patterns
- **Dashboard Creation**: Visualizing system health
- **SLO/SLI Definition**: Service level objectives and indicators
- **OpenDeRisk Integration**: AI-powered anomaly detection
- **Alert Fatigue Prevention**: Reducing false positives

## Core Metrics

### RED Method (Request-driven)
- **Rate**: Requests per second
- **Errors**: Error rate
- **Duration**: Response time distribution

### USE Method (Resource-driven)
- **Utilization**: % time resource busy
- **Saturation**: Queue depth
- **Errors**: Error count

### Four Golden Signals
- **Latency**: Request duration
- **Traffic**: Request rate
- **Errors**: Failed requests
- **Saturation**: Resource fullness

## Alerting Best Practices

- Alert on symptoms, not causes
- Include actionable information
- Set appropriate thresholds
- Use percentiles (P95, P99) not averages
- Implement alert grouping and deduplication
- Define clear severity levels

## Related Skills

- [Risk Assessment](../risk-assessment/) - Identify monitoring gaps
- [Incident Response](../incident-response/) - Handle alerts
- [Root Cause Analysis](../root-cause-analysis/) - Investigate alerts
- [n8n-OpenDeRisk Integration](../n8n-openderisk-integration/) - Automated workflows
