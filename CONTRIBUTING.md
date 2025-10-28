# Contributing to derisk_skills

Thank you for your interest in contributing to **derisk_skills**! This is a **community-powered** project, and we welcome contributions from SRE professionals, DevOps engineers, and anyone passionate about risk mitigation and incident response.

---

## 🎯 How Can I Contribute?

### 1. **Create New Skills**
Share your expertise by creating new risk mitigation skills:
- SRE best practices and methodologies
- Incident response playbooks
- Monitoring and alerting patterns
- Automation workflows
- Integration guides

### 2. **Improve Existing Skills**
Enhance current skills by:
- Adding more examples and use cases
- Improving documentation clarity
- Fixing errors or outdated information
- Adding real-world scenarios

### 3. **Share n8n Workflows**
Contribute n8n workflow templates for:
- Alert ingestion and processing
- Incident response automation
- Communication and notification flows
- Remediation workflows
- Integration patterns

### 4. **Report Issues**
Help us improve by:
- Reporting bugs or errors
- Suggesting new features
- Identifying gaps in documentation
- Sharing feedback

---

## 📋 Contribution Process

### Step 1: Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/derisk_skills.git
cd derisk_skills
```

### Step 2: Create a Branch

```bash
git checkout -b feature/your-skill-name
# or
git checkout -b fix/issue-description
```

### Step 3: Make Your Changes

Follow the [Skill Development Guide](docs/SKILL_DEVELOPMENT.md) for creating new skills.

### Step 4: Test Your Changes

- Verify all markdown renders correctly
- Test examples and code snippets
- Check for broken links
- Ensure proper formatting

### Step 5: Commit and Push

```bash
git add .
git commit -m "Add: [Skill Name] - Brief description"
git push origin feature/your-skill-name
```

### Step 6: Create Pull Request

1. Go to the [derisk_skills repository](https://github.com/derisk-ai/derisk_skills)
2. Click "New Pull Request"
3. Select your branch
4. Fill in the PR template with details
5. Submit for review

---

## 🏗️ Skill Structure Guidelines

Each skill should follow this structure:

```
skills/your-skill-name/
├── README.md           # Skill overview and metadata
├── SKILL.md           # Main skill content (core knowledge)
├── EXAMPLES.md        # Practical examples and use cases
├── PATTERNS.md        # Common patterns and best practices (optional)
└── evaluations/       # Test scenarios (optional)
    ├── scenario1.md
    └── scenario2.md
```

### File Descriptions

#### `README.md`
```markdown
# Skill Name

**Brief one-line description**

## Overview
Detailed description of what this skill teaches

## When This Skill Activates
- Trigger condition 1
- Trigger condition 2
- ...

## Key Features
- Feature 1
- Feature 2
- ...

## Related Skills
- Link to related skill 1
- Link to related skill 2
```

#### `SKILL.md`
The main skill content file (500-1000 lines max):
- Core concepts and methodologies
- Step-by-step procedures
- Decision trees and workflows
- Tool and command references
- Common pitfalls and how to avoid them

#### `EXAMPLES.md`
Real-world examples:
- Scenario-based walkthroughs
- Code snippets and configurations
- Before/after comparisons
- Actual incident case studies

#### `PATTERNS.md` (optional)
Reusable patterns:
- Architectural patterns
- Workflow patterns
- Integration patterns
- Best practices

---

## ✅ Quality Standards

### Content Quality

1. **Accuracy**: All information must be technically accurate
2. **Clarity**: Write clear, concise explanations
3. **Completeness**: Cover edge cases and gotchas
4. **Actionable**: Provide concrete, actionable guidance
5. **Examples**: Include real-world examples

### Code Quality

1. **Tested**: All code examples should be tested
2. **Commented**: Add comments for complex logic
3. **Safe**: No security vulnerabilities
4. **Best Practices**: Follow industry standards

### Documentation Quality

1. **Formatting**: Use proper markdown formatting
2. **Links**: Ensure all links work
3. **Images**: Optimize images (if any) for size
4. **Spelling**: Check for typos and grammar

---

## 🎨 Style Guide

### Writing Style

- Use clear, professional language
- Write in second person ("you") when giving instructions
- Use active voice
- Keep paragraphs short and focused
- Use bullet points for lists
- Use numbered lists for sequential steps

### Code Style

**Bash/Shell**:
```bash
# Always include comments
command --option value  # Explain what this does
```

**Python** (if applicable):
```python
# Follow PEP 8
def function_name(param: str) -> dict:
    """Docstring describing the function."""
    return {"result": "value"}
```

**YAML** (for n8n workflows):
```yaml
# Use proper indentation (2 spaces)
nodes:
  - name: "Node Name"
    type: "node.type"
```

### Markdown Style

```markdown
# H1: Main title (one per file)
## H2: Major sections
### H3: Subsections
#### H4: Minor points

**Bold** for emphasis
*Italic* for technical terms
`code` for inline code
```

---

## 🔍 Review Process

### What We Look For

1. **Relevance**: Does it fit the project scope?
2. **Quality**: Is it well-written and accurate?
3. **Completeness**: Does it cover the topic adequately?
4. **Examples**: Are there sufficient examples?
5. **Testing**: Has it been tested?

### Review Timeline

- Initial review: 2-3 days
- Feedback and iterations: As needed
- Final approval: 1-2 days

### After Approval

Once approved, your contribution will be:
1. Merged into the main branch
2. Added to the skills catalog
3. Credited in release notes
4. Shared with the community

---

## 💡 Skill Ideas

Need inspiration? Here are some skill ideas:

### SRE & DevOps
- Chaos engineering practices
- Service mesh troubleshooting
- Database performance tuning
- Container orchestration best practices

### Security
- Security incident response
- Vulnerability management
- Compliance automation
- Zero-trust architecture

### Cloud Platforms
- AWS troubleshooting patterns
- Azure monitoring best practices
- GCP incident response
- Multi-cloud strategies

### Observability
- Distributed tracing patterns
- Log aggregation strategies
- Metrics design principles
- APM tool integration

---

## 🤔 Questions?

- **General Questions**: Open a [GitHub Discussion](https://github.com/derisk-ai/derisk_skills/discussions)
- **Bugs**: Create an [Issue](https://github.com/derisk-ai/derisk_skills/issues)
- **Private Inquiries**: Contact the maintainers

---

## 📜 Code of Conduct

This project follows the [OpenDeRisk Code of Conduct](https://github.com/derisk-ai/OpenDerisk/blob/main/CODE_OF_CONDUCT). Please be respectful and constructive in all interactions.

---

## 🎉 Recognition

Contributors will be:
- Listed in the project README
- Credited in release notes
- Acknowledged in the community

Thank you for helping make derisk_skills better! 🙏

---

## 📚 Additional Resources

- [Skill Development Guide](docs/SKILL_DEVELOPMENT.md)
- [OpenDeRisk Documentation](https://github.com/derisk-ai/OpenDerisk)
- [n8n Documentation](https://docs.n8n.io/)
- [Site Reliability Engineering Book](https://sre.google/books/)
