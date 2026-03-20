from flask import Flask, jsonify, request, send_from_directory
import os
from api.bigcommerce_client import BigCommerceClient
from api.webflow_client import WebflowClient

app = Flask(__name__)

# Configuration
BIGCOMMERCE_STORE_HASH = os.environ.get('BIGCOMMERCE_STORE_HASH')
BIGCOMMERCE_ACCESS_TOKEN = os.environ.get('BIGCOMMERCE_ACCESS_TOKEN')
WEBFLOW_API_KEY = os.environ.get('WEBFLOW_API_KEY')
WEBFLOW_SITE_ID = os.environ.get('WEBFLOW_SITE_ID')

# Initialize clients
bc_client = BigCommerceClient(BIGCOMMERCE_STORE_HASH, BIGCOMMERCE_ACCESS_TOKEN)
wf_client = WebflowClient(WEBFLOW_API_KEY, WEBFLOW_SITE_ID)

@app.route('/')
def hello():
    return jsonify({"message": "Webflow-BigCommerce Integration Plugin API"})

@app.route('/sync-products', methods=['POST'])
def sync_products():
    """Sync products from BigCommerce to Webflow CMS"""
    try:
        # Get products from BigCommerce
        bc_products = bc_client.get_products()

        # Transform and sync to Webflow CMS
        synced_count = 0
        for product in bc_products:
            # Transform BigCommerce product to Webflow CMS item
            wf_item = transform_bc_product_to_wf(product)

            # Create/update item in Webflow CMS
            wf_client.create_or_update_cms_item(wf_item)
            synced_count += 1

        return jsonify({
            "status": "success",
            "message": f"Synced {synced_count} products to Webflow"
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

def transform_bc_product_to_wf(bc_product):
    """Transform BigCommerce product data to Webflow CMS format"""
    return {
        "name": bc_product.get("name", ""),
        "slug": bc_product.get("custom_url", {}).get("url", ""),
        "price": bc_product.get("price", 0),
        "description": bc_product.get("description", ""),
        "images": [img.get("url_standard") for img in bc_product.get("images", [])],
        "inventory": bc_product.get("inventory_level", 0),
        "sku": bc_product.get("sku", ""),
        "brand": bc_product.get("brand", {}).get("name", ""),
        "categories": [cat.get("name") for cat in bc_product.get("categories", [])]
    }

@app.route('/webhook/bigcommerce', methods=['POST'])
def bigcommerce_webhook():
    """Handle BigCommerce webhooks for real-time updates"""
    try:
        data = request.get_json()
        event_type = data.get('scope')

        if event_type == 'store/product/created':
            # Handle product creation
            product_data = data.get('data')
            wf_item = transform_bc_product_to_wf(product_data)
            wf_client.create_or_update_cms_item(wf_item)

        elif event_type == 'store/product/updated':
            # Handle product update
            product_data = data.get('data')
            wf_item = transform_bc_product_to_wf(product_data)
            wf_client.create_or_update_cms_item(wf_item)

        elif event_type == 'store/product/deleted':
            # Handle product deletion
            product_id = data.get('data', {}).get('id')
            wf_client.delete_cms_item_by_bc_id(product_id)

        return jsonify({"status": "received"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    """Add item to BigCommerce cart"""
    try:
        data = request.get_json()
        cart_id = data.get('cart_id')
        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)

        # Add item to cart using BigCommerce API
        result = bc_client.add_to_cart(cart_id, product_id, quantity)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/checkout-url', methods=['POST'])
def get_checkout_url():
    """Get BigCommerce checkout URL for cart"""
    try:
        data = request.get_json()
        cart_id = data.get('cart_id')

        # Get checkout URL from BigCommerce
        checkout_url = bc_client.get_checkout_url(cart_id)
        return jsonify({"checkout_url": checkout_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files from frontend directory"""
    return send_from_directory('../frontend/webflow-widgets', filename)

@app.route('/create-cart', methods=['POST'])
def create_cart():
    """Create a new BigCommerce cart"""
    try:
        cart = bc_client.create_cart()
        return jsonify(cart)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cart/<cart_id>')
def get_cart(cart_id):
    """Get BigCommerce cart details"""
    try:
        cart = bc_client.get_cart(cart_id)
        return jsonify(cart)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cart/<cart_id>/items/<item_id>', methods=['PUT'])
def update_cart_item(cart_id, item_id):
    """Update item quantity in cart"""
    try:
        data = request.get_json()
        quantity = data.get('quantity', 1)

        # Update item in cart
        result = bc_client.update_cart_item(cart_id, item_id, quantity)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cart/<cart_id>/items/<item_id>', methods=['DELETE'])
def remove_cart_item(cart_id, item_id):
    """Remove item from cart"""
    try:
        # Remove item from cart
        result = bc_client.remove_cart_item(cart_id, item_id)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))