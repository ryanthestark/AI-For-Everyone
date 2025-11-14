"""
Generic, family-friendly, educational prompts for LLM evaluation.

These prompts test different aspects of LLM capabilities:
- Creativity (jokes, stories)
- Explanation (teaching concepts)
- Helpfulness (practical suggestions)
- Reasoning (problem-solving)
"""

# List of prompts to use for evaluation
EVALUATION_PROMPTS = [
    {
        "id": "joke",
        "category": "creativity",
        "prompt": "Tell me a joke.",
        "description": "Tests creative and humorous output"
    },
    {
        "id": "star_explanation",
        "category": "explanation",
        "prompt": "Explain what a star is to a 5-year-old.",
        "description": "Tests ability to simplify complex concepts"
    },
    {
        "id": "rainy_day_activity",
        "category": "helpfulness",
        "prompt": "Suggest a fun activity for a rainy day.",
        "description": "Tests practical suggestion generation"
    },
    {
        "id": "healthy_snack",
        "category": "helpfulness",
        "prompt": "What's a healthy snack I can make in 5 minutes?",
        "description": "Tests practical advice with constraints"
    },
    {
        "id": "learning_tips",
        "category": "explanation",
        "prompt": "Give me 3 tips for learning something new.",
        "description": "Tests educational advice generation"
    }
]


def get_prompts():
    """Return the list of evaluation prompts."""
    return EVALUATION_PROMPTS


def get_prompt_by_id(prompt_id):
    """Get a specific prompt by its ID."""
    for prompt in EVALUATION_PROMPTS:
        if prompt["id"] == prompt_id:
            return prompt
    return None


def get_prompts_by_category(category):
    """Get all prompts in a specific category."""
    return [p for p in EVALUATION_PROMPTS if p["category"] == category]


if __name__ == "__main__":
    # Simple test to display all prompts
    print("Available Evaluation Prompts:")
    print("=" * 60)
    for prompt in EVALUATION_PROMPTS:
        print(f"\nID: {prompt['id']}")
        print(f"Category: {prompt['category']}")
        print(f"Prompt: {prompt['prompt']}")
        print(f"Description: {prompt['description']}")
