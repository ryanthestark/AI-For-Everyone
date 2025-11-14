# Legal Case Multi-LLM Strategy Analysis

> ⚠️ **Note:** This directory is currently a placeholder for the Legal Case Multi-LLM Strategy Engine. The Python implementation files are not yet present in this repository.

## Overview

This directory is designed to contain a multi-LLM legal strategy analysis engine that uses OpenRouter to run multiple AI models in parallel for comprehensive legal case analysis.

## Run via GitHub Actions (Multi-LLM Strategy)

A GitHub Actions workflow has been configured to automate the multi-LLM legal strategy analysis.

### Prerequisites

1. Ensure the repository secret `OPENROUTER_API_KEY` is configured in GitHub Settings → Secrets and variables → Actions.
2. The following Python files must be present in `legal-case/analysis/`:
   - `run_multi_llm_strategy.py` - Main CLI entry point
   - `validate_outputs.py` - Output validation tool
   - Required modules in `llm_clients/`, `modules/`, and `prompts/` directories

### Running the Workflow

1. Navigate to the **Actions** tab in the GitHub repository
2. Select **"Legal Case – Multi-LLM Strategy"** from the workflows list
3. Click **"Run workflow"** button
4. Select the branch (usually `main` or your working branch)
5. Click the green **"Run workflow"** button to start

### After Completion

Once the workflow completes successfully:

1. Go to the workflow run page
2. Scroll down to the **Artifacts** section
3. Download the `legal-case-multi-llm-outputs` artifact (will be a .zip file)
4. Extract the archive to access your analysis results

### Key Output Files

The workflow generates several important files in `legal-case/analysis/outputs/`:

- **`final-master-strategy.md`** - ⭐ **Start here.** Primary human-readable legal strategy report with claim strength, damages ranges, and recommendations
- **`HUMAN_NEXT_STEPS.md`** - Quick guide explaining which files to review and in what order
- **`consensus.md`** / **`consensus.json`** - Areas where multiple AI models agree on legal strategy
- **`dissent.json`** - Areas of disagreement between models and remaining uncertainties
- **`summary_stats.json`** - Metadata about the analysis run
- **`models/*/*`** - Detailed per-model analysis outputs

### Cost Expectations

Multi-LLM analysis using OpenRouter will incur API costs. Refer to `IMPLEMENTATION_SUMMARY.md` (if present) for estimated costs per run.

## Expected Directory Structure

When fully implemented, this directory should contain:

```
legal-case/analysis/
├── run_multi_llm_strategy.py       # Main CLI entry point
├── validate_outputs.py             # Output validation tool
├── demo_system.py                  # Demo mode (no API calls)
├── README.md                       # This file
├── QUICKSTART.md                   # Quick start guide
├── llm_clients/
│   ├── base_client.py
│   └── openrouter_client.py
├── modules/
│   ├── strategy_engine.py
│   ├── consensus_builder.py
│   └── output_generator.py
├── prompts/
│   ├── round1_analysis.md
│   ├── round2_critique.md
│   ├── round3_debate.md
│   └── consensus_builder.md
├── data/
│   └── master-evidence.json       # Case evidence data
└── outputs/
    └── (generated files from analysis runs)
```

## Development Status

- [x] GitHub Actions workflow created (`.github/workflows/legal-case-multi-llm.yml`)
- [x] Documentation structure established
- [ ] Python implementation of multi-LLM strategy engine
- [ ] LLM client implementations (OpenRouter)
- [ ] Analysis modules (strategy, consensus, output generation)
- [ ] Prompt templates
- [ ] Evidence data files

## Contributing

When implementing the multi-LLM strategy engine:

1. **Do not modify** the GitHub Actions workflow unless necessary for compatibility
2. **Do not commit** API keys, tokens, or sensitive data
3. **Ensure** all outputs are written to `legal-case/analysis/outputs/`
4. **Follow** the expected file structure outlined above
5. **Test** locally before running via GitHub Actions to avoid unnecessary API costs

## Security

- Never commit the `OPENROUTER_API_KEY` or any API keys to the repository
- Use GitHub Secrets for all sensitive credentials
- Review the Security Policy in the root `SECURITY.md` file

## License

This project component is part of the AI-For-Everyone repository and is licensed under the MIT License.
