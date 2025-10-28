# n8n Risk Workflow Patterns

**Proven n8n workflow patterns for risk mitigation scenarios**

## Overview

This skill provides proven workflow patterns and templates for implementing risk mitigation, incident response, and SRE automation using n8n. Includes ready-to-use templates for common scenarios integrated with OpenDeRisk.

## When This Skill Activates

- "Build alert workflow in n8n"
- "Create incident response automation"
- "Automate risk mitigation"
- "n8n workflow for monitoring"
- "Alert escalation pattern"
- "Notification workflow template"

## Key Features

- **Alert Processing Workflows**: Ingestion, enrichment, routing
- **Incident Response Automation**: Detection, triage, remediation
- **Escalation Patterns**: Multi-tier escalation logic
- **Notification Flows**: Slack, PagerDuty, email, SMS
- **Integration Patterns**: OpenDeRisk, monitoring tools, ticketing systems
- **Ready-to-Use Templates**: Import and customize

## Workflow Patterns

### 1. Alert Ingestion & Enrichment
```
Webhook → Parse → Enrich → Deduplicate → Route → Notify
```

**Use Case**: Centralize alerts from multiple sources

**Key Nodes**:
- Webhook (receive alerts)
- Code (parse and enrich)
- Merge (deduplicate)
- Switch (route by severity)
- Slack/Email (notify)

### 2. Incident Response Automation
```
Alert → Classify → OpenDeRisk RCA → Create Ticket → Notify Team → Monitor
```

**Use Case**: Automated incident handling

**Key Nodes**:
- Webhook (alert trigger)
- Code (classify severity)
- HTTP Request (OpenDeRisk API)
- JIRA (create ticket)
- Slack (notify)
- Cron (monitor status)

### 3. Escalation Pattern
```
Alert → Wait → Check Status → Escalate if Unresolved → Repeat
```

**Use Case**: Multi-tier on-call escalation

**Key Nodes**:
- Webhook (alert)
- Wait (15 min)
- HTTP Request (check status)
- IF (resolved?)
- PagerDuty (escalate)
- Loop (next tier)

### 4. Scheduled Risk Assessment
```
Schedule → Collect Data → OpenDeRisk Analysis → Generate Report → Distribute
```

**Use Case**: Daily/weekly risk assessments

**Key Nodes**:
- Cron (schedule)
- HTTP Request (data collection)
- HTTP Request (OpenDeRisk)
- Code (format report)
- Email (distribute)

### 5. Self-Healing Automation
```
Monitor → Detect Issue → Attempt Fix → Verify → Alert if Failed
```

**Use Case**: Automated remediation

**Key Nodes**:
- Webhook (monitoring alert)
- Code (analyze issue)
- HTTP Request (execute fix)
- Wait (verification delay)
- HTTP Request (health check)
- IF (healthy?)
- Slack (alert if failed)

## Template Library

### Template 1: PagerDuty Alert → OpenDeRisk → Slack

**Purpose**: Process PagerDuty alerts with OpenDeRisk analysis

```yaml
workflow:
  name: "PagerDuty to OpenDeRisk Integration"
  nodes:
    - name: "PagerDuty Webhook"
      type: "webhook"
      path: "pagerduty-alerts"
      
    - name: "Extract Alert Data"
      type: "code"
      code: |
        return [{
          json: {
            incident_id: $json.incident.id,
            title: $json.incident.title,
            severity: $json.incident.urgency,
            service: $json.incident.service.name
          }
        }];
        
    - name: "Call OpenDeRisk"
      type: "httpRequest"
      url: "{{$env.OPENDERISK_URL}}/api/v1/agents/sre/investigate"
      method: "POST"
      authentication: "headerAuth"
      
    - name: "Format Slack Message"
      type: "code"
      code: |
        return [{
          json: {
            channel: "#incidents",
            text: `*Incident Analysis*\n` +
                  `ID: ${$json.incident_id}\n` +
                  `Root Cause: ${$json.analysis.root_cause}\n` +
                  `Recommendation: ${$json.analysis.recommendation}`
          }
        }];
        
    - name: "Send to Slack"
      type: "slack"
```

### Template 2: CloudWatch → Alert → Auto-Scale

**Purpose**: Auto-scale based on CloudWatch metrics

```yaml
workflow:
  name: "Auto-Scale on High CPU"
  nodes:
    - name: "CloudWatch Alarm"
      type: "webhook"
      
    - name: "Check Threshold"
      type: "if"
      conditions:
        - field: "{{$json.NewStateValue}}"
          operation: "equals"
          value: "ALARM"
          
    - name: "Scale Up ECS Service"
      type: "httpRequest"
      url: "https://ecs.amazonaws.com/"
      method: "POST"
      authentication: "aws"
      
    - name: "Log Action"
      type: "httpRequest"
      url: "{{$env.LOGGING_ENDPOINT}}"
      
    - name: "Notify Team"
      type: "slack"
      message: "Auto-scaled {{$json.service}} due to high CPU"
```

### Template 3: Multi-Channel Alert Distribution

**Purpose**: Distribute alerts via multiple channels based on severity

```yaml
workflow:
  name: "Multi-Channel Alert Router"
  nodes:
    - name: "Receive Alert"
      type: "webhook"
      
    - name: "Parse Alert"
      type: "code"
      
    - name: "Route by Severity"
      type: "switch"
      rules:
        - condition: "={{$json.severity}}" = "critical"
          output: 0  # PagerDuty
        - condition: "={{$json.severity}}" = "high"
          output: 1  # Slack
        - condition: "={{$json.severity}}" = "medium"
          output: 2  # Email
          
    - name: "PagerDuty (Critical)"
      type: "pagerduty"
      
    - name: "Slack (High)"
      type: "slack"
      
    - name: "Email (Medium)"
      type: "emailSend"
```

### Template 4: Incident Timeline Tracker

**Purpose**: Track and visualize incident timeline

```yaml
workflow:
  name: "Incident Timeline Tracker"
  nodes:
    - name: "Incident Events"
      type: "webhook"
      
    - name: "Add Timestamp"
      type: "code"
      code: |
        return [{
          json: {
            ...$json,
            timestamp: new Date().toISOString(),
            event_type: $json.type
          }
        }];
        
    - name: "Store in Database"
      type: "postgres"
      operation: "insert"
      table: "incident_timeline"
      
    - name: "Update Dashboard"
      type: "httpRequest"
      url: "{{$env.GRAFANA_API}}/annotations"
      
    - name: "Check for Resolution"
      type: "if"
      conditions:
        - field: "{{$json.event_type}}"
          operation: "equals"
          value: "resolved"
          
    - name: "Generate Timeline Report"
      type: "code"
      
    - name: "Post to Slack"
      type: "slack"
```

### Template 5: Automated Deployment Rollback

**Purpose**: Detect failed deployments and auto-rollback

```yaml
workflow:
  name: "Auto-Rollback on Failed Deployment"
  nodes:
    - name: "Deployment Completed"
      type: "webhook"
      
    - name: "Wait for Health Check"
      type: "wait"
      amount: 5
      unit: "minutes"
      
    - name: "Run Health Checks"
      type: "httpRequest"
      url: "{{$json.service_url}}/health"
      
    - name: "Check Health Status"
      type: "if"
      conditions:
        - field: "{{$json.status}}"
          operation: "notEquals"
          value: "healthy"
          
    - name: "Trigger Rollback"
      type: "httpRequest"
      url: "{{$env.CI_CD_API}}/rollback"
      method: "POST"
      
    - name: "Alert Team"
      type: "slack"
      message: "Auto-rollback triggered for {{$json.service}}"
      
    - name: "Create Incident"
      type: "httpRequest"
      url: "{{$env.OPENDERISK_URL}}/api/v1/incidents"
```

## Common Node Patterns

### Alert Deduplication
```javascript
// Code node to deduplicate alerts
const alertKey = `${$json.service}-${$json.error_type}`;
const recentAlerts = $('Webhook').all();

const isDuplicate = recentAlerts.some(alert => 
  alert.json.key === alertKey &&
  (Date.now() - new Date(alert.json.timestamp)) < 300000 // 5 min
);

if (isDuplicate) {
  return [];  // Skip duplicate
}

return [{
  json: {
    ...$json,
    key: alertKey,
    timestamp: new Date().toISOString()
  }
}];
```

### Alert Enrichment
```javascript
// Enrich alert with context
const enrichedAlert = {
  ...$json,
  environment: $json.tags.env || 'unknown',
  owner: getTeamOwner($json.service),
  runbook_url: `https://wiki.company.com/runbooks/${$json.service}`,
  dashboard_url: `https://grafana.company.com/d/${$json.service}`,
  recent_deployments: await fetchRecentDeployments($json.service)
};

return [{ json: enrichedAlert }];
```

### Progressive Retry
```javascript
// Retry with exponential backoff
const maxRetries = 3;
const retryCount = $json.retryCount || 0;

if (retryCount >= maxRetries) {
  // Give up and escalate
  return [{ json: { ...$json, escalate: true } }];
}

// Wait before retry: 2^retry seconds
const waitTime = Math.pow(2, retryCount);
await $helpers.wait(waitTime * 1000);

// Retry the operation
try {
  const result = await $helpers.httpRequest({ /* config */ });
  return [{ json: result }];
} catch (error) {
  return [{ json: { ...$json, retryCount: retryCount + 1 } }];
}
```

## Best Practices

### Workflow Design
✅ Use descriptive node names
✅ Add error handling to every HTTP request
✅ Implement retry logic for external calls
✅ Use environment variables for configuration
✅ Log important events
✅ Test workflows thoroughly

### Performance
✅ Use batch operations when possible
✅ Implement rate limiting
✅ Cache frequently accessed data
✅ Use async operations
✅ Monitor workflow execution time

### Security
✅ Never hardcode credentials
✅ Use webhook authentication
✅ Validate input data
✅ Sanitize user inputs
✅ Encrypt sensitive data
✅ Audit workflow access

## Related Skills

- [n8n-OpenDeRisk Integration](../n8n-openderisk-integration/) - Integration guide
- [Incident Response](../incident-response/) - Response procedures
- [Monitoring & Alerting](../monitoring-alerting/) - Alert design
- [Remediation & Recovery](../remediation-recovery/) - Automation patterns
