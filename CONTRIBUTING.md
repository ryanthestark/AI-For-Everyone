# Contributing to AI-For-Everyone

Welcome! We're excited that you want to contribute to making AI education accessible to everyone. This guide will help you get started.

## 🎯 Our Mission

AI-For-Everyone is an educational initiative designed to make AI accessible, transparent, and practical for everyone. We welcome contributions that help further this mission.

## 🤝 How to Contribute

### Types of Contributions

We welcome many types of contributions:

- **Educational content** - Lessons, tutorials, examples
- **Documentation** - Improving clarity, fixing typos, adding examples
- **Code** - Tools, automation, improvements
- **Ideas** - Feature requests, suggestions, discussions
- **Bug reports** - Help us improve quality

### Getting Started

1. **Check existing issues** - Someone might already be working on it
2. **Use our templates** - We have templates for different issue types
3. **Start a discussion** - For big ideas, discuss first before building
4. **Be transparent about AI** - We embrace AI tools and ask you to label their use

## 🚀 Contribution Workflow

### 1. Create or Find an Issue

- Browse [existing issues](https://github.com/ryanthestark/AI-For-Everyone/issues)
- Or [create a new issue](https://github.com/ryanthestark/AI-For-Everyone/issues/new/choose) using our templates
- Comment on the issue to let others know you're working on it

### 2. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/AI-For-Everyone.git
cd AI-For-Everyone
```

### 3. Create a Branch

```bash
# Create a branch for your work
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bugfix-name
```

### 4. Make Your Changes

- Keep changes focused and related to the issue
- Follow existing code style and conventions
- Write clear commit messages
- Test your changes if applicable

### 5. Submit a Pull Request

- Push your branch to your fork
- Open a Pull Request against the main repository
- Fill out the PR template (it will load automatically)
- Check the boxes for any AI assistance you used

## 🔒 Security & Safety (Important!)

**This is a PUBLIC repository** - everything you commit is visible to the world.

### Before You Commit

**Never commit:**
- API keys, tokens, or passwords
- Private SSH keys or certificates
- Personal information (real names of minors, addresses, phone numbers, SSNs)
- Proprietary or confidential information

**Read our [Security Practices Guide](./SECURITY.md)** for detailed guidance.

### Automated Security Checks

Every Pull Request runs automated security checks:

1. **Secret Scanning** - Detects accidentally committed secrets (BLOCKS PR if found)
2. **Content Hygiene** - Warns about potential PII or sensitive patterns

These checks help protect you and the community!

### Optional: Pre-Commit Hooks (Recommended)

For an extra safety layer, install pre-commit hooks that check your code **before** you commit locally:

```bash
# Install pre-commit
pip install pre-commit

# Install the hooks for this repository
cd AI-For-Everyone
pre-commit install
```

**What this does:**
- Scans for secrets before each commit
- Checks for PII and sensitive patterns
- Checks file hygiene (trailing whitespace, file size, etc.)
- Blocks commits with issues so you can fix them

**Running manually:**
```bash
# Check all files
pre-commit run --all-files

# Check specific files
pre-commit run --files path/to/file.py
```

**This is optional but recommended** - it catches issues earlier and saves time vs. fixing them after CI runs.

## 🤖 AI Transparency

We embrace AI tools and ask contributors to be transparent about their use:

### Using AI Tools

You're welcome to use AI tools like:
- ChatGPT, Claude, or other LLMs
- GitHub Copilot (editor or agent)
- Any other AI assistants

### Labeling AI Usage

When you create issues or PRs, our templates include an **AI Assistance** section:

```markdown
### AI Assistance (optional)
- [ ] ChatGPT (planning / wording)
- [ ] GitHub Copilot (editor)
- [ ] Copilot Agent (automation)
- [ ] Other AI tool (please specify)
```

**Please check the boxes** for any AI tools you used. This helps us:
- Learn from each other's AI usage patterns
- Track what works well for different tasks
- Demonstrate best practices in AI-aware development

**Optional but helpful:** Add a note about how AI helped:

```markdown
_AI assistance: ChatGPT helped structure the lesson outline,
Copilot provided code completions during implementation._
```

See our [AI Governance Guide](./docs/ai-governance.md) for more details.

## 📝 Style & Conventions

### Code

- Follow existing patterns in the codebase
- Write clear, self-documenting code
- Add comments for complex logic
- Keep functions focused and small

### Documentation

- Use clear, accessible language
- Include examples where helpful
- Check spelling and grammar
- Use inclusive language

### Commit Messages

Write clear commit messages:

```bash
# Good
git commit -m "Add secret scanning workflow"
git commit -m "Fix typo in SECURITY.md"
git commit -m "Update pre-commit hooks to v4.5.0"

# Less helpful
git commit -m "updates"
git commit -m "fix stuff"
```

## 🧪 Testing

- Test your changes before submitting
- If you add code, consider adding tests
- For documentation, proofread carefully
- For workflows, test with `workflow_dispatch` if possible

## 📋 Pull Request Checklist

Before submitting your PR, make sure:

- [ ] You've tested your changes
- [ ] You've checked for secrets and PII (pre-commit helps!)
- [ ] You've filled out the PR template
- [ ] You've labeled any AI assistance used
- [ ] Commit messages are clear
- [ ] Changes are focused on the issue being addressed

## 🎨 Best Practices

### DO:

✅ Read existing docs and code before starting
✅ Ask questions in Discussions if unsure
✅ Keep PRs focused and reasonably sized
✅ Be patient - maintainers are volunteers
✅ Be respectful and inclusive
✅ Have fun and learn!

### DON'T:

❌ Submit PRs without an associated issue
❌ Make unrelated changes in the same PR
❌ Commit secrets or personal information
❌ Copy code without proper attribution
❌ Expect immediate responses (we're volunteers!)

## ❓ Questions?

- **General questions:** Use [GitHub Discussions](https://github.com/ryanthestark/AI-For-Everyone/discussions)
- **Bug reports:** [Create an issue](https://github.com/ryanthestark/AI-For-Everyone/issues/new/choose)
- **Security concerns:** See [SECURITY.md](./SECURITY.md)

## 🌟 Recognition

All contributors are valued! We recognize contributions through:

- GitHub's built-in contributor tracking
- Acknowledgment in release notes
- Community highlights in discussions

## 📜 Code of Conduct

Be respectful, inclusive, and constructive. We're all here to learn and help each other.

Detailed Code of Conduct coming soon.

## 🔗 Additional Resources

- [AI Governance Guide](./docs/ai-governance.md) - How we use and label AI
- [Security Practices](./SECURITY.md) - Keep the repository safe
- [Documentation Hub](./docs/README.md) - All project documentation

---

**Thank you for contributing to AI-For-Everyone!** Your work helps make AI education accessible to everyone. 🚀

_This guide was created with AI assistance (Copilot Agent) to provide comprehensive contribution guidelines._
