# Risk Assessment & Analysis - Core Skill

## Table of Contents
1. [Risk Assessment Framework](#risk-assessment-framework)
2. [Threat Modeling Techniques](#threat-modeling-techniques)
3. [Risk Scoring and Prioritization](#risk-scoring-and-prioritization)
4. [Attack Surface Analysis](#attack-surface-analysis)
5. [Vulnerability Assessment](#vulnerability-assessment)
6. [Risk Mitigation Strategies](#risk-mitigation-strategies)

---

## Risk Assessment Framework

### Step 1: Define Scope and Context

**Questions to Ask:**
- What systems, applications, or services are in scope?
- What are the business-critical functions?
- What are the regulatory/compliance requirements?
- Who are the stakeholders?
- What are the acceptable risk thresholds?

**Documentation Template:**
```markdown
# Risk Assessment Scope

## Systems in Scope
- System Name: [Name]
- Description: [What it does]
- Business Criticality: [High/Medium/Low]
- Data Classification: [Public/Internal/Confidential/Secret]
- Compliance Requirements: [GDPR, HIPAA, PCI-DSS, etc.]

## Assessment Period
- Start Date: [Date]
- End Date: [Date]
- Next Review: [Date]
```

### Step 2: Asset Identification

**Asset Categories:**
1. **Data Assets**: Databases, file stores, data lakes, backups
2. **Application Assets**: Web apps, APIs, microservices, mobile apps
3. **Infrastructure Assets**: Servers, networks, cloud resources
4. **Human Assets**: Administrators, developers, support staff
5. **External Dependencies**: Third-party services, vendors, partners

**Asset Inventory Template:**
```yaml
asset:
  id: "asset-001"
  name: "Customer Database"
  type: "Data"
  owner: "Data Team"
  classification: "Confidential"
  location: "AWS RDS - us-east-1"
  dependencies:
    - "User Service API"
    - "Analytics Service"
  access_controls:
    - "IAM Roles"
    - "VPC Security Groups"
    - "Database Credentials"
```

### Step 3: Threat Identification

**Common Threat Sources:**
- **External Attackers**: Hackers, cybercriminals, nation-states
- **Internal Threats**: Malicious insiders, negligent employees
- **Natural Disasters**: Floods, earthquakes, fires
- **Technical Failures**: Hardware failure, software bugs, misconfigurations
- **Supply Chain**: Compromised dependencies, vendor breaches

**Threat Catalog:**
```markdown
| Threat ID | Threat Name | Source | Target Asset | STRIDE Category |
|-----------|-------------|--------|--------------|-----------------|
| T-001 | SQL Injection | External | Customer DB | Tampering |
| T-002 | DDoS Attack | External | Web App | Denial of Service |
| T-003 | Credential Theft | External/Internal | Admin Accounts | Elevation of Privilege |
| T-004 | Data Exfiltration | Internal | Customer DB | Information Disclosure |
```

---

## Threat Modeling Techniques

### STRIDE Analysis

**For Each Component, Ask:**

1. **Spoofing**: Can an attacker impersonate a user/service?
   - Authentication mechanisms in place?
   - Token validation?
   - Multi-factor authentication?

2. **Tampering**: Can data be modified in transit or at rest?
   - Data integrity checks?
   - Encryption?
   - Audit logging?

3. **Repudiation**: Can actions be denied?
   - Non-repudiation mechanisms?
   - Audit trails?
   - Digital signatures?

4. **Information Disclosure**: Can sensitive data be exposed?
   - Access controls?
   - Encryption at rest and in transit?
   - Data masking?

5. **Denial of Service**: Can the service be made unavailable?
   - Rate limiting?
   - Resource quotas?
   - DDoS protection?

6. **Elevation of Privilege**: Can unauthorized access be gained?
   - Least privilege principle?
   - Role-based access control?
   - Input validation?

**STRIDE Threat Model Example:**
```markdown
## Component: User Authentication API

### Spoofing Threats
- **T-AUTH-001**: Attacker uses stolen JWT token
  - Likelihood: Medium
  - Impact: High
  - Mitigation: Short-lived tokens, token rotation, refresh token mechanism

### Tampering Threats
- **T-AUTH-002**: Session hijacking via XSS
  - Likelihood: Medium
  - Impact: High
  - Mitigation: HttpOnly cookies, CSP headers, input sanitization

### Information Disclosure Threats
- **T-AUTH-003**: Password exposure in logs
  - Likelihood: Low
  - Impact: Critical
  - Mitigation: Sanitize logs, never log credentials, use structured logging
```

### Data Flow Diagrams (DFD)

**DFD Elements:**
- **External Entity**: Users, external systems (rectangle)
- **Process**: Application logic, services (circle)
- **Data Store**: Databases, files (parallel lines)
- **Data Flow**: Information movement (arrow)

**Example DFD:**
```
[User] ---(HTTPS)---> [Web App] ---(SQL)---> [Database]
                          |
                          +---(REST API)---> [External Payment Gateway]
```

**For Each Data Flow, Assess:**
- Is it encrypted?
- Is it authenticated?
- Is it authorized?
- Is it logged?
- What data is transmitted?

---

## Risk Scoring and Prioritization

### Quantitative Risk Scoring

**Formula:**
```
Risk Score = Likelihood × Impact × Exposure

Where:
- Likelihood: 1-5 (1=Rare, 5=Almost Certain)
- Impact: 1-5 (1=Negligible, 5=Catastrophic)
- Exposure: 1-3 (1=Internal Only, 2=Authenticated External, 3=Public)
```

**Likelihood Scale:**
- **5 - Almost Certain**: > 90% probability, happens regularly
- **4 - Likely**: 60-90% probability, happens often
- **3 - Possible**: 30-60% probability, happens sometimes
- **2 - Unlikely**: 10-30% probability, happens rarely
- **1 - Rare**: < 10% probability, almost never happens

**Impact Scale:**
- **5 - Catastrophic**: Complete system failure, major data breach, regulatory fines, bankruptcy
- **4 - Major**: Significant service disruption, substantial data loss, major financial impact
- **3 - Moderate**: Noticeable service degradation, limited data exposure, measurable costs
- **2 - Minor**: Minimal service impact, negligible data exposure, small costs
- **1 - Negligible**: No real impact, easily recovered

**Risk Priority:**
```
Score 60-75: CRITICAL - Immediate action required
Score 40-59: HIGH - Action required within 1 week
Score 20-39: MEDIUM - Action required within 1 month
Score 10-19: LOW - Action required within 3 months
Score 1-9: MINIMAL - Monitor and review
```

### Qualitative Risk Assessment

**Risk Matrix:**
```markdown
|            | Negligible | Minor | Moderate | Major | Catastrophic |
|------------|------------|-------|----------|-------|--------------|
| Almost     | Medium     | High  | High     | Critical | Critical  |
| Certain    |            |       |          |       |              |
| Likely     | Low        | Medium| High     | High  | Critical     |
| Possible   | Low        | Medium| Medium   | High  | High         |
| Unlikely   | Low        | Low   | Medium   | Medium| High         |
| Rare       | Low        | Low   | Low      | Medium| Medium       |
```

### CVSS (Common Vulnerability Scoring System)

For technical vulnerabilities, use CVSS v3.1:

**Base Score Metrics:**
- Attack Vector (AV): Network/Adjacent/Local/Physical
- Attack Complexity (AC): Low/High
- Privileges Required (PR): None/Low/High
- User Interaction (UI): None/Required
- Scope (S): Unchanged/Changed
- Confidentiality Impact (C): None/Low/High
- Integrity Impact (I): None/Low/High
- Availability Impact (A): None/Low/High

**CVSS Severity Ratings:**
- 9.0-10.0: Critical
- 7.0-8.9: High
- 4.0-6.9: Medium
- 0.1-3.9: Low

---

## Attack Surface Analysis

### Attack Surface Components

1. **Network Attack Surface**
   - Open ports and services
   - Firewall rules
   - Network segmentation
   - VPN endpoints
   - Load balancers

2. **Application Attack Surface**
   - API endpoints
   - Web forms and inputs
   - File upload functionality
   - Authentication mechanisms
   - Session management

3. **Human Attack Surface**
   - Social engineering vectors
   - Phishing susceptibility
   - Credential management
   - Access privileges

4. **Physical Attack Surface**
   - Data center access
   - Hardware disposal
   - Removable media
   - Physical network access

### Attack Surface Mapping

**Tool: Network Scanning**
```bash
# Identify open ports
nmap -sV -sC -O target-host

# Identify web application technologies
whatweb https://target-app.com

# Enumerate subdomains
subfinder -d target-domain.com

# Check for exposed services
shodan search "org:CompanyName"
```

**Attack Surface Documentation:**
```yaml
attack_surface:
  network:
    - endpoint: "api.example.com:443"
      service: "HTTPS API"
      exposure: "Public"
      authentication: "OAuth2 Bearer Token"
      rate_limiting: "Yes - 1000 req/min"
      
    - endpoint: "admin.example.com:22"
      service: "SSH"
      exposure: "VPN Only"
      authentication: "SSH Keys + 2FA"
      
  application:
    - endpoint: "/api/v1/users"
      method: "POST"
      authentication: "Required"
      input_validation: "Yes"
      rate_limiting: "Yes"
      encryption: "TLS 1.3"
```

### Reducing Attack Surface

**Strategies:**
1. **Eliminate**: Remove unnecessary services and endpoints
2. **Restrict**: Limit access through network segmentation
3. **Harden**: Apply security configurations and patches
4. **Monitor**: Detect and respond to suspicious activity

---

## Vulnerability Assessment

### Common Vulnerability Categories

**OWASP Top 10 (2021):**
1. **Broken Access Control**: Missing authorization checks
2. **Cryptographic Failures**: Weak encryption, exposed secrets
3. **Injection**: SQL, NoSQL, OS command, LDAP injection
4. **Insecure Design**: Missing security controls in design
5. **Security Misconfiguration**: Default configs, verbose errors
6. **Vulnerable Components**: Outdated libraries, dependencies
7. **Identification/Auth Failures**: Weak auth, session management
8. **Software/Data Integrity**: Unsigned updates, insecure CI/CD
9. **Logging/Monitoring Failures**: Insufficient logging
10. **SSRF**: Server-side request forgery

### Vulnerability Scanning

**Tools:**
```bash
# Web application scanning
zap-cli quick-scan https://target-app.com

# Dependency scanning
npm audit
pip-audit
snyk test

# Infrastructure scanning
trivy image docker-image:tag
checkov -d /path/to/terraform

# Static code analysis
semgrep --config=auto .
bandit -r /path/to/python/code
```

### Vulnerability Assessment Process

1. **Discovery**: Identify vulnerabilities using automated tools
2. **Validation**: Confirm vulnerabilities are exploitable
3. **Classification**: Categorize by type and severity
4. **Prioritization**: Rank by risk score
5. **Remediation**: Fix or mitigate vulnerabilities
6. **Verification**: Confirm fixes are effective
7. **Documentation**: Record findings and actions

**Vulnerability Report Template:**
```markdown
# Vulnerability: SQL Injection in User Search

## Severity: High (CVSS 8.6)

## Description
The user search endpoint is vulnerable to SQL injection, allowing attackers
to extract sensitive data from the database.

## Affected Components
- Endpoint: /api/v1/users/search
- Parameter: query
- Component: UserSearchService.java:42

## Reproduction Steps
1. Send POST request to /api/v1/users/search
2. Use payload: {"query": "' OR '1'='1"}
3. Observe all users returned regardless of search term

## Impact
- Unauthorized access to user data (Confidentiality: High)
- Potential data modification (Integrity: Medium)
- Database availability at risk (Availability: Low)

## Remediation
1. Immediate: Disable search endpoint
2. Short-term: Implement parameterized queries
3. Long-term: Add input validation, WAF rules

## Verification
- [ ] Code review completed
- [ ] Security testing passed
- [ ] Regression testing passed
```

---

## Risk Mitigation Strategies

### The 4 T's of Risk Management

1. **Transfer**: Insurance, outsourcing, cloud services
2. **Tolerate**: Accept risk if cost of mitigation > potential impact
3. **Treat**: Implement controls to reduce risk
4. **Terminate**: Eliminate the risk by removing the activity

### Defense in Depth

**Security Layers:**
```
Layer 7: User Awareness & Training
Layer 6: Application Security (WAF, input validation)
Layer 5: Authentication & Authorization
Layer 4: Network Security (firewall, IDS/IPS)
Layer 3: Encryption (TLS, at-rest encryption)
Layer 2: Logging & Monitoring
Layer 1: Physical Security
```

### Security Controls

**Preventive Controls:**
- Access controls (RBAC, ABAC)
- Encryption
- Firewalls
- Input validation
- Security training

**Detective Controls:**
- Logging and monitoring
- Intrusion detection systems
- Security audits
- Vulnerability scanning
- Penetration testing

**Corrective Controls:**
- Incident response plans
- Backup and recovery
- Patch management
- Configuration management

**Deterrent Controls:**
- Security policies
- Legal agreements
- Warning banners
- Audit trails

### Risk Treatment Plan

```markdown
# Risk Treatment Plan: High-Risk Vulnerabilities

## Risk: Unencrypted Database Backups
- Current Risk Score: 60 (High)
- Target Risk Score: 15 (Low)

### Treatment Actions:
1. **Immediate (Week 1)**
   - Enable backup encryption in AWS RDS
   - Verify existing backups cannot be decrypted
   - Update backup procedures documentation

2. **Short-term (Month 1)**
   - Implement backup monitoring
   - Set up alerts for unencrypted backups
   - Review and encrypt historical backups

3. **Long-term (Quarter 1)**
   - Establish backup encryption policy
   - Train team on secure backup practices
   - Include in regular security audits

### Success Criteria:
- [ ] 100% of backups encrypted
- [ ] Monitoring alerts configured
- [ ] Team trained
- [ ] Policy documented

### Review Date: [Date + 90 days]
```

### Continuous Risk Management

**Risk Register Maintenance:**
- Review quarterly (minimum)
- Update after significant changes
- Track risk trends over time
- Measure effectiveness of controls

**Metrics to Track:**
- Number of risks by severity
- Average time to remediate
- Risk score trends
- Control effectiveness
- Compliance posture

---

## Integration with OpenDeRisk

### Using OpenDeRisk for Risk Assessment

OpenDeRisk's multi-agent architecture can enhance risk assessment:

1. **SRE-Agent**: Analyzes operational risks from logs and metrics
2. **Code-Agent**: Identifies code-level vulnerabilities
3. **Data-Agent**: Assesses data flow and storage risks
4. **Vis-Agent**: Visualizes risk dependencies and evidence chains

**Example OpenDeRisk Workflow:**
```python
# Pseudo-code for risk assessment with OpenDeRisk
from openderisk import RiskAssessmentAgent

# Initialize agent
risk_agent = RiskAssessmentAgent()

# Analyze system
assessment = risk_agent.assess({
    "scope": "production-api",
    "frameworks": ["STRIDE", "OWASP"],
    "assets": load_asset_inventory(),
    "threat_intel": get_threat_intelligence()
})

# Generate report
report = risk_agent.generate_report(
    assessment,
    format="markdown",
    include_recommendations=True
)
```

### Integration with n8n

See the [n8n-OpenDeRisk Integration](../n8n-openderisk-integration/) skill for workflows that automate risk assessment tasks.

---

## Best Practices

### DO:
✅ Regularly update risk assessments (quarterly minimum)
✅ Involve stakeholders from different teams
✅ Document all assumptions and decisions
✅ Use both automated tools and manual review
✅ Track risk trends over time
✅ Prioritize based on business impact
✅ Test your mitigations are effective

### DON'T:
❌ Rely solely on automated scanning
❌ Ignore low-severity risks indefinitely
❌ Treat risk assessment as a one-time activity
❌ Skip validation of tool findings
❌ Ignore the human factor in security
❌ Forget to reassess after significant changes
❌ Create risks in isolation without context

---

## Quick Reference

### Risk Assessment Checklist
- [ ] Define scope and context
- [ ] Identify and inventory assets
- [ ] Identify threats and threat actors
- [ ] Conduct threat modeling (STRIDE/PASTA)
- [ ] Perform vulnerability assessment
- [ ] Calculate risk scores
- [ ] Prioritize risks
- [ ] Develop mitigation plans
- [ ] Implement controls
- [ ] Verify effectiveness
- [ ] Document findings
- [ ] Schedule next review

### Common Tools
- **Threat Modeling**: Microsoft Threat Modeling Tool, OWASP Threat Dragon
- **Vulnerability Scanning**: Nessus, OpenVAS, Qualys
- **Web App Scanning**: OWASP ZAP, Burp Suite
- **Dependency Scanning**: Snyk, Dependabot, npm audit
- **Cloud Security**: AWS Security Hub, Azure Security Center, GCP Security Command Center
- **SIEM**: Splunk, ELK Stack, Sumo Logic

### Key Frameworks and Standards
- NIST Cybersecurity Framework
- ISO 27001/27002
- CIS Controls
- OWASP SAMM (Software Assurance Maturity Model)
- FAIR (Factor Analysis of Information Risk)
- OCTAVE (Operationally Critical Threat, Asset, and Vulnerability Evaluation)
