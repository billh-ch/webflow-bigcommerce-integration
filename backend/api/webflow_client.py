import requests
import os

class WebflowClient:
    def __init__(self, api_key, site_id):
        self.api_key = api_key
        self.site_id = site_id
        self.base_url = "https://api.webflow.com"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def get_collections(self):
        """Get all collections in Webflow site"""
        url = f"{self.base_url}/sites/{self.site_id}/collections"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json().get("collections", [])

    def get_collection_items(self, collection_id):
        """Get items in a specific collection"""
        url = f"{self.base_url}/collections/{collection_id}/items"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json().get("items", [])

    def create_cms_item(self, collection_id, fields):
        """Create a new item in Webflow CMS"""
        url = f"{self.base_url}/collections/{collection_id}/items"
        payload = {"fields": fields}

        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def update_cms_item(self, collection_id, item_id, fields):
        """Update an existing item in Webflow CMS"""
        url = f"{self.base_url}/collections/{collection_id}/items/{item_id}"
        payload = {"fields": fields}

        response = requests.put(url, headers=self.headers, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_cms_item(self, collection_id, item_id):
        """Delete an item from Webflow CMS"""
        url = f"{self.base_url}/collections/{collection_id}/items/{item_id}"
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
        return {"status": "deleted"}

    def create_or_update_cms_item(self, fields):
        """Create or update item based on BigCommerce product ID"""
        # This is a simplified implementation
        # In practice, you would need to map BigCommerce product IDs to Webflow item IDs
        # For now, we'll just create new items
        collections = self.get_collections()
        products_collection = None

        # Find the products collection (you might want to configure this)
        for collection in collections:
            if collection.get("name", "").lower() == "products":
                products_collection = collection
                break

        if products_collection:
            return self.create_cms_item(products_collection["_id"], fields)
        else:
            raise Exception("Products collection not found in Webflow")

    def delete_cms_item_by_bc_id(self, bc_product_id):
        """Delete Webflow CMS item by BigCommerce product ID"""
        # This would require maintaining a mapping between BC and Webflow IDs
        # Simplified implementation for now
        return {"status": "not implemented"}