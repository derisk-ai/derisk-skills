# n8n-OpenDeRisk Integration

**Connect n8n workflows with OpenDeRisk agents and services**

## Overview

This skill provides comprehensive guidance on integrating n8n workflow automation with OpenDeRisk's AI-powered risk intelligence system. Learn how to build workflows that leverage OpenDeRisk's multi-agent architecture for automated risk mitigation.

## When This Skill Activates

- "Integrate n8n with OpenDeRisk"
- "Call OpenDeRisk from n8n"
- "Build risk mitigation workflow"
- "Automate RCA with n8n"
- "Connect to OpenDeRisk API"
- "Orchestrate OpenDeRisk agents"

## Key Features

- **API Integration**: Connect to OpenDeRisk REST API
- **Agent Orchestration**: Trigger and coordinate multiple agents
- **MCP Service Integration**: Use OpenDeRisk MCP services
- **Data Flow Patterns**: Pass data between n8n and OpenDeRisk
- **Webhook Integration**: Receive alerts and events
- **Workflow Templates**: Ready-to-use integration patterns

## Integration Patterns

### 1. Alert Ingestion
```
External Alert → n8n → OpenDeRisk SRE-Agent → Analysis → Response
```

### 2. Automated RCA
```
Incident → n8n → OpenDeRisk Multi-Agent → RCA Report → Notification
```

### 3. Risk Assessment
```
Schedule → n8n → OpenDeRisk Risk Agent → Report → Store
```

### 4. Remediation Workflow
```
Issue Detected → n8n → OpenDeRisk → Remediation Plan → Execute → Verify
```

## OpenDeRisk API Endpoints

```yaml
# Example OpenDeRisk API structure
base_url: https://openderisk.example.com/api/v1

endpoints:
  # Agent orchestration
  - POST /agents/sre/investigate
  - POST /agents/code/analyze
  - POST /agents/data/correlate
  
  # Risk assessment
  - POST /risk/assess
  - GET /risk/report/{id}
  
  # RCA
  - POST /rca/analyze
  - GET /rca/report/{id}
  
  # Incidents
  - POST /incidents
  - GET /incidents/{id}
  - PATCH /incidents/{id}
```

## n8n Node Configuration

### HTTP Request Node (OpenDeRisk API)
```json
{
  "method": "POST",
  "url": "={{$env.OPENDERISK_URL}}/api/v1/agents/sre/investigate",
  "authentication": "headerAuth",
  "sendHeaders": true,
  "headerParameters": {
    "parameters": [
      {
        "name": "Authorization",
        "value": "=Bearer {{$env.OPENDERISK_API_KEY}}"
      }
    ]
  },
  "sendBody": true,
  "bodyParameters": {
    "parameters": [
      {
        "name": "incident_id",
        "value": "={{$json.incident_id}}"
      },
      {
        "name": "time_range",
        "value": "={{$json.time_range}}"
      }
    ]
  }
}
```

### Webhook Node (Receive OpenDeRisk Alerts)
```json
{
  "path": "openderisk-alerts",
  "httpMethod": "POST",
  "responseMode": "onReceived",
  "responseData": "allEntries"
}
```

## Example Workflows

### 1. Automated Incident Response
```yaml
name: "Auto Incident Response with OpenDeRisk"
nodes:
  - name: "Receive Alert"
    type: "n8n-nodes-base.webhook"
    
  - name: "Parse Alert"
    type: "n8n-nodes-base.set"
    
  - name: "Call OpenDeRisk SRE-Agent"
    type: "n8n-nodes-base.httpRequest"
    parameters:
      url: "{{$env.OPENDERISK_URL}}/api/v1/agents/sre/investigate"
      
  - name: "Generate RCA Report"
    type: "n8n-nodes-base.httpRequest"
    parameters:
      url: "{{$env.OPENDERISK_URL}}/api/v1/rca/analyze"
      
  - name: "Send Slack Notification"
    type: "n8n-nodes-base.slack"
    
  - name: "Create JIRA Ticket"
    type: "n8n-nodes-base.jira"
```

### 2. Scheduled Risk Assessment
```yaml
name: "Daily Risk Assessment"
nodes:
  - name: "Schedule Trigger"
    type: "n8n-nodes-base.cron"
    parameters:
      triggerTimes:
        - hour: 9
          minute: 0
          
  - name: "Collect System Info"
    type: "n8n-nodes-base.httpRequest"
    
  - name: "Run Risk Assessment"
    type: "n8n-nodes-base.httpRequest"
    parameters:
      url: "{{$env.OPENDERISK_URL}}/api/v1/risk/assess"
      
  - name: "Generate Report"
    type: "n8n-nodes-base.set"
    
  - name: "Email Report"
    type: "n8n-nodes-base.emailSend"
```

## Authentication Methods

### 1. API Key Authentication
```javascript
// In n8n HTTP Request node
{
  "authentication": "headerAuth",
  "headerAuth": {
    "name": "Authorization",
    "value": "=Bearer {{$env.OPENDERISK_API_KEY}}"
  }
}
```

### 2. OAuth2 (if supported)
```javascript
{
  "authentication": "oAuth2",
  "oAuth2": {
    "grantType": "clientCredentials",
    "accessTokenUrl": "{{$env.OPENDERISK_URL}}/oauth/token",
    "clientId": "={{$env.OPENDERISK_CLIENT_ID}}",
    "clientSecret": "={{$env.OPENDERISK_CLIENT_SECRET}}"
  }
}
```

## Data Mapping

### Alert → OpenDeRisk Format
```javascript
// n8n Code node
const openderiskPayload = {
  incident_id: $json.alert_id,
  timestamp: $json.timestamp,
  severity: $json.severity,
  service: $json.service_name,
  description: $json.message,
  metadata: {
    environment: $json.environment,
    region: $json.region,
    logs: $json.log_urls
  }
};

return [{ json: openderiskPayload }];
```

### OpenDeRisk Response → Notification
```javascript
// Format RCA report for Slack
const slackMessage = {
  text: "RCA Report Available",
  blocks: [
    {
      type: "section",
      text: {
        type: "mrkdwn",
        text: `*Incident:* ${$json.incident_id}\n*Root Cause:* ${$json.root_cause}\n*Impact:* ${$json.impact}`
      }
    },
    {
      type: "actions",
      elements: [
        {
          type: "button",
          text: { type: "plain_text", text: "View Full Report" },
          url: $json.report_url
        }
      ]
    }
  ]
};

return [{ json: slackMessage }];
```

## Error Handling

```javascript
// n8n Code node for error handling
try {
  const response = await $helpers.httpRequest({
    method: 'POST',
    url: `${$env.OPENDERISK_URL}/api/v1/agents/sre/investigate`,
    headers: {
      'Authorization': `Bearer ${$env.OPENDERISK_API_KEY}`
    },
    body: $json
  });
  
  return [{ json: response }];
} catch (error) {
  // Log error and send notification
  console.error('OpenDeRisk API Error:', error);
  
  // Send to error handling workflow
  return [{
    json: {
      error: true,
      message: error.message,
      incident_id: $json.incident_id
    }
  }];
}
```

## Best Practices

✅ **DO:**
- Store credentials in environment variables
- Implement retry logic for API calls
- Use webhook authentication
- Validate OpenDeRisk responses
- Log all integration points
- Test workflows in staging first

❌ **DON'T:**
- Hardcode API keys in workflows
- Skip error handling
- Send sensitive data without encryption
- Ignore rate limits
- Bypass authentication
- Deploy untested workflows

## Related Skills

- [n8n Risk Workflow Patterns](../n8n-risk-workflows/) - Workflow templates
- [Incident Response](../incident-response/) - Response automation
- [Monitoring & Alerting](../monitoring-alerting/) - Alert integration
- [Root Cause Analysis](../root-cause-analysis/) - RCA automation
