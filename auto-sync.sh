#!/bin/bash
# Auto-sync script for Webflow-BigCommerce Integration Plugin

# Function to sync changes to GitHub
sync_to_github() {
    echo "🔍 Checking for changes..."

    # Check if there are any changes
    if [[ -z $(git status -s) ]]; then
        echo "✅ No changes to commit"
        return 0
    fi

    # Get the changes summary
    CHANGES=$(git status -s)
    echo "📝 Changes detected:"
    echo "$CHANGES"

    # Ask for commit message
    echo ""
    read -p "Enter commit message: " COMMIT_MESSAGE

    if [[ -z "$COMMIT_MESSAGE" ]]; then
        COMMIT_MESSAGE="Update files"
    fi

    # Add all changes
    echo "➕ Adding changes..."
    git add --all

    # Commit changes
    echo "💾 Committing changes..."
    git commit -m "$COMMIT_MESSAGE"

    # Push to GitHub
    echo "📤 Pushing to GitHub..."
    git push origin main

    echo "✅ Changes successfully synced to GitHub!"
    echo "🔗 Repository: https://github.com/billh-ch/webflow-bigcommerce-integration"
}

# Run the sync function
sync_to_github