import pytest
from unittest.mock import Mock, patch
from api.bigcommerce_client import BigCommerceClient

class TestBigCommerceClient:
    def setup_method(self):
        """Set up test fixtures"""
        self.client = BigCommerceClient("test_store_hash", "test_access_token")

    def test_init(self):
        """Test client initialization"""
        assert self.client.store_hash == "test_store_hash"
        assert self.client.access_token == "test_access_token"
        assert self.client.base_url == "https://api.bigcommerce.com/stores/test_store_hash"

    @patch('api.bigcommerce_client.requests.get')
    def test_get_products(self, mock_get):
        """Test get_products method"""
        # Mock response
        mock_response = Mock()
        mock_response.json.return_value = {"data": [{"id": 1, "name": "Test Product"}]}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Call method
        products = self.client.get_products(limit=10)

        # Assertions
        assert len(products) == 1
        assert products[0]["name"] == "Test Product"
        mock_get.assert_called_once_with(
            "https://api.bigcommerce.com/stores/test_store_hash/v3/catalog/products",
            headers={
                "X-Auth-Token": "test_access_token",
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            params={
                "limit": 10,
                "include": "images,variants,custom_fields,primary_image,modifiers,category_ids,categories,brand"
            }
        )

    @patch('api.bigcommerce_client.requests.get')
    def test_get_product(self, mock_get):
        """Test get_product method"""
        # Mock response
        mock_response = Mock()
        mock_response.json.return_value = {"data": {"id": 1, "name": "Test Product"}}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Call method
        product = self.client.get_product(1)

        # Assertions
        assert product["name"] == "Test Product"
        mock_get.assert_called_once_with(
            "https://api.bigcommerce.com/stores/test_store_hash/v3/catalog/products/1",
            headers={
                "X-Auth-Token": "test_access_token",
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            params={
                "include": "images,variants,custom_fields,primary_image,modifiers,category_ids,categories,brand"
            }
        )