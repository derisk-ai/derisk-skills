# Risk Assessment & Analysis - Examples

## Table of Contents
1. [Complete Risk Assessment Example](#complete-risk-assessment-example)
2. [STRIDE Threat Modeling Example](#stride-threat-modeling-example)
3. [Attack Surface Analysis Example](#attack-surface-analysis-example)
4. [Vulnerability Assessment Example](#vulnerability-assessment-example)
5. [Risk Scoring Example](#risk-scoring-example)

---

## Complete Risk Assessment Example

### Scenario: E-Commerce Platform

**System Overview:**
- Web application for online shopping
- Microservices architecture (15 services)
- PostgreSQL database
- Redis cache
- AWS infrastructure
- 100,000+ daily active users
- Payment processing via Stripe

### Step 1: Asset Inventory

```yaml
assets:
  - id: "ASSET-001"
    name: "Customer Database"
    type: "Data Store"
    classification: "Confidential"
    business_value: "Critical"
    location: "AWS RDS PostgreSQL"
    contains:
      - "Customer PII"
      - "Order history"
      - "Payment tokens"
    
  - id: "ASSET-002"
    name: "Product Catalog Service"
    type: "Application"
    classification: "Internal"
    business_value: "High"
    technology: "Node.js"
    exposure: "Public API"
    
  - id: "ASSET-003"
    name: "Payment Processing Service"
    type: "Application"
    classification: "Confidential"
    business_value: "Critical"
    technology: "Python/FastAPI"
    exposure: "Internal Only"
    dependencies:
      - "Stripe API"
      - "Customer Database"
```

### Step 2: Threat Identification

```markdown
| Threat ID | Threat Name | Category | Target Asset | Likelihood | Impact | Risk Score |
|-----------|-------------|----------|--------------|------------|--------|------------|
| THR-001 | SQL Injection | Security | Customer DB | Medium (3) | Critical (5) | 45 (High) |
| THR-002 | DDoS Attack | Availability | Product API | High (4) | Major (4) | 48 (High) |
| THR-003 | API Key Leakage | Security | Payment Service | Low (2) | Critical (5) | 30 (Medium) |
| THR-004 | Session Hijacking | Security | Web App | Medium (3) | Major (4) | 36 (Medium) |
| THR-005 | Database Failure | Operational | Customer DB | Low (2) | Critical (5) | 30 (Medium) |
```

### Step 3: STRIDE Analysis for Payment Service

```markdown
## Payment Processing Service - Threat Model

### Spoofing
**THR-PAY-001: API Authentication Bypass**
- Description: Attacker bypasses API authentication to submit fraudulent payments
- Attack Vector: Exploit weak JWT validation
- Likelihood: Low (2) - Strong auth implemented
- Impact: Critical (5) - Financial loss, reputation damage
- Risk Score: 30 (Medium)
- Mitigations:
  - ✅ JWT signature verification
  - ✅ Short-lived tokens (15 min)
  - ✅ Token rotation
  - ⚠️ Missing: Hardware security module for key storage
- Recommendation: Implement AWS KMS for key management

### Tampering
**THR-PAY-002: Payment Amount Manipulation**
- Description: Attacker modifies payment amount in transit
- Attack Vector: Man-in-the-middle attack
- Likelihood: Low (2) - TLS enforced
- Impact: Critical (5) - Financial fraud
- Risk Score: 30 (Medium)
- Mitigations:
  - ✅ TLS 1.3 encryption
  - ✅ Certificate pinning
  - ✅ Request signing
  - ✅ Amount verification at multiple layers
- Recommendation: No action required, well-protected

### Repudiation
**THR-PAY-003: Payment Denial**
- Description: Customer denies making a payment
- Attack Vector: Lack of audit trail
- Likelihood: Medium (3) - Happens occasionally
- Impact: Moderate (3) - Chargeback costs
- Risk Score: 27 (Medium)
- Mitigations:
  - ✅ Transaction logging
  - ✅ Timestamp synchronization
  - ⚠️ Missing: Digital signatures for non-repudiation
- Recommendation: Implement transaction signing

### Information Disclosure
**THR-PAY-004: Payment Data Exposure in Logs**
- Description: Credit card data logged in plain text
- Attack Vector: Log file access
- Likelihood: Low (2) - Access restricted
- Impact: Catastrophic (5) - PCI DSS violation, fines
- Risk Score: 50 (High)
- Mitigations:
  - ⚠️ Missing: Log sanitization
  - ✅ Log encryption at rest
  - ✅ Restricted log access
- Recommendation: IMMEDIATE - Implement log sanitization

### Denial of Service
**THR-PAY-005: Payment Queue Exhaustion**
- Description: Attacker floods payment queue with invalid requests
- Attack Vector: Missing rate limiting
- Likelihood: Medium (3) - No rate limiting
- Impact: Major (4) - Service unavailable
- Risk Score: 36 (Medium)
- Mitigations:
  - ⚠️ Missing: Rate limiting
  - ⚠️ Missing: Request queue size limits
  - ✅ Auto-scaling configured
- Recommendation: Implement rate limiting (1000 req/hour per user)

### Elevation of Privilege
**THR-PAY-006: Admin Access via IDOR**
- Description: Attacker accesses other users' payment history via IDOR
- Attack Vector: Insecure direct object reference
- Likelihood: Medium (3) - Common vulnerability
- Impact: Critical (5) - Data breach
- Risk Score: 45 (High)
- Mitigations:
  - ⚠️ Partial: Authorization checks inconsistent
  - ✅ User context validation
- Recommendation: Comprehensive authorization audit
```

### Step 4: Risk Prioritization

**Critical Priority (Immediate Action):**
1. **THR-PAY-004**: Payment data in logs (Score: 50)
   - Action: Deploy log sanitization within 24 hours
   - Owner: Security Team
   - Deadline: Tomorrow

2. **THR-002**: DDoS vulnerability (Score: 48)
   - Action: Enable AWS Shield, configure CloudFront
   - Owner: Infrastructure Team
   - Deadline: 1 week

3. **THR-001**: SQL injection (Score: 45)
   - Action: Implement parameterized queries, deploy WAF
   - Owner: Development Team
   - Deadline: 1 week

**High Priority (Within 1 Month):**
4. **THR-PAY-006**: IDOR vulnerability (Score: 45)
   - Action: Authorization audit and remediation
   - Owner: Development Team
   - Deadline: 2 weeks

5. **THR-PAY-005**: DoS via queue exhaustion (Score: 36)
   - Action: Implement rate limiting
   - Owner: Platform Team
   - Deadline: 1 month

### Step 5: Mitigation Plan

```markdown
# Risk Mitigation Roadmap - Q1 2025

## Week 1 (Critical)
- [ ] Deploy log sanitization for payment service
- [ ] Emergency code review for SQL injection
- [ ] Enable AWS Shield Standard
- [ ] Configure CloudFront rate limiting

## Week 2 (High)
- [ ] Fix SQL injection vulnerabilities
- [ ] Deploy WAF with OWASP ruleset
- [ ] Conduct authorization audit
- [ ] Implement IDOR protection

## Week 3-4 (High)
- [ ] Implement API rate limiting
- [ ] Add queue size limits
- [ ] Deploy monitoring for rate limit violations
- [ ] Penetration testing for payment service

## Month 2 (Medium)
- [ ] Implement transaction signing
- [ ] Migrate keys to AWS KMS
- [ ] Enhance monitoring and alerting
- [ ] Update incident response playbooks

## Ongoing
- [ ] Quarterly risk reassessment
- [ ] Monthly vulnerability scanning
- [ ] Weekly dependency updates
- [ ] Continuous security training
```

---

## STRIDE Threat Modeling Example

### API Gateway Component

```markdown
# API Gateway Threat Model

## Component Description
- Central API gateway using Kong
- Handles authentication and rate limiting
- Routes to 15 backend microservices
- Processes 10M requests/day

## Data Flow
[Client] --HTTPS--> [API Gateway] --HTTP--> [Microservices]
                         |
                         +--Redis (session/cache)
                         +--PostgreSQL (analytics)

## STRIDE Analysis

### S - Spoofing
| ID | Threat | Mitigation | Status |
|----|--------|------------|--------|
| S1 | API key spoofing | HMAC signature verification | ✅ Implemented |
| S2 | JWT token forgery | RS256 with key rotation | ✅ Implemented |
| S3 | IP spoofing | X-Forwarded-For validation | ⚠️ Partial |

### T - Tampering
| ID | Threat | Mitigation | Status |
|----|--------|------------|--------|
| T1 | Request modification | Request signing | ⚠️ Missing |
| T2 | Response tampering | Response validation | ⚠️ Missing |
| T3 | Configuration tampering | IaC with version control | ✅ Implemented |

### R - Repudiation
| ID | Threat | Mitigation | Status |
|----|--------|------------|--------|
| R1 | Deny API calls | Audit logging | ✅ Implemented |
| R2 | Log tampering | Write-once logging | ⚠️ Missing |

### I - Information Disclosure
| ID | Threat | Mitigation | Status |
|----|--------|------------|--------|
| I1 | Error message leakage | Generic error responses | ✅ Implemented |
| I2 | Header information disclosure | Security headers | ✅ Implemented |
| I3 | Log data exposure | PII redaction | ⚠️ Partial |

### D - Denial of Service
| ID | Threat | Mitigation | Status |
|----|--------|------------|--------|
| D1 | Rate limit exhaustion | Progressive rate limiting | ✅ Implemented |
| D2 | Memory exhaustion | Request size limits | ✅ Implemented |
| D3 | Connection exhaustion | Connection pooling | ✅ Implemented |

### E - Elevation of Privilege
| ID | Threat | Mitigation | Status |
|----|--------|------------|--------|
| E1 | Bypass authorization | Middleware auth checks | ✅ Implemented |
| E2 | Admin path traversal | Path whitelisting | ✅ Implemented |
| E3 | Privilege escalation via API | RBAC enforcement | ✅ Implemented |

## Prioritized Remediation
1. **HIGH**: Implement request/response signing (T1, T2)
2. **MEDIUM**: Add write-once logging (R2)
3. **LOW**: Complete PII redaction (I3)
4. **LOW**: Enhance IP validation (S3)
```

---

## Attack Surface Analysis Example

### Web Application Attack Surface

```markdown
# Attack Surface Assessment - Customer Portal

## External Attack Surface

### 1. Web Application
**URL**: https://app.example.com
**Technology**: React SPA + Node.js backend
**Authentication**: OAuth2 + OIDC

Exposed Endpoints:
- `GET /api/v1/user/profile` - User data retrieval
- `POST /api/v1/orders` - Order creation
- `PUT /api/v1/user/settings` - User settings update
- `POST /api/v1/support/ticket` - Support ticket creation
- `GET /api/v1/products/*` - Product catalog (public)

Attack Vectors:
- ✅ XSS: Protected via Content Security Policy
- ⚠️ CSRF: Missing CSRF tokens on state-changing operations
- ✅ Injection: Parameterized queries, input validation
- ⚠️ Broken Auth: Session timeout set to 24 hours (too long)
- ✅ Security Misconfig: Security headers implemented
- ⚠️ Sensitive Data: API keys visible in browser DevTools

Recommendations:
1. Implement CSRF protection
2. Reduce session timeout to 1 hour
3. Move API keys to backend

### 2. API Gateway
**URL**: https://api.example.com
**Technology**: Kong Gateway
**Authentication**: API Keys + JWT

Exposed Services:
- `/v1/products` - Public product API
- `/v1/orders` - Authenticated order API
- `/v1/payments` - PCI-scoped payment API
- `/v1/admin` - Admin-only API

Attack Vectors:
- ✅ Rate Limiting: 1000 req/min per IP
- ✅ DDoS: CloudFlare protection enabled
- ⚠️ API Enumeration: Verbose error messages
- ✅ Auth Bypass: Multi-layer authorization
- ⚠️ Version Disclosure: API version in header

Recommendations:
1. Sanitize error messages
2. Remove version disclosure headers

### 3. Admin Portal
**URL**: https://admin.example.com
**Technology**: Vue.js + Django backend
**Authentication**: SSO (Okta) + 2FA

Exposed Functionality:
- User management
- Order management
- Content management
- System configuration

Attack Vectors:
- ✅ Brute Force: 2FA + account lockout
- ✅ Privilege Escalation: RBAC enforced
- ⚠️ SSRF: URL validation incomplete
- ✅ XXE: XML processing disabled
- ⚠️ Insecure Deserialization: Pickle used for sessions

Recommendations:
1. Replace Pickle with JSON sessions
2. Implement strict URL validation

## Internal Attack Surface

### 4. Database Servers
**Technology**: PostgreSQL 14
**Access**: VPC-only

Exposed Services:
- Port 5432 (within VPC only)

Attack Vectors:
- ✅ SQL Injection: Parameterized queries
- ✅ Weak Credentials: Strong password policy
- ⚠️ Unencrypted Backups: Backups not encrypted
- ✅ Network Segmentation: Isolated in private subnet
- ✅ Encryption: TLS for connections

Recommendations:
1. Enable backup encryption immediately

### 5. Message Queue
**Technology**: RabbitMQ
**Access**: VPC-only

Exposed Services:
- Port 5672 (AMQP)
- Port 15672 (Management UI)

Attack Vectors:
- ⚠️ Default Credentials: Still using guest/guest
- ✅ Network Access: VPC-restricted
- ⚠️ Unencrypted Traffic: No TLS
- ⚠️ Management UI: Exposed to entire VPC

Recommendations:
1. Change default credentials
2. Enable TLS
3. Restrict management UI access

## Attack Surface Summary

| Surface | Severity | Priority | Status |
|---------|----------|----------|--------|
| CSRF Protection | High | 1 | ⚠️ Missing |
| Database Backups | High | 2 | ⚠️ Unencrypted |
| RabbitMQ Default Creds | Critical | 3 | ⚠️ Unchanged |
| Session Timeout | Medium | 4 | ⚠️ Too Long |
| API Keys in Browser | Medium | 5 | ⚠️ Exposed |
| SSRF in Admin | Medium | 6 | ⚠️ Incomplete |
```

---

## Vulnerability Assessment Example

### Automated Scan Results

```markdown
# Vulnerability Assessment Report
**Date**: 2025-01-15
**Scope**: Production Web Application
**Tools**: OWASP ZAP, npm audit, Trivy

## Executive Summary
- Total Vulnerabilities: 47
- Critical: 2
- High: 8
- Medium: 15
- Low: 22

## Critical Vulnerabilities

### VULN-001: SQL Injection in Search Function
**CVSS Score**: 9.8 (Critical)
**Location**: /api/v1/search?q=<input>
**Description**: User input directly concatenated into SQL query

**Proof of Concept**:
```bash
curl "https://api.example.com/api/v1/search?q=test%27%20OR%20%271%27=%271"
# Returns all records regardless of search term
```

**Vulnerable Code**:
```javascript
// search.controller.js:42
const query = `SELECT * FROM products WHERE name LIKE '%${req.query.q}%'`;
db.query(query, (err, results) => {
  // ...
});
```

**Remediation**:
```javascript
// Fixed version
const query = 'SELECT * FROM products WHERE name LIKE $1';
db.query(query, [`%${req.query.q}%`], (err, results) => {
  // ...
});
```

**Timeline**:
- Discovered: 2025-01-15
- Reported: 2025-01-15
- Fix Deployed: 2025-01-16 (URGENT)
- Verified: 2025-01-17

### VULN-002: Authentication Bypass via JWT None Algorithm
**CVSS Score**: 9.1 (Critical)
**Location**: /api/v1/auth/verify
**Description**: JWT verification accepts 'none' algorithm

**Proof of Concept**:
```python
import jwt

# Create token with 'none' algorithm
token = jwt.encode(
    {"user_id": "admin", "role": "admin"},
    "",
    algorithm="none"
)
# Token is accepted by the API
```

**Vulnerable Code**:
```javascript
// auth.middleware.js:15
jwt.verify(token, process.env.JWT_SECRET);
// No algorithm whitelist specified
```

**Remediation**:
```javascript
// Fixed version
jwt.verify(token, process.env.JWT_SECRET, {
  algorithms: ['RS256']  // Explicitly whitelist algorithms
});
```

**Timeline**:
- Discovered: 2025-01-15
- Reported: 2025-01-15
- Fix Deployed: 2025-01-15 (IMMEDIATE)
- Verified: 2025-01-16

## High Vulnerabilities

### VULN-003: Insecure Direct Object Reference (IDOR)
**CVSS Score**: 7.5 (High)
**Location**: /api/v1/orders/{orderId}
**Description**: No authorization check for order access

**Proof of Concept**:
```bash
# User A can access User B's orders
curl -H "Authorization: Bearer <user_a_token>" \
  https://api.example.com/api/v1/orders/user_b_order_123
# Returns User B's order details
```

**Remediation**:
```javascript
// orders.controller.js
async function getOrder(req, res) {
  const order = await Order.findById(req.params.orderId);
  
  // Add authorization check
  if (order.userId !== req.user.id) {
    return res.status(403).json({ error: "Unauthorized" });
  }
  
  res.json(order);
}
```

### VULN-004-010: [Additional High Severity Vulnerabilities]
- VULN-004: XSS in comment field (CVSS 7.2)
- VULN-005: Missing rate limiting on password reset (CVSS 7.0)
- VULN-006: Sensitive data in error messages (CVSS 6.8)
- VULN-007: Outdated Express.js version (CVSS 6.5)
- VULN-008: CORS misconfiguration (CVSS 6.3)
- VULN-009: Weak session ID generation (CVSS 6.1)
- VULN-010: Information disclosure via stack traces (CVSS 6.0)

## Dependency Vulnerabilities

### npm audit Results:
```
found 15 vulnerabilities (3 high, 12 moderate)

high severity vulnerabilities:
- lodash: Prototype Pollution (CVE-2020-8203)
- axios: SSRF via URL manipulation (CVE-2021-3749)
- handlebars: RCE via template injection (CVE-2021-23383)

Remediation:
npm audit fix --force
```

## Remediation Summary

| Priority | Count | Target Date | Owner |
|----------|-------|-------------|-------|
| Critical | 2 | 2025-01-16 | Security Team |
| High | 8 | 2025-01-22 | Dev Team |
| Medium | 15 | 2025-02-15 | Dev Team |
| Low | 22 | 2025-03-31 | Dev Team |

## Re-scan Schedule
- Next scan: 2025-02-01
- Frequency: Bi-weekly
```

---

## Risk Scoring Example

### Detailed Risk Calculation

**Scenario**: Evaluating risk of database credential exposure

**Step 1: Determine Likelihood**
```markdown
Likelihood Factors:
- Credentials stored in Git repository: +3
- Repository is private: -1
- 20 developers have access: +2
- No secrets scanning enabled: +1
- Credential rotation policy: never rotated: +2

Likelihood Score: 3-1+2+1+2 = 7/10 → Scale to 1-5 = 4 (Likely)
```

**Step 2: Determine Impact**
```markdown
Impact Analysis:
- Confidentiality: Database contains customer PII → Critical (5)
- Integrity: Attacker could modify/delete data → Critical (5)
- Availability: Attacker could drop database → Critical (5)
- Financial: Potential regulatory fines + lawsuit → $5M+ (5)
- Reputation: Major media coverage, customer churn → Critical (5)

Impact Score: 5 (Catastrophic)
```

**Step 3: Determine Exposure**
```markdown
Exposure Factors:
- Access level: Internal developers only
- But: Git history is public via mirror: Public exposure
- Credential could work from anywhere: Network accessible

Exposure Score: 3 (Public)
```

**Step 4: Calculate Risk Score**
```
Risk Score = Likelihood × Impact × Exposure
Risk Score = 4 × 5 × 3 = 60

Classification: CRITICAL (60/75)
```

**Step 5: Risk Treatment**
```markdown
# Risk Treatment Plan: Database Credential Exposure

## Immediate Actions (24 hours)
1. Rotate database credentials
2. Remove credentials from Git history (BFG Repo-Cleaner)
3. Enable AWS Secrets Manager
4. Audit access logs for suspicious activity

## Short-term Actions (1 week)
1. Implement git-secrets pre-commit hook
2. Enable GitHub secret scanning
3. Migrate all credentials to secrets manager
4. Update deployment pipelines

## Long-term Actions (1 month)
1. Implement automated credential rotation
2. Set up alerting for credential access
3. Conduct security awareness training
4. Regular secrets scanning in CI/CD

## Residual Risk
After mitigation:
- Likelihood: 1 (Rare) - Secrets manager + scanning
- Impact: 5 (Catastrophic) - Still critical data
- Exposure: 1 (Internal) - Secrets manager access only
- New Risk Score: 1 × 5 × 1 = 5 (MINIMAL)

Risk reduced by 91% (from 60 to 5)
```

---

## Integration Example: OpenDeRisk + Risk Assessment

```python
# Example: Automated risk assessment using OpenDeRisk

from openderisk import SREAgent, CodeAgent, RiskAnalyzer

# Initialize agents
sre_agent = SREAgent()
code_agent = CodeAgent()
risk_analyzer = RiskAnalyzer()

# Collect data from multiple sources
logs = sre_agent.collect_logs(
    source="cloudwatch",
    time_range="last_24h",
    filter="error|warning|exception"
)

code_vulns = code_agent.scan_repository(
    repo="github.com/company/app",
    scanners=["semgrep", "bandit", "npm-audit"]
)

infra_config = sre_agent.analyze_infrastructure(
    provider="aws",
    resources=["ec2", "rds", "s3", "iam"]
)

# Perform comprehensive risk analysis
risk_assessment = risk_analyzer.assess({
    "logs": logs,
    "vulnerabilities": code_vulns,
    "infrastructure": infra_config,
    "frameworks": ["STRIDE", "OWASP"],
    "compliance": ["PCI-DSS", "SOC2"]
})

# Generate prioritized risk report
report = risk_analyzer.generate_report(
    assessment=risk_assessment,
    format="markdown",
    include_remediation=True,
    prioritize_by="risk_score"
)

print(report)
```

**Example Output:**
```markdown
# Risk Assessment Report - 2025-01-15

## Critical Risks (Immediate Action Required)
1. SQL Injection in search endpoint (Score: 60)
2. Unencrypted database backups (Score: 50)
3. Default RabbitMQ credentials (Score: 48)

## High Risks (Action Required Within 1 Week)
4. Missing CSRF protection (Score: 45)
5. IDOR vulnerability in orders API (Score: 42)
...

## Recommended Actions
### Critical Priority
- [ ] Fix SQL injection (ETA: 24h)
- [ ] Enable backup encryption (ETA: 24h)
- [ ] Rotate RabbitMQ credentials (ETA: 24h)

## Compliance Impact
- PCI-DSS: 3 violations (Critical: 2, High: 1)
- SOC2: 5 gaps (Critical: 1, Medium: 4)
```
