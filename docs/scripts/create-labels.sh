#!/bin/bash
# Script to create labels in the repository based on labels.json
# This should be run by a repository administrator with appropriate permissions

set -e

REPO_OWNER="ryanthestark"
REPO_NAME="AI-For-Everyone"
LABELS_FILE=".github/labels.json"

echo "🏷️  Creating labels for $REPO_OWNER/$REPO_NAME"
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed."
    echo "Please install it from: https://cli.github.com/"
    exit 1
fi

# Check if user is authenticated
if ! gh auth status &> /dev/null; then
    echo "❌ Not authenticated with GitHub CLI"
    echo "Please run: gh auth login"
    exit 1
fi

# Parse and create labels
jq -c '.[]' "$LABELS_FILE" | while read -r label; do
    name=$(echo "$label" | jq -r '.name')
    color=$(echo "$label" | jq -r '.color')
    description=$(echo "$label" | jq -r '.description')
    
    echo "Creating label: $name"
    
    # Try to create or update the label
    gh label create "$name" \
        --repo "$REPO_OWNER/$REPO_NAME" \
        --color "$color" \
        --description "$description" \
        --force 2>/dev/null || echo "  ⚠️  Label may already exist (this is OK)"
done

echo ""
echo "✅ Label creation complete!"
echo "View labels at: https://github.com/$REPO_OWNER/$REPO_NAME/labels"
