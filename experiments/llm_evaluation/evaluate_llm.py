"""
LLM Evaluation Script

This script evaluates free/low-cost LLMs by sending prompts and collecting responses.
It supports multiple LLM backends and can be easily extended.

Usage:
    python evaluate_llm.py [--model MODEL_NAME] [--all-prompts]
"""

import os
import sys
import time
import json
import argparse
from datetime import datetime
from dotenv import load_dotenv
import requests

# Import our prompts
from prompts import get_prompts, get_prompt_by_id


class LLMEvaluator:
    """Base class for LLM evaluation."""
    
    def __init__(self, model_name="default"):
        """Initialize the evaluator."""
        self.model_name = model_name
        load_dotenv()  # Load environment variables from .env file
    
    def evaluate(self, prompt_text):
        """
        Evaluate a single prompt and return the response.
        
        Args:
            prompt_text (str): The prompt to send to the LLM
            
        Returns:
            dict: Contains 'response', 'latency', 'error' (if any)
        """
        raise NotImplementedError("Subclasses must implement evaluate()")
    
    def format_result(self, prompt_info, result):
        """Format the evaluation result for display."""
        output = []
        output.append(f"\n{'='*70}")
        output.append(f"Prompt ID: {prompt_info['id']}")
        output.append(f"Category: {prompt_info['category']}")
        output.append(f"Prompt: {prompt_info['prompt']}")
        output.append(f"Model: {self.model_name}")
        output.append(f"{'-'*70}")
        
        if result.get('error'):
            output.append(f"ERROR: {result['error']}")
        else:
            output.append(f"Response:\n{result['response']}")
            output.append(f"\nLatency: {result.get('latency', 0):.2f}s")
        
        output.append(f"{'='*70}")
        return "\n".join(output)


class HuggingFaceEvaluator(LLMEvaluator):
    """Evaluator using Hugging Face Inference API (free tier)."""
    
    def __init__(self, model_name="mistralai/Mistral-7B-Instruct-v0.1"):
        """Initialize with Hugging Face model."""
        super().__init__(model_name)
        self.api_token = os.getenv("HUGGINGFACE_API_TOKEN")
        self.api_url = f"https://api-inference.huggingface.co/models/{model_name}"
        
        if not self.api_token:
            print("⚠️  Warning: HUGGINGFACE_API_TOKEN not set. Using public (rate-limited) access.")
            print("   Get a free token at: https://huggingface.co/settings/tokens")
    
    def evaluate(self, prompt_text):
        """Send prompt to Hugging Face API and get response."""
        headers = {}
        if self.api_token:
            headers["Authorization"] = f"Bearer {self.api_token}"
        
        payload = {
            "inputs": prompt_text,
            "parameters": {
                "max_new_tokens": 200,
                "temperature": 0.7,
                "return_full_text": False
            }
        }
        
        start_time = time.time()
        
        try:
            response = requests.post(
                self.api_url,
                headers=headers,
                json=payload,
                timeout=30
            )
            latency = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                
                # Handle different response formats
                if isinstance(result, list) and len(result) > 0:
                    text = result[0].get("generated_text", "")
                elif isinstance(result, dict):
                    text = result.get("generated_text", "")
                else:
                    text = str(result)
                
                return {
                    "response": text.strip(),
                    "latency": latency,
                    "error": None
                }
            else:
                return {
                    "response": None,
                    "latency": latency,
                    "error": f"API returned status {response.status_code}: {response.text}"
                }
        
        except requests.exceptions.RequestException as e:
            latency = time.time() - start_time
            return {
                "response": None,
                "latency": latency,
                "error": f"Request failed: {str(e)}"
            }


class MockLLMEvaluator(LLMEvaluator):
    """
    Mock evaluator for testing without API access.
    Returns simulated responses based on prompt category.
    """
    
    def __init__(self, model_name="mock-model"):
        """Initialize mock evaluator."""
        super().__init__(model_name)
        
        # Predefined responses for different categories
        self.responses = {
            "creativity": "Here's a creative response! I can generate jokes, stories, and fun content.",
            "explanation": "Let me explain this in simple terms that anyone can understand. It's like...",
            "helpfulness": "Here's a helpful suggestion: Try doing something fun and practical!",
            "default": "This is a simulated response from a mock LLM. In real usage, this would come from an actual language model."
        }
    
    def evaluate(self, prompt_text):
        """Return a mock response."""
        # Simulate some processing time
        time.sleep(0.5)
        
        # Simple keyword matching to pick response type
        response = self.responses["default"]
        
        if "joke" in prompt_text.lower() or "fun" in prompt_text.lower():
            response = self.responses["creativity"]
        elif "explain" in prompt_text.lower():
            response = self.responses["explanation"]
        elif "suggest" in prompt_text.lower() or "tip" in prompt_text.lower():
            response = self.responses["helpfulness"]
        
        return {
            "response": response,
            "latency": 0.5,
            "error": None
        }


def main():
    """Main evaluation function."""
    parser = argparse.ArgumentParser(
        description="Evaluate LLMs using standardized prompts"
    )
    parser.add_argument(
        "--model",
        choices=["huggingface", "mock"],
        default="mock",
        help="Which LLM backend to use (default: mock)"
    )
    parser.add_argument(
        "--all-prompts",
        action="store_true",
        help="Run all prompts (default: run first 3)"
    )
    parser.add_argument(
        "--output",
        help="Save results to a file"
    )
    
    args = parser.parse_args()
    
    # Create appropriate evaluator
    if args.model == "huggingface":
        print("🤖 Using Hugging Face Inference API...")
        evaluator = HuggingFaceEvaluator()
    else:
        print("🤖 Using Mock LLM (for testing without API access)...")
        evaluator = MockLLMEvaluator()
    
    # Get prompts to evaluate
    all_prompts = get_prompts()
    prompts_to_run = all_prompts if args.all_prompts else all_prompts[:3]
    
    print(f"\n📝 Running {len(prompts_to_run)} prompt(s)...\n")
    
    # Store results
    results = []
    
    # Run each prompt
    for prompt_info in prompts_to_run:
        print(f"Testing: {prompt_info['id']}...")
        
        result = evaluator.evaluate(prompt_info['prompt'])
        results.append({
            "prompt": prompt_info,
            "result": result
        })
        
        # Display result
        print(evaluator.format_result(prompt_info, result))
        
        # Brief pause between requests to be nice to APIs
        time.sleep(1)
    
    # Summary
    print("\n" + "="*70)
    print("📊 EVALUATION SUMMARY")
    print("="*70)
    print(f"Model: {evaluator.model_name}")
    print(f"Prompts tested: {len(results)}")
    
    successful = sum(1 for r in results if not r['result'].get('error'))
    print(f"Successful: {successful}/{len(results)}")
    
    if successful > 0:
        avg_latency = sum(
            r['result']['latency'] for r in results 
            if not r['result'].get('error')
        ) / successful
        print(f"Average latency: {avg_latency:.2f}s")
    
    print(f"\n💰 Cost: $0.00 (using free tier/mock)")
    print("="*70)
    
    # Save to file if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n✅ Results saved to: {args.output}")


if __name__ == "__main__":
    main()
