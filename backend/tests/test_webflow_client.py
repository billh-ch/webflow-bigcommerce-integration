import pytest
from unittest.mock import Mock, patch
from api.webflow_client import WebflowClient

class TestWebflowClient:
    def setup_method(self):
        """Set up test fixtures"""
        self.client = WebflowClient("test_api_key", "test_site_id")

    def test_init(self):
        """Test client initialization"""
        assert self.client.api_key == "test_api_key"
        assert self.client.site_id == "test_site_id"
        assert self.client.base_url == "https://api.webflow.com"

    @patch('api.webflow_client.requests.get')
    def test_get_collections(self, mock_get):
        """Test get_collections method"""
        # Mock response
        mock_response = Mock()
        mock_response.json.return_value = {"collections": [{"id": "1", "name": "Products"}]}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Call method
        collections = self.client.get_collections()

        # Assertions
        assert len(collections) == 1
        assert collections[0]["name"] == "Products"
        mock_get.assert_called_once_with(
            "https://api.webflow.com/sites/test_site_id/collections",
            headers={
                "Authorization": "Bearer test_api_key",
                "Content-Type": "application/json"
            }
        )