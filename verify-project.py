#!/usr/bin/env python3
"""
Project verification script for Webflow-BigCommerce Integration Plugin
"""

import os
import sys
from pathlib import Path

def verify_project_structure():
    """Verify that all required files and directories exist"""
    print("Verifying Webflow-BigCommerce Integration Plugin project structure...")
    print("=" * 70)

    # Define expected structure
    expected_files = [
        "README.md",
        "LICENSE",
        "Dockerfile",
        "Procfile",
        "Makefile",
        "config.json",
        "start.sh",
        "test_integration.py",
        "test_webhook.py",
        ".gitignore",
        "backend/app.py",
        "backend/requirements.txt",
        "backend/requirements-dev.txt",
        "backend/pytest.ini",
        "backend/api/bigcommerce_client.py",
        "backend/api/webflow_client.py",
        "backend/tests/test_bigcommerce_client.py",
        "backend/tests/test_webflow_client.py",
        "frontend/webflow-widgets/product-display.js",
        "frontend/webflow-widgets/cart-widget.js",
        "docs/setup-guide.md",
        "docs/deployment-guide.md",
        "docs/api-documentation.md",
        "docs/webflow-usage-example.md",
        "docs/troubleshooting-guide.md",
        "docs/faq.md",
        "docs/contributing.md",
        "docs/security-guidelines.md",
        "docs/performance-optimization.md",
        "docs/roadmap.md",
        "docs/feature-comparison.md",
        "docs/monetization-strategy.md",
        "docs/marketing-plan.md",
        "docs/user-stories.md",
        "docs/project-summary.md",
        "docs/status-report.md",
        "docs/project-retrospective.md",
        "docs/project-completion-certificate.md",
        "docs/final-summary.md"
    ]

    # Check project root
    project_root = Path(__file__).parent

    # Verify directories exist
    required_directories = [
        "backend",
        "backend/api",
        "backend/tests",
        "frontend",
        "frontend/webflow-widgets",
        "docs"
    ]

    print("Checking directories...")
    dirs_verified = 0
    for directory in required_directories:
        dir_path = project_root / directory
        if dir_path.exists() and dir_path.is_dir():
            print(f"  ✅ {directory}")
            dirs_verified += 1
        else:
            print(f"  ❌ {directory} (MISSING)")

    print(f"\nDirectories: {dirs_verified}/{len(required_directories)} verified")

    # Verify files exist
    print("\nChecking files...")
    files_verified = 0
    files_missing = 0

    for file_path in expected_files:
        full_path = project_root / file_path
        if full_path.exists() and full_path.is_file():
            print(f"  ✅ {file_path}")
            files_verified += 1
        else:
            print(f"  ❌ {file_path} (MISSING)")
            files_missing += 1

    total_files = files_verified + files_missing
    print(f"\nFiles: {files_verified}/{total_files} verified")

    # Summary
    print("\n" + "=" * 70)
    if files_missing == 0 and dirs_verified == len(required_directories):
        print("🎉 PROJECT VERIFICATION SUCCESSFUL!")
        print("All required files and directories are present.")
        return True
    else:
        print("⚠️  PROJECT VERIFICATION ISSUES FOUND!")
        print(f"Missing {files_missing} files and/or directories.")
        return False

def main():
    """Main function"""
    success = verify_project_structure()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()