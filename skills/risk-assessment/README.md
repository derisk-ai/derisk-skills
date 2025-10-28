# Risk Assessment & Analysis

**AI-powered risk assessment and threat modeling for distributed systems**

## Overview

This skill provides comprehensive guidance on risk assessment and threat modeling for complex distributed systems. It covers methodologies for identifying, analyzing, and prioritizing risks in production environments, infrastructure, and applications.

## When This Skill Activates

- "How do I assess risks in my system?"
- "What are the security threats for my application?"
- "Help me create a threat model"
- "How do I prioritize risks?"
- "What vulnerabilities should I look for?"
- "Conduct a risk assessment for my infrastructure"
- "Identify attack surfaces in my system"

## Key Features

- **Risk Identification**: Systematic approaches to discovering potential risks
- **Threat Modeling**: STRIDE, PASTA, and other threat modeling frameworks
- **Risk Scoring**: Quantitative and qualitative risk assessment methods
- **Attack Surface Analysis**: Identifying and mapping exposure points
- **Vulnerability Assessment**: Common vulnerability patterns and detection
- **Risk Prioritization**: Decision frameworks for prioritizing remediation
- **Compliance Mapping**: Aligning risks with compliance requirements

## Core Concepts

### Risk Categories
- **Security Risks**: Unauthorized access, data breaches, malware
- **Operational Risks**: System failures, performance degradation, capacity issues
- **Compliance Risks**: Regulatory violations, audit failures
- **Business Continuity Risks**: Disaster recovery, data loss, service disruption

### Risk Metrics
- **Likelihood**: Probability of risk occurrence (Low/Medium/High or 1-5 scale)
- **Impact**: Severity of consequences (Low/Medium/High or 1-5 scale)
- **Risk Score**: Likelihood × Impact
- **Exposure**: Attack surface size and accessibility

## Methodologies

### STRIDE Threat Modeling
- **S**poofing: Identity impersonation
- **T**ampering: Data modification
- **R**epudiation: Denial of actions
- **I**nformation Disclosure: Data leakage
- **D**enial of Service: Availability attacks
- **E**levation of Privilege: Unauthorized access escalation

### PASTA (Process for Attack Simulation and Threat Analysis)
1. Define business objectives
2. Define technical scope
3. Application decomposition
4. Threat analysis
5. Vulnerability analysis
6. Attack modeling
7. Risk and impact analysis

### Risk Matrix
```
        Low Impact  Medium Impact  High Impact
High    Medium      High           Critical
Likelihood
Medium  Low         Medium         High
Likelihood
Low     Low         Low            Medium
Likelihood
```

## Related Skills

- [Root Cause Analysis](../root-cause-analysis/) - For investigating incidents
- [Incident Response](../incident-response/) - For handling security incidents
- [Monitoring & Alerting](../monitoring-alerting/) - For detecting risks
