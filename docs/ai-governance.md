# AI Governance in AI-For-Everyone

## Overview

This document explains how we use AI tools in the AI-For-Everyone project, how to attribute AI assistance transparently, and why this matters for our educational mission.

## Our Philosophy

**Transparency + Education = Better AI Adoption**

The AI-For-Everyone project embraces AI tools while maintaining transparency about when and how they're used. This approach:

- **Builds trust** through honest attribution
- **Enables learning** by showing real-world AI usage patterns
- **Improves reproducibility** by documenting which tools helped create what
- **Creates searchable history** of AI-assisted contributions
- **Demonstrates best practices** for responsible AI use

## How We Use AI

AI tools are welcome and encouraged in this project across all activities:

### Planning & Ideation
- ChatGPT, Claude, or other LLMs for brainstorming
- AI assistance in structuring issues or proposals
- Exploring different approaches to problems

### Implementation
- GitHub Copilot for code completion and suggestions
- Copilot Agent for automated implementation tasks
- AI-powered refactoring and code generation

### Documentation
- AI assistance in writing clear, accessible documentation
- Translation and localization help
- Improving readability and structure

### Review & Quality
- Multi-model review (getting feedback from multiple AI tools)
- AI-assisted testing and debugging
- Code quality analysis

## AI Label Taxonomy

We use a structured set of labels to track AI usage:

### AI Tool Labels

| Label | Purpose | When to Use |
|-------|---------|-------------|
| `ai:chatgpt` | ChatGPT assistance | When ChatGPT helped with planning, wording, or problem-solving |
| `ai:copilot-editor` | GitHub Copilot in editor | When Copilot provided code completions or suggestions |
| `ai:copilot-agent` | Copilot Agent automation | When Copilot Agent performed automated implementation |
| `ai:multi-model-review` | Multiple AI models | When you got feedback from 2+ different AI tools |
| `meta:ai-assisted` | General AI assistance | When you used AI but the specific tool isn't listed |

### Other Relevant Labels

| Label | Purpose |
|-------|---------|
| `content` | Educational content or lessons |
| `ai-for-everyone` | Related to core educational initiative |
| `meta` | Project governance or processes |
| `process` | Workflow improvements |

## How to Attribute AI Assistance

### In Issues

Our issue templates include an **AI Assistance** section with checkboxes:

```markdown
### AI Assistance (optional)

- [ ] ChatGPT (planning / wording)
- [ ] GitHub Copilot (editor)
- [ ] Copilot Agent (automation)
- [ ] Other AI tool (please specify)
```

**Check the boxes that apply** when creating your issue. Our automation will apply the appropriate labels.

### In Pull Requests

Similarly, our PR template includes:

```markdown
## AI Assistance

- [ ] ChatGPT (planning / problem-solving)
- [ ] GitHub Copilot (code completion in editor)
- [ ] Copilot Agent (automated implementation)
- [ ] Other AI tool: ____________________
```

**Optional but encouraged:** Add a brief note about how AI helped:

```markdown
_AI assistance: ChatGPT helped design the API interface, 
Copilot Agent generated the boilerplate code, manual review and refinement done by human._
```

### In Comments

For comments on issues or PRs, use the footer convention:

```markdown
_AI assistance: ChatGPT (drafting), manual editing for tone and accuracy_
```

## Automation

We have lightweight automation in place to make attribution easier:

### Auto-Labeling

When you create or edit an issue/PR, our GitHub Action automatically:
- Scans the body text for AI tool mentions
- Applies relevant `ai:*` labels when detected
- Works with both checkboxes and text mentions

**What triggers labels:**
- ✅ Checking AI tool checkboxes in templates
- ✅ Mentioning tools by name (e.g., "ChatGPT", "Copilot Agent")
- ✅ Using the footer format: `_AI assistance: ..._`

### Template Reminders

If an issue or PR is created without using our templates:
- A friendly bot comment suggests using the appropriate template
- **This is just a reminder** - not enforced
- No action required if you've provided sufficient detail

## Why This Matters

### For Contributors
- **Honesty is respected** - we want to know when AI helped
- **No penalty** for using AI tools
- **Learn from each other** - see how others use AI effectively

### For Learners
- **Real examples** of AI-assisted development
- **Searchable patterns** - find issues/PRs by AI tool used
- **Transparency** in how modern development works
- **Best practices** demonstrated in action

### For the Project
- **Better collaboration** - knowing how contributions were created
- **Quality insights** - understanding which AI tools work well for what
- **Educational value** - our process is part of the curriculum
- **Reproducibility** - others can follow similar approaches

## Examples

### Example 1: Feature Request with ChatGPT

```markdown
### AI Assistance (optional)

- [x] ChatGPT (planning / wording)
- [ ] GitHub Copilot (editor)
- [ ] Copilot Agent (automation)
- [ ] Other AI tool
```

**Result:** Issue automatically gets the `ai:chatgpt` label.

### Example 2: PR with Multiple AI Tools

```markdown
## AI Assistance

- [x] ChatGPT (planning / problem-solving)
- [x] GitHub Copilot (code completion in editor)
- [x] Copilot Agent (automated implementation)
- [ ] Other AI tool: ____________________

_AI assistance: ChatGPT helped break down the problem into steps, 
Copilot Agent implemented the initial solution, Copilot provided 
code completions during manual refinement._
```

**Result:** PR gets labels: `ai:chatgpt`, `ai:copilot-editor`, `ai:copilot-agent`, and `meta:ai-assisted`.

### Example 3: Comment with AI Assistance

```markdown
Here's my feedback on the proposed approach...

[detailed technical feedback]

_AI assistance: ChatGPT helped structure this response and check technical accuracy_
```

## Best Practices

### ✅ DO:
- Be honest about AI usage
- Use templates when creating issues/PRs
- Check relevant AI assistance boxes
- Add context about how AI helped (optional but valuable)
- Update labels if you use AI tools during iteration

### ❌ DON'T:
- Claim AI-generated content as entirely your own
- Worry about "using too much AI" - all levels are welcome
- Skip attribution to save time - it's quick with templates!
- Assume AI labels mean lower quality - transparency ≠ inferior

## Getting Started

1. **Creating an Issue:** Go to Issues → New Issue → Choose a template
2. **Creating a PR:** Our template loads automatically when you create a PR
3. **Adding Labels:** If automation misses something, manually add `ai:*` labels
4. **Learning More:** Check out our [AI for Everyone lessons](../README.md)

## Questions?

- **General questions:** Use [GitHub Discussions](https://github.com/ryanthestark/AI-For-Everyone/discussions)
- **Process improvements:** Create an issue with the "Meta / Process" template
- **Found a bug in automation:** File a bug report

## Future Enhancements

We're considering:
- Per-lesson AI usage metadata
- Advanced analytics and insights
- Integration with learning materials
- Community showcase of great AI-assisted contributions

Want to help? Check issues labeled `meta` and `process`!

---

**Last Updated:** November 2025  
**Maintained by:** AI-For-Everyone Community  
**License:** See repository LICENSE file

_This document was created with AI assistance (Copilot Agent) and refined by human maintainers._
