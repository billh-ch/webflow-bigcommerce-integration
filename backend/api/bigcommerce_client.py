import requests
import os

class BigCommerceClient:
    def __init__(self, store_hash, access_token):
        self.store_hash = store_hash
        self.access_token = access_token
        self.base_url = f"https://api.bigcommerce.com/stores/{store_hash}"
        self.headers = {
            "X-Auth-Token": access_token,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_products(self, limit=50):
        """Get products from BigCommerce"""
        url = f"{self.base_url}/v3/catalog/products"
        params = {
            "limit": limit,
            "include": "images,variants,custom_fields,primary_image,modifiers,category_ids,categories,brand"
        }

        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json().get("data", [])

    def get_product(self, product_id):
        """Get a specific product by ID"""
        url = f"{self.base_url}/v3/catalog/products/{product_id}"
        params = {
            "include": "images,variants,custom_fields,primary_image,modifiers,category_ids,categories,brand"
        }

        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json().get("data", {})

    def add_to_cart(self, cart_id, product_id, quantity=1):
        """Add item to BigCommerce cart"""
        url = f"{self.base_url}/v3/carts/{cart_id}/items"
        payload = {
            "line_items": [
                {
                    "product_id": product_id,
                    "quantity": quantity
                }
            ]
        }

        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def create_cart(self):
        """Create a new BigCommerce cart"""
        url = f"{self.base_url}/v3/carts"
        payload = {"line_items": []}

        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def get_cart(self, cart_id):
        """Get BigCommerce cart details"""
        url = f"{self.base_url}/v3/carts/{cart_id}"

        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_cart_item(self, cart_id, item_id, quantity):
        """Update item quantity in cart"""
        url = f"{self.base_url}/v3/carts/{cart_id}/items/{item_id}"
        payload = {"quantity": quantity}

        response = requests.put(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def remove_cart_item(self, cart_id, item_id):
        """Remove item from cart"""
        url = f"{self.base_url}/v3/carts/{cart_id}/items/{item_id}"

        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
        return {"status": "removed"}

    def get_checkout_url(self, cart_id):
        """Get checkout URL for cart"""
        url = f"{self.base_url}/v3/checkouts"
        payload = {"cart_id": cart_id}

        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        checkout_data = response.json()
        return checkout_data.get("data", {}).get("checkout_url", "")