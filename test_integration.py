#!/usr/bin/env python3
"""
Test script for Webflow-BigCommerce Integration
"""

import os
import sys
import requests
from backend.api.bigcommerce_client import BigCommerceClient
from backend.api.webflow_client import WebflowClient

def test_bigcommerce_connection():
    """Test BigCommerce API connection"""
    print("Testing BigCommerce connection...")

    try:
        store_hash = os.environ.get('BIGCOMMERCE_STORE_HASH')
        access_token = os.environ.get('BIGCOMMERCE_ACCESS_TOKEN')

        if not store_hash or not access_token:
            print("❌ Missing BigCommerce credentials")
            return False

        client = BigCommerceClient(store_hash, access_token)
        products = client.get_products(limit=5)

        print(f"✅ Successfully connected to BigCommerce")
        print(f"   Found {len(products)} products")
        return True

    except Exception as e:
        print(f"❌ BigCommerce connection failed: {str(e)}")
        return False

def test_webflow_connection():
    """Test Webflow API connection"""
    print("\nTesting Webflow connection...")

    try:
        api_key = os.environ.get('WEBFLOW_API_KEY')
        site_id = os.environ.get('WEBFLOW_SITE_ID')

        if not api_key or not site_id:
            print("❌ Missing Webflow credentials")
            return False

        client = WebflowClient(api_key, site_id)
        collections = client.get_collections()

        print(f"✅ Successfully connected to Webflow")
        print(f"   Found {len(collections)} collections")
        return True

    except Exception as e:
        print(f"❌ Webflow connection failed: {str(e)}")
        return False

def test_backend_api():
    """Test backend API endpoints"""
    print("\nTesting Backend API...")

    try:
        # Test health check endpoint
        response = requests.get('http://localhost:5000/')
        if response.status_code == 200:
            print("✅ Backend API is running")
            return True
        else:
            print(f"❌ Backend API health check failed: {response.status_code}")
            return False

    except requests.exceptions.ConnectionError:
        print("❌ Backend API is not running. Start with: python backend/app.py")
        return False
    except Exception as e:
        print(f"❌ Backend API test failed: {str(e)}")
        return False

def main():
    """Run all tests"""
    print("Webflow-BigCommerce Integration Test Suite")
    print("=" * 40)

    tests = [
        test_bigcommerce_connection,
        test_webflow_connection,
        test_backend_api
    ]

    results = []
    for test in tests:
        results.append(test())

    print("\n" + "=" * 40)
    if all(results):
        print("🎉 All tests passed!")
        return 0
    else:
        print("💥 Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())