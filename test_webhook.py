#!/usr/bin/env python3
"""
Webhook testing script for development
"""

import requests
import json
from datetime import datetime

def test_bigcommerce_webhook():
    """Test BigCommerce webhook endpoint"""
    print("Testing BigCommerce webhook endpoint...")

    # Sample webhook payload
    payload = {
        "scope": "store/product/created",
        "data": {
            "id": 123,
            "name": "Test Product",
            "price": 29.99,
            "sku": "TEST-001"
        },
        "hash": "abc123",
        "created_at": datetime.now().isoformat(),
        "store_id": "store123"
    }

    try:
        # Send POST request to webhook endpoint
        response = requests.post(
            'http://localhost:5000/webhook/bigcommerce',
            json=payload,
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code == 200:
            print("✅ Webhook test successful!")
            print(f"Response: {response.json()}")
        else:
            print(f"❌ Webhook test failed with status {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Make sure the backend is running.")
    except Exception as e:
        print(f"❌ Webhook test failed: {str(e)}")

if __name__ == "__main__":
    test_bigcommerce_webhook()