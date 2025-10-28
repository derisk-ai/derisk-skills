# Risk Scenarios

This directory contains example risk scenarios with detailed analysis and mitigation strategies.

## Scenarios

### 1. Database Connection Pool Exhaustion
**File**: `database-connection-exhaustion.md`
**Category**: Performance / Availability
**Severity**: High

A production service experiences database connection pool exhaustion due to a code change that doesn't properly release connections.

**Key Learning Points**:
- Resource leak detection
- Connection pool monitoring
- Code review practices
- Testing strategies

---

### 2. Unencrypted Backup Exposure
**File**: `unencrypted-backup-exposure.md`
**Category**: Security / Compliance
**Severity**: Critical

Database backups are discovered to be stored unencrypted in cloud storage, violating compliance requirements.

**Key Learning Points**:
- Data at rest encryption
- Compliance requirements
- Backup security
- Audit processes

---

### 3. Third-Party API Dependency Failure
**File**: `third-party-api-failure.md`
**Category**: Resilience / Dependencies
**Severity**: High

A critical third-party payment API experiences an outage, cascading to internal systems.

**Key Learning Points**:
- Circuit breaker patterns
- Graceful degradation
- Dependency management
- Fallback strategies

---

### 4. Configuration Drift Leading to Outage
**File**: `configuration-drift-outage.md`
**Category**: Operations / Configuration
**Severity**: Medium

Manual configuration changes across environments lead to inconsistencies and service failures.

**Key Learning Points**:
- Infrastructure as Code (IaC)
- Configuration management
- Environment parity
- Change control

---

### 5. Insufficient Rate Limiting Causes DDoS
**File**: `ddos-rate-limiting.md`
**Category**: Security / Availability
**Severity**: High

Lack of proper rate limiting allows a DDoS attack to overwhelm the API gateway.

**Key Learning Points**:
- Rate limiting strategies
- DDoS protection
- API security
- Scalability planning

---

## How to Use These Scenarios

### For Learning
1. Read the scenario description
2. Try to identify risks before reading the analysis
3. Compare your approach with the provided solution
4. Apply lessons to your own systems

### For Training
1. Use as tabletop exercises
2. Discuss with your team
3. Role-play incident response
4. Document your team's approach

### For Reference
1. Bookmark relevant scenarios
2. Use during incident response
3. Reference during risk assessments
4. Include in runbooks

## Scenario Structure

Each scenario includes:

1. **Overview**: Brief description
2. **Context**: System architecture and background
3. **Incident Timeline**: How events unfolded
4. **Risk Analysis**: Threats, vulnerabilities, impact
5. **Root Cause**: Underlying issues
6. **Immediate Response**: What was done
7. **Permanent Fix**: Long-term solution
8. **Preventive Measures**: How to avoid recurrence
9. **Lessons Learned**: Key takeaways
10. **OpenDeRisk Integration**: How OpenDeRisk could help

## Contributing Scenarios

Have an interesting risk scenario from your experience?

1. Anonymize any sensitive information
2. Follow the scenario template
3. Include thorough analysis
4. Add preventive measures
5. Submit a pull request

### Scenario Template

```markdown
# Scenario Title

## Overview
Brief 2-3 sentence description

## System Context
- Architecture overview
- Technologies involved
- Scale and criticality

## Incident Timeline
Chronological events

## Risk Analysis
### Threats Identified
### Vulnerabilities Exploited
### Impact Assessment

## Root Cause Analysis
What really caused this?

## Response Actions
### Immediate Response
### Temporary Mitigation
### Permanent Fix

## Preventive Measures
How to prevent this in the future

## Lessons Learned
Key takeaways

## OpenDeRisk Application
How OpenDeRisk agents could help

## Related Skills
- [Skill 1](../../skills/skill-1/)
```

## By Category

### Security
- Unencrypted Backup Exposure
- DDoS via Rate Limiting Gap
- (More coming soon)

### Performance
- Database Connection Pool Exhaustion
- (More coming soon)

### Resilience
- Third-Party API Dependency Failure
- (More coming soon)

### Operations
- Configuration Drift Leading to Outage
- (More coming soon)

## Additional Resources

- [Risk Assessment Skill](../../skills/risk-assessment/)
- [Root Cause Analysis Skill](../../skills/root-cause-analysis/)
- [Incident Response Skill](../../skills/incident-response/)
- [Google SRE Book](https://sre.google/books/)
