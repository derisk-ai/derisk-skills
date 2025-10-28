# n8n Workflow Examples

This directory contains ready-to-use n8n workflow templates for risk mitigation and incident response.

## Available Workflows

### 1. Alert Processing Pipeline
**File**: `alert-processing-pipeline.json`
**Purpose**: Centralize and process alerts from multiple monitoring sources
**Features**:
- Multi-source alert ingestion
- Deduplication and enrichment
- Severity-based routing
- Slack and PagerDuty integration

**Usage**:
1. Import workflow into n8n
2. Configure webhook URLs for your monitoring tools
3. Set Slack and PagerDuty credentials
4. Test with sample alert

### 2. Automated Incident Response
**File**: `automated-incident-response.json`
**Purpose**: Automated incident detection, analysis, and response
**Features**:
- OpenDeRisk integration for RCA
- JIRA ticket creation
- Team notification
- Status tracking

**Usage**:
1. Import workflow
2. Configure OpenDeRisk API credentials
3. Set up JIRA integration
4. Define on-call schedule

### 3. Daily Risk Assessment
**File**: `daily-risk-assessment.json`
**Purpose**: Scheduled risk assessment using OpenDeRisk
**Features**:
- Scheduled execution (daily at 9 AM)
- OpenDeRisk risk analysis
- Report generation
- Email distribution

**Usage**:
1. Import workflow
2. Configure OpenDeRisk API
3. Set email recipients
4. Customize schedule if needed

### 4. Deployment Health Check
**File**: `deployment-health-check.json`
**Purpose**: Monitor deployments and auto-rollback if unhealthy
**Features**:
- Post-deployment health checks
- Automatic rollback on failure
- Team alerts
- Incident creation

**Usage**:
1. Import workflow
2. Configure CI/CD webhook
3. Define health check endpoints
4. Set rollback triggers

### 5. Multi-Tier Escalation
**File**: `multi-tier-escalation.json`
**Purpose**: Escalate unresolved incidents through on-call tiers
**Features**:
- Configurable wait periods
- Status checking
- Progressive escalation
- PagerDuty integration

**Usage**:
1. Import workflow
2. Define escalation tiers
3. Set wait periods
4. Configure PagerDuty

## How to Use These Workflows

### Step 1: Import into n8n

1. Open n8n web interface
2. Click "+" to create new workflow
3. Click the three dots menu → "Import from File"
4. Select the `.json` file
5. Click "Import"

### Step 2: Configure Credentials

Each workflow requires specific credentials:
- **OpenDeRisk API**: API key or OAuth token
- **Slack**: OAuth or webhook URL
- **PagerDuty**: API token
- **JIRA**: Username and API token
- **Email**: SMTP settings

Set these in n8n Settings → Credentials.

### Step 3: Update Environment Variables

Configure in n8n Settings → Environment Variables:
```bash
OPENDERISK_URL=https://your-openderisk-instance.com
OPENDERISK_API_KEY=your-api-key
SLACK_CHANNEL=#incidents
JIRA_PROJECT=OPS
```

### Step 4: Test the Workflow

1. Click "Execute Workflow"
2. Send a test event
3. Verify each node executes correctly
4. Check outputs in connected systems

### Step 5: Activate

1. Click the "Active" toggle in the top-right
2. Workflow will now respond to triggers

## Customization Tips

### Modify Alert Routing
Edit the Switch node to add custom routing logic:
```javascript
// Route based on service name
if ($json.service.includes('payment')) {
  return 0;  // Critical path
} else if ($json.service.includes('api')) {
  return 1;  // High priority path
} else {
  return 2;  // Normal path
}
```

### Adjust Wait Times
Change Wait node duration:
```json
{
  "amount": 15,
  "unit": "minutes"
}
```

### Customize Notifications
Modify Slack message format:
```javascript
return [{
  json: {
    channel: "#incidents",
    text: `*${$json.severity}* alert for ${$json.service}`,
    blocks: [
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: `*Service*: ${$json.service}\n*Error*: ${$json.message}`
        }
      }
    ]
  }
}];
```

## Workflow Templates Coming Soon

- Database Backup Verification
- Certificate Expiration Monitoring
- Cost Anomaly Detection
- Security Scan Automation
- Capacity Planning Alerts

## Contributing

Have a useful workflow? Submit a PR!

1. Export your workflow as JSON
2. Add to this directory
3. Update this README
4. Submit pull request

## Support

- **Issues**: Report problems with workflows
- **Questions**: Ask in Discussions
- **Improvements**: Suggest enhancements

---

For more information, see:
- [n8n-OpenDeRisk Integration Skill](../../skills/n8n-openderisk-integration/)
- [n8n Risk Workflow Patterns Skill](../../skills/n8n-risk-workflows/)
