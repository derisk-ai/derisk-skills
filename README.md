# derisk_skills

**Community-Powered Risk Mitigation Skills for OpenDeRisk & n8n**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![OpenDeRisk](https://img.shields.io/badge/OpenDeRisk-compatible-green.svg)](https://github.com/derisk-ai/OpenDerisk)
[![n8n](https://img.shields.io/badge/n8n-compatible-blue.svg)](https://n8n.io/)

---

## 🎯 What is this?

This repository contains **community-contributed skills** for AI-powered risk mitigation, incident response, and SRE automation using [OpenDeRisk](https://github.com/derisk-ai/OpenDerisk) and [n8n](https://n8n.io/) workflow automation platform.

### Why These Skills Exist

Managing complex distributed systems requires deep expertise in:
- Risk assessment and threat modeling
- Root cause analysis (RCA) for production incidents
- Incident response and remediation workflows
- Monitoring, alerting, and anomaly detection
- Integration with workflow automation platforms

These skills solve these problems by providing:
- ✅ AI-powered risk assessment and analysis frameworks
- ✅ Proven RCA methodologies and patterns
- ✅ Incident response playbooks and workflows
- ✅ n8n workflow templates for risk mitigation
- ✅ Integration guides for OpenDeRisk multi-agent systems

---

## 📚 Available Skills

### OpenDeRisk Risk Mitigation Skills

#### 1. **Risk Assessment & Analysis**
AI-powered risk assessment and threat modeling for distributed systems.

**Key Features**:
- Threat identification and classification
- Risk scoring and prioritization
- Attack surface analysis
- Vulnerability assessment frameworks

#### 2. **Root Cause Analysis (RCA)**
Deep research and analysis for incident root cause determination.

**Key Features**:
- Log, trace, and metric correlation
- Evidence chain visualization
- Multi-agent collaboration patterns
- Code-level analysis techniques

#### 3. **Incident Response**
Structured incident response workflows and playbooks.

**Key Features**:
- Incident classification and severity assessment
- Response playbook templates
- Communication workflows
- Post-mortem analysis

#### 4. **Monitoring & Alerting**
Intelligent monitoring, alerting, and anomaly detection.

**Key Features**:
- Alert rule configuration
- Anomaly detection patterns
- Metric correlation techniques
- Alert fatigue reduction

#### 5. **Remediation & Recovery**
Automated remediation and system recovery workflows.

**Key Features**:
- Automated fix deployment
- Rollback strategies
- Recovery verification
- Post-incident validation

### n8n Integration Skills

#### 6. **n8n-OpenDeRisk Integration**
Connect n8n workflows with OpenDeRisk agents and services.

**Key Features**:
- OpenDeRisk API integration
- Agent orchestration via n8n
- MCP service integration
- Data flow patterns

#### 7. **n8n Risk Workflow Patterns**
Proven n8n workflow patterns for risk mitigation scenarios.

**Key Features**:
- Alert ingestion workflows
- Incident response automation
- Escalation patterns
- Notification and communication flows

---

## 🚀 Quick Start

### Prerequisites

- **OpenDeRisk** installed ([Installation Guide](https://github.com/derisk-ai/OpenDerisk))
- **n8n** (optional, for workflow automation) ([Installation Guide](https://docs.n8n.io/))
- AI assistant with skill support (Claude, GitHub Copilot, etc.)

### Installation

**Method 1: Clone Repository**
```bash
# Clone this repository
git clone https://github.com/derisk-ai/derisk_skills.git

# Skills are in the skills/ directory
cd derisk_skills/skills
```

**Method 2: Download Individual Skills**
Download specific skill folders from the `skills/` directory as needed.

---

## 💡 Usage

### With AI Assistants

Skills activate automatically when relevant queries are detected:

```
"How do I assess risks in my distributed system?"
→ Activates: Risk Assessment & Analysis

"Analyze this production incident and find the root cause"
→ Activates: Root Cause Analysis (RCA)

"Create an incident response workflow"
→ Activates: Incident Response

"Set up monitoring for my services"
→ Activates: Monitoring & Alerting

"Automate remediation for this issue"
→ Activates: Remediation & Recovery

"Integrate OpenDeRisk with n8n"
→ Activates: n8n-OpenDeRisk Integration

"Build an alert workflow in n8n"
→ Activates: n8n Risk Workflow Patterns
```

### Skills Work Together

When you ask: **"Build an end-to-end incident response system with OpenDeRisk and n8n"**

1. **Risk Assessment** identifies potential risks
2. **Monitoring & Alerting** sets up detection
3. **n8n-OpenDeRisk Integration** connects the platforms
4. **n8n Risk Workflow Patterns** creates automation
5. **Incident Response** provides response playbooks
6. **Root Cause Analysis** guides investigation
7. **Remediation & Recovery** automates fixes

All skills compose seamlessly!

---

## 📖 Documentation

- [Contributing Guide](CONTRIBUTING.md) - How to contribute new skills
- [Skill Development Guide](docs/SKILL_DEVELOPMENT.md) - Creating your own skills
- [OpenDeRisk Integration](docs/OPENDERISK_INTEGRATION.md) - Deep dive into OpenDeRisk
- [n8n Workflow Templates](examples/n8n-workflows/) - Ready-to-use workflow examples

---

## 🏗️ Repository Structure

```
derisk_skills/
├── skills/                          # All skill definitions
│   ├── risk-assessment/            # Risk assessment skill
│   ├── root-cause-analysis/        # RCA skill
│   ├── incident-response/          # Incident response skill
│   ├── monitoring-alerting/        # Monitoring & alerting skill
│   ├── remediation-recovery/       # Remediation & recovery skill
│   ├── n8n-openderisk-integration/ # n8n integration skill
│   └── n8n-risk-workflows/         # n8n workflow patterns skill
├── examples/                        # Example implementations
│   ├── n8n-workflows/              # n8n workflow templates
│   ├── risk-scenarios/             # Risk scenario examples
│   └── playbooks/                  # Incident response playbooks
├── docs/                           # Documentation
│   ├── SKILL_DEVELOPMENT.md        # How to create skills
│   ├── OPENDERISK_INTEGRATION.md   # OpenDeRisk integration guide
│   └── BEST_PRACTICES.md           # SRE and DevOps best practices
├── README.md                       # This file
├── CONTRIBUTING.md                 # Contribution guidelines
└── LICENSE                         # MIT License
```

---

## 🤝 Contributing

We welcome community contributions! This is a **community-powered** project.

### How to Contribute

1. **Share Your Skills**: Create skills based on your SRE/DevOps expertise
2. **Improve Existing Skills**: Enhance documentation, add examples
3. **Add Workflow Templates**: Share n8n workflows and automation patterns
4. **Report Issues**: Help us improve by reporting bugs or gaps

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 🌟 Community

Join the OpenDeRisk community:

- **GitHub Discussions**: [OpenDeRisk Discussions](https://github.com/derisk-ai/OpenDerisk/discussions)
- **Issues**: Report bugs or request features
- **Pull Requests**: Submit your contributions

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

This project builds upon:
- [OpenDeRisk](https://github.com/derisk-ai/OpenDerisk) - AI-Native Risk Intelligence Systems
- [n8n](https://n8n.io/) - Workflow Automation Platform
- [n8n-skills](https://github.com/czlonkowski/n8n-skills) - Inspiration for skill structure

---

## 📊 What's Included

- **7** comprehensive risk mitigation skills
- **Multi-agent** collaboration patterns
- **Production-tested** incident response playbooks
- **n8n workflow** templates for automation
- **Community-driven** knowledge sharing

---

**Ready to enhance your SRE and DevOps capabilities? Get started now!** 🚀
