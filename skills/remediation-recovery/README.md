# Remediation & Recovery

**Automated remediation and system recovery workflows**

## Overview

This skill provides guidance on implementing automated remediation strategies, recovery procedures, and preventive measures for production systems. Covers rollback strategies, self-healing systems, and integration with OpenDeRisk and n8n.

## When This Skill Activates

- "Automate incident remediation"
- "Create rollback procedure"
- "Implement self-healing"
- "Build recovery workflow"
- "Prevent incident recurrence"
- "Deploy automated fixes"

## Key Features

- **Automated Remediation**: Self-healing systems and auto-remediation
- **Rollback Strategies**: Safe deployment rollback procedures
- **Recovery Procedures**: System and data recovery workflows
- **Chaos Engineering**: Testing recovery mechanisms
- **Preventive Measures**: Implementing fixes to prevent recurrence
- **n8n Automation**: Automated remediation workflows
- **OpenDeRisk Integration**: AI-powered remediation suggestions

## Remediation Strategies

### 1. Automated Rollback
- Detect deployment issues
- Automatic rollback to last known good version
- Health check validation

### 2. Auto-Scaling
- Detect resource saturation
- Automatically scale resources
- Monitor and adjust

### 3. Circuit Breakers
- Detect failing dependencies
- Open circuit to prevent cascading failures
- Automatic recovery attempts

### 4. Self-Healing
- Detect unhealthy instances
- Automatically restart or replace
- Verify recovery

## Recovery Types

- **Service Recovery**: Restart services, clear caches
- **Data Recovery**: Restore from backups, replay events
- **Infrastructure Recovery**: Rebuild resources, failover
- **Configuration Recovery**: Rollback configs, restore settings

## Best Practices

- Test recovery procedures regularly
- Automate where possible
- Document manual procedures
- Implement graceful degradation
- Monitor recovery effectiveness
- Learn from each incident

## Related Skills

- [Incident Response](../incident-response/) - Initial handling
- [Root Cause Analysis](../root-cause-analysis/) - Understanding failures
- [Monitoring & Alerting](../monitoring-alerting/) - Detection
- [n8n Risk Workflows](../n8n-risk-workflows/) - Automation
