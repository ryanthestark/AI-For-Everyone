# LLM Evaluation

## Purpose

This directory contains tools and documentation for systematically evaluating free and low-cost Large Language Model (LLM) solutions. The goal is to help non-technical users understand accessible AI options and make informed decisions about which tools best fit their needs.

## Why Evaluate LLMs?

With the growing number of free and affordable AI tools available, it's important to understand:
- **Quality**: How well does the model perform on different types of tasks?
- **Cost**: What's truly free vs. what has hidden costs or limitations?
- **Accessibility**: How easy is it to use for non-technical users?
- **Safety**: Is the output appropriate for family-friendly educational content?

## Methodology

Our evaluation approach focuses on practical, reproducible comparisons that anyone can understand:

### 1. Consistent Prompts
- We use the same set of prompts across all models
- Prompts are generic, family-friendly, and educational
- Prompts test different capabilities (creativity, explanation, helpfulness)

### 2. Fair Comparison
- All models tested under similar conditions
- Same input format and parameters when possible
- Clear documentation of any configuration differences

### 3. Reproducibility
- All prompts are saved in `prompts.py`
- Configuration details documented in results
- Code is open and can be run by others

### 4. Simple Metrics
- Qualitative assessment (human-readable comparisons)
- Response quality (accuracy, helpfulness, clarity)
- Cost tracking (free tier usage, API costs)
- Speed/latency (how long responses take)

## How to Use This Directory

### Setup
1. Install Python dependencies: `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and add any required API keys
3. Review the prompts in `prompts.py`

### Running Evaluations
```bash
python evaluate_llm.py
```

The script will:
- Load prompts from `prompts.py`
- Send them to configured LLM(s)
- Display responses
- Save results for comparison

### Viewing Results
- Check `results_comparison_*.md` files for documented comparisons
- Each file contains raw responses and qualitative analysis

## Available LLMs for Evaluation

This evaluation focuses on **free or low-cost options** suitable for educational use:

### Free Tier API Options
- **Hugging Face Inference API**: Free tier available for many open-source models
- **Ollama**: Run models locally (completely free, requires local compute)
- **GPT4All**: Desktop app for running models locally (free)

### Local Model Options
- Smaller models that can run on typical hardware
- No API keys required
- Complete privacy (everything stays on your computer)

## Current Evaluations

- `results_comparison_1.md`: First basic comparison of free LLM options

## Contributing

When adding new evaluations:
1. Use the existing `evaluate_llm.py` script or extend it
2. Document your methodology clearly
3. Include cost information
4. Keep content family-friendly and educational
5. Save results in a new `results_comparison_*.md` file

## Related Resources

- [Skill 2: Basic LLM Evaluation](../../skills/README.md) - Learn how to evaluate LLMs
- [AI Labs](../../ai-labs/) - Hands-on practice with AI
- [Free Tools Directory](../../tools/) - Other free AI tools

---

*This evaluation framework is designed to be educational and accessible to everyone, regardless of technical background.*
