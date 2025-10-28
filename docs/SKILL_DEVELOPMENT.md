# Skill Development Guide

## Creating New Skills for derisk_skills

This guide explains how to create high-quality risk mitigation skills for the derisk_skills repository.

## Skill Structure

Each skill should follow this directory structure:

```
skills/skill-name/
├── README.md           # Skill overview and metadata
├── SKILL.md           # Main skill content (core knowledge)
├── EXAMPLES.md        # Practical examples (optional but recommended)
├── PATTERNS.md        # Common patterns (optional)
└── evaluations/       # Test scenarios (optional)
    ├── scenario1.md
    └── scenario2.md
```

## README.md Template

```markdown
# Skill Name

**Brief one-line description**

## Overview
2-3 paragraphs describing the skill's purpose and scope

## When This Skill Activates
- List of trigger phrases or queries
- Use actual examples users might say
- Include variations

## Key Features
- Feature 1
- Feature 2
- Feature 3

## Core Concepts (optional)
Brief explanation of key concepts

## Related Skills
- [Skill 1](../skill-1/) - How it relates
- [Skill 2](../skill-2/) - How it relates
```

## SKILL.md Guidelines

The SKILL.md file is the core knowledge document:

### Structure
1. **Table of Contents**: Link to major sections
2. **Core Content**: Organized by topic
3. **Quick Reference**: Checklists, commands, tables
4. **Integration Points**: Links to related skills

### Content Guidelines

**DO:**
- Use clear section headers
- Include code examples with explanations
- Provide step-by-step procedures
- Add decision trees or flowcharts (as text)
- Include real-world scenarios
- Reference industry standards
- Link to official documentation

**DON'T:**
- Exceed 1000 lines (aim for 500-800)
- Include speculation or opinions as facts
- Copy-paste large blocks of code without context
- Use jargon without explanation
- Skip error handling in examples

### Code Examples

All code examples should:
- Be tested and working
- Include comments
- Show both good and bad patterns
- Include error handling
- Use realistic data

```python
# Good example with context
from openderisk import SREAgent

# Initialize SRE agent for log analysis
agent = SREAgent()

try:
    # Analyze logs from the last 24 hours
    result = agent.analyze_logs(
        time_range="24h",
        severity="error",
        service="payment-api"
    )
    print(f"Found {result.error_count} errors")
except Exception as e:
    print(f"Analysis failed: {e}")
    # Handle error appropriately
```

## EXAMPLES.md Guidelines

Provide real-world, complete examples:

### Structure
1. **Scenario Description**: What problem does this solve?
2. **Prerequisites**: What's needed to use this example
3. **Step-by-Step Walkthrough**: Complete implementation
4. **Explanation**: Why each step matters
5. **Expected Results**: What success looks like
6. **Troubleshooting**: Common issues and fixes

### Example Template

```markdown
## Example: [Descriptive Title]

### Scenario
[2-3 sentences describing the real-world problem]

### Prerequisites
- Tool/library version X.Y.Z
- Access to [service]
- Configuration [requirement]

### Implementation

#### Step 1: [Action]
[Explanation of why this step is needed]

```bash
# Command or code
command --option value
```

[Explanation of what this does]

#### Step 2: [Action]
...

### Expected Output
```
[Show what users should see]
```

### Troubleshooting
**Issue**: [Common problem]
**Solution**: [How to fix it]
```

## Quality Checklist

Before submitting a skill, verify:

- [ ] README.md is complete and clear
- [ ] SKILL.md follows the structure guidelines
- [ ] All code examples are tested and working
- [ ] Examples are relevant and realistic
- [ ] Links to related skills are correct
- [ ] No sensitive information (API keys, passwords) included
- [ ] Grammar and spelling are correct
- [ ] Markdown formatting is proper
- [ ] File names use kebab-case (lowercase with hyphens)

## SRE and Risk Mitigation Focus

Skills should emphasize:

1. **Reliability**: How to build and maintain reliable systems
2. **Observability**: Monitoring, alerting, and debugging
3. **Automation**: Reducing toil through automation
4. **Best Practices**: Industry-standard approaches
5. **OpenDeRisk Integration**: Leveraging AI agents
6. **n8n Workflows**: Practical automation patterns

## Testing Your Skill

### Manual Testing
1. Read through the skill as if you're a user
2. Try to follow all examples
3. Check all links work
4. Verify code examples execute correctly

### Peer Review
- Ask a colleague to review
- Get feedback from potential users
- Test with AI assistants if possible

## Submission Process

1. **Create** skill in appropriate directory
2. **Test** all examples and links
3. **Document** in main README.md
4. **Submit** pull request with:
   - Skill files
   - Updates to main README.md
   - Brief description of the skill
   - Any dependencies or prerequisites

## Examples of Good Skills

Study these skills for reference:
- [Risk Assessment](../skills/risk-assessment/) - Comprehensive with examples
- [Root Cause Analysis](../skills/root-cause-analysis/) - Structured approach
- [n8n-OpenDeRisk Integration](../skills/n8n-openderisk-integration/) - Practical templates

## Getting Help

- **Questions**: Open a discussion on GitHub
- **Issues**: Report bugs or gaps
- **Ideas**: Suggest new skills or improvements

## Resources

### SRE and DevOps
- [Google SRE Book](https://sre.google/books/)
- [Site Reliability Workbook](https://sre.google/workbook/table-of-contents/)
- [The Phoenix Project](https://itrevolution.com/the-phoenix-project/)

### Risk Management
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CIS Controls](https://www.cisecurity.org/controls)

### Tools and Platforms
- [OpenDeRisk Documentation](https://github.com/derisk-ai/OpenDerisk)
- [n8n Documentation](https://docs.n8n.io/)
- [Prometheus](https://prometheus.io/docs/)
- [Grafana](https://grafana.com/docs/)

---

**Happy skill building! 🚀**
