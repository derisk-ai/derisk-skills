# Incident Response Playbooks

This directory contains ready-to-use incident response playbooks for common scenarios.

## Available Playbooks

### 1. Database Outage Response
**File**: `database-outage.md`
**When to Use**: Database is unresponsive or completely down
**Severity**: P0/P1
**MTTR Target**: 30 minutes

---

### 2. Application Performance Degradation
**File**: `performance-degradation.md`
**When to Use**: Slow response times, high latency
**Severity**: P1/P2
**MTTR Target**: 60 minutes

---

### 3. Security Incident Response
**File**: `security-incident.md`
**When to Use**: Suspected or confirmed security breach
**Severity**: P0/P1
**MTTR Target**: Immediate containment

---

### 4. Third-Party Service Outage
**File**: `third-party-outage.md`
**When to Use**: Critical external dependency is down
**Severity**: P1/P2
**MTTR Target**: 45 minutes (to implement fallback)

---

### 5. High Error Rate
**File**: `high-error-rate.md`
**When to Use**: Error rate exceeds threshold (> 1%)
**Severity**: P1/P2
**MTTR Target**: 45 minutes

---

## Playbook Structure

Each playbook follows this format:

### 1. Overview
- Incident type and description
- Severity level
- MTTR target
- On-call roles involved

### 2. Detection
- Alert criteria
- Monitoring sources
- Verification steps

### 3. Triage
- Severity assessment
- Impact evaluation
- Team notification

### 4. Investigation
- Data collection checklist
- Key questions to answer
- Tools and commands

### 5. Mitigation
- Immediate actions (5 min)
- Short-term fixes (30 min)
- Communication plan

### 6. Resolution
- Permanent fix steps
- Verification procedures
- Service restoration

### 7. Post-Incident
- RCA requirements
- Documentation checklist
- Follow-up actions

### 8. Automation
- n8n workflow integration
- OpenDeRisk agent usage
- Monitoring setup

## How to Use Playbooks

### During an Incident

1. **Identify** the incident type
2. **Open** the relevant playbook
3. **Follow** steps in order
4. **Document** actions taken
5. **Escalate** if needed
6. **Communicate** status

### Before an Incident

1. **Review** playbooks with team
2. **Customize** for your environment
3. **Test** procedures in staging
4. **Update** contact information
5. **Integrate** with tools
6. **Train** on-call engineers

## Customization Guide

### Add Your Environment Details

Replace placeholders with actual values:
```markdown
# Before
Contact: [DevOps Team]

# After
Contact: #devops-oncall (Slack), devops@company.com
```

### Add Your Tools
```markdown
# Check logs
# Before: View logs in [logging system]
# After: View logs in Datadog: https://app.datadoghq.com/logs
```

### Add Your Runbook Links
```markdown
# Rollback procedure: See [deployment runbook]
# After: Rollback procedure: See https://wiki.company.com/runbooks/rollback
```

## Example: Quick Reference Card

Print this for your on-call room:

```
┌──────────────────────────────────────────┐
│     INCIDENT RESPONSE QUICK GUIDE        │
├──────────────────────────────────────────┤
│ 1. Assess severity (P0-P3)               │
│ 2. Open playbook                         │
│ 3. Start war room (if P0/P1)             │
│ 4. Notify stakeholders                   │
│ 5. Follow playbook steps                 │
│ 6. Document timeline                     │
│ 7. Communicate updates                   │
│ 8. Schedule post-mortem                  │
├──────────────────────────────────────────┤
│ P0: Complete outage - Page immediately   │
│ P1: Major impact - Page within 15 min    │
│ P2: Minor impact - Alert during hours    │
│ P3: Minimal - Create ticket              │
├──────────────────────────────────────────┤
│ Playbooks: /playbooks/                   │
│ Runbooks: https://wiki/runbooks          │
│ Contacts: https://wiki/oncall            │
└──────────────────────────────────────────┘
```

## Integration with OpenDeRisk

Each playbook includes an OpenDeRisk integration section:

```python
# Automated RCA with OpenDeRisk
from openderisk import SREAgent, CodeAgent

# Let SRE-Agent investigate
analysis = SREAgent().investigate({
    "incident_id": "INC-2025-001",
    "playbook": "database-outage",
    "time_range": "last_2_hours"
})

# Get recommendations
recommendations = CodeAgent().suggest_fixes(
    analysis.findings
)
```

## Integration with n8n

Automate playbook execution:

```yaml
# n8n workflow trigger
- name: "Incident Detected"
  type: "webhook"
  
- name: "Select Playbook"
  type: "switch"
  rules:
    - database_error → database-outage.md
    - high_latency → performance-degradation.md
    
- name: "Execute Playbook Steps"
  type: "code"
  # Parse and execute playbook
```

## Creating New Playbooks

Follow this template:

```markdown
# [Incident Type] Response Playbook

## Overview
- **Type**: [Incident category]
- **Severity**: P0/P1/P2/P3
- **MTTR Target**: [X minutes]
- **Roles**: [On-call roles needed]

## Detection
[How to detect this incident]

## Triage
[ ] Verify the incident
[ ] Assess severity
[ ] Gather initial info

## Investigation
### Questions to Answer
1. [Question 1]
2. [Question 2]

### Data to Collect
- [ ] Logs
- [ ] Metrics
- [ ] Recent changes

## Mitigation
### Immediate (5 min)
1. [Action 1]
2. [Action 2]

### Short-term (30 min)
1. [Action 1]
2. [Action 2]

## Communication
- [ ] Notify [stakeholders]
- [ ] Status update every [X] minutes
- [ ] Resolution announcement

## Resolution
1. [Permanent fix step 1]
2. [Verification]

## Post-Incident
- [ ] Schedule RCA
- [ ] Update runbooks
- [ ] Improve monitoring

## Automation
[OpenDeRisk and n8n integration]
```

## Contributing

Improve these playbooks:
1. Add real-world lessons learned
2. Include specific tool commands
3. Add troubleshooting tips
4. Share successful patterns
5. Submit pull request

## Related Resources

- [Incident Response Skill](../../skills/incident-response/)
- [Root Cause Analysis Skill](../../skills/root-cause-analysis/)
- [n8n Risk Workflows](../../skills/n8n-risk-workflows/)
- [PagerDuty Incident Response](https://response.pagerduty.com/)

---

**Remember**: Practice makes perfect. Run tabletop exercises regularly!
