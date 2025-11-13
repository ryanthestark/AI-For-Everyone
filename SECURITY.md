# Security Practices for AI-For-Everyone

## 🔒 Overview

**AI-For-Everyone is a PUBLIC repository** - anyone on the internet can view all code, comments, and history. This document explains how we keep our community safe while working in the open.

## 🎯 Our Security Philosophy

This repository uses **lightweight, educational security guardrails** designed to:

- **Prevent accidents** - Catch secrets and PII before they're committed
- **Teach best practices** - Learn safe public development habits
- **Stay simple** - No complex enterprise security setups
- **Empower contributors** - Clear guidance on what to do when issues arise

These guardrails are intentionally educational. They demonstrate good practices without creating barriers to contribution.

## 🚫 What NOT to Commit

### Never Commit Secrets

**Examples of secrets that must NOT be committed:**

- API keys and tokens (OpenAI, GitHub, AWS, etc.)
- Passwords or password hashes
- Private SSH keys or certificates
- OAuth tokens or client secrets
- Database connection strings with credentials
- Encryption keys or secrets

**Why?** Once committed to a public repo, secrets are permanently visible in the Git history, even if you delete them later. Bad actors scan GitHub constantly for exposed credentials.

### Avoid Committing Personal Information (PII)

**Examples of PII to avoid:**

- Real full names of minors or students
- Home addresses or precise locations
- Phone numbers
- Social Security Numbers (SSNs) or other national IDs
- Email addresses (in code - README contact info is fine)
- Photos or videos of individuals without consent
- Private health or financial information

**Why?** This is an educational project. Protecting privacy, especially for learners, is paramount.

## ✅ What Our Security Checks Do

We have automated checks running on every pull request:

### 1. Secret Scanning (Gitleaks)

**What it does:**
- Scans all code changes for high-confidence secrets
- Detects patterns like API keys, tokens, and private keys
- **BLOCKS the PR** if secrets are detected

**Technology:** [Gitleaks](https://github.com/gitleaks/gitleaks) - industry-standard open-source tool

**What to expect:**
- Runs automatically on every PR
- Takes 10-30 seconds typically
- Fails with clear error messages if secrets found

### 2. Content Hygiene Check

**What it does:**
- Scans for PII patterns (SSNs, phone numbers, etc.)
- Checks for hardcoded passwords or credentials
- Looks for suspicious content patterns

**What to expect:**
- Runs automatically on every PR
- **WARNS but does NOT block** the PR
- You should review warnings and fix real issues

**Current patterns checked:**
- Hardcoded passwords (`password = "..."`)
- AWS secret keys
- Private key markers (`-----BEGIN PRIVATE KEY-----`)
- US SSN patterns (XXX-XX-XXXX)
- US phone numbers
- Email addresses in code files

## 🆘 What to Do If You Accidentally Commit a Secret

**Don't panic!** This happens. Here's what to do:

### Immediate Actions

1. **Rotate/Invalidate the secret IMMEDIATELY**
   - Go to the service (GitHub, OpenAI, AWS, etc.)
   - Regenerate/rotate the key or token
   - The old secret is now useless to attackers

2. **Remove the secret from your code**
   - Replace it with an environment variable
   - Use a configuration file (not committed)
   - Update your `.gitignore` if needed

3. **Update your PR**
   - Push the changes
   - The security check will re-run

### If the Secret Was Already Merged

If the secret made it to the main branch:

1. **Invalidate the secret immediately** (same as above)
2. **Contact a maintainer** via GitHub Issues or Discussions
3. **We'll help** with history rewriting if needed (BFG, git filter-repo)

**Important:** Simply deleting a file or removing a line does NOT remove it from Git history. The secret remains visible in old commits.

### Resources

- [GitHub: Removing sensitive data](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository)
- [Gitleaks Documentation](https://github.com/gitleaks/gitleaks)

## 🛡️ Best Practices for Safe Public Development

### Use Environment Variables

**Instead of:**
```python
api_key = "sk-abc123..."  # ❌ NEVER
openai.api_key = api_key
```

**Do this:**
```python
import os
api_key = os.getenv("OPENAI_API_KEY")  # ✅ Good
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")
```

### Use Configuration Files (Not Committed)

Create a `.env` file for secrets (add to `.gitignore`):

```bash
# .env (NOT committed)
OPENAI_API_KEY=sk-abc123...
DATABASE_URL=postgresql://user:pass@localhost/db
```

Load it in your code:
```python
from dotenv import load_dotenv
load_dotenv()  # Reads .env file
```

**Make sure `.env` is in `.gitignore`!**

### Use Example/Template Files

Commit a template, not real values:

```bash
# .env.example (this IS committed)
OPENAI_API_KEY=your_key_here
DATABASE_URL=your_database_url
```

Contributors copy `.env.example` to `.env` and fill in their own values.

### Anonymize Learning Materials

When creating examples or lessons:

- Use placeholder names: "Student A", "Learner B"
- Use example.com for domains
- Use fake data generators for realistic examples
- Get explicit consent before using real names or data

## 🔧 Optional: Local Pre-Commit Hooks

For an extra safety layer, install pre-commit hooks that check your code **before** you commit:

### Installation

```bash
# Install pre-commit
pip install pre-commit

# Install the hooks in this repo
cd AI-For-Everyone
pre-commit install
```

### What Happens

Now, every time you run `git commit`:

1. **Gitleaks scans** your staged changes for secrets
2. **Content hygiene checks** run on your files
3. **Basic file checks** (file size, trailing whitespace, etc.)

If issues are found, the commit is blocked and you can fix them.

### Running Manually

```bash
# Check all files
pre-commit run --all-files

# Check specific files
pre-commit run --files path/to/file.py
```

### This is Optional

Pre-commit hooks are **recommended but not required**. The CI checks will catch issues anyway, but local hooks save time by catching them earlier.

## 🤝 Reporting Security Issues

### For General Security Concerns

Open an issue using our templates, or start a discussion.

### For Sensitive Security Issues

If you discover a vulnerability or serious security issue:

**Do NOT open a public issue.**

Instead:
1. Email the maintainers (see README for contact)
2. Or use [GitHub Security Advisories](https://github.com/ryanthestark/AI-For-Everyone/security/advisories) (if enabled)

We'll work with you privately to address the issue.

## 📚 Educational Value

These security practices are part of the learning experience:

- **For beginners**: Learn safe development habits early
- **For educators**: See a real-world example of security automation
- **For everyone**: Understand why and how to work safely in public

We intentionally keep this setup simple and transparent so it can serve as an educational reference.

## ❓ FAQ

### Q: Why not use a heavier security solution?

**A:** This is an educational project. We want security that's:
- Easy to understand
- Easy to maintain
- Not intimidating to beginners
- Open source and transparent

Enterprise-grade security would be overkill and create barriers to contribution.

### Q: Are these checks perfect?

**A:** No. They catch common mistakes but aren't exhaustive. Use common sense:
- If it looks sensitive, don't commit it
- When in doubt, ask in Discussions
- Think before you commit

### Q: What if I get a false positive?

**A:** For Gitleaks:
- Add the false positive to `.gitleaksignore`
- Document why it's safe in a comment

For content hygiene warnings:
- Review them carefully
- If it's truly safe, you can ignore the warning (it doesn't block)

### Q: Can I opt out of the checks?

**A:** No. All PRs must pass secret scanning. This is a basic safety requirement for a public educational repository.

Content hygiene checks only warn and don't block.

## 🔗 Additional Resources

- [OWASP: Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
- [GitHub: Security Best Practices](https://docs.github.com/en/code-security)
- [Gitleaks Documentation](https://github.com/gitleaks/gitleaks)
- [Pre-commit Framework](https://pre-commit.com/)

## 📝 Document History

- **Created:** November 2024
- **Purpose:** Establish lightweight security guardrails for public educational repository
- **Maintained by:** AI-For-Everyone Community

---

**Remember:** Security is everyone's responsibility. When you see something, say something. Let's keep our community safe! 🛡️

_This document was created with AI assistance (Copilot Agent) to ensure comprehensive coverage of security best practices._
