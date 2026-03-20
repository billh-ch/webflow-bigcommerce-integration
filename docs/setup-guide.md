# Webflow-BigCommerce Integration Plugin Setup Guide

## Overview
This guide will help you set up and configure the Webflow-BigCommerce Integration Plugin to display your BigCommerce products in Webflow and enable shopping cart functionality.

## Prerequisites
1. A BigCommerce store with products
2. A Webflow site
3. Basic knowledge of Webflow customization

## Installation Steps

### Step 1: Deploy the Backend
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd bigflow
   ```

2. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```

3. Set environment variables:
   ```bash
   export BIGCOMMERCE_STORE_HASH=your_store_hash
   export BIGCOMMERCE_ACCESS_TOKEN=your_access_token
   export WEBFLOW_API_KEY=your_webflow_api_key
   export WEBFLOW_SITE_ID=your_webflow_site_id
   ```

4. Run the application:
   ```bash
   python backend/app.py
   ```

### Step 2: Configure BigCommerce
1. Log in to your BigCommerce admin panel
2. Navigate to Settings > API Accounts
3. Create a new API account with the following scopes:
   - Content: read-only
   - Catalog: read-only
   - Carts: modify
   - Checkouts: modify
4. Copy the Store Hash and Access Token for use in environment variables

### Step 3: Configure Webflow
1. Log in to your Webflow account
2. Open your site editor
3. Go to Site Settings > Custom Code
4. Add the following script to the `<head>` section:
   ```html
   <script src="https://your-deployed-backend-url/static/product-display.js"></script>
   <script src="https://your-deployed-backend-url/static/cart-widget.js"></script>
   ```

### Step 4: Add Product Display Elements
1. In Webflow designer, add a new HTML Embed element where you want to display products
2. Add the following code:
   ```html
   <div data-bc-product-id="PRODUCT_ID"></div>
   ```
   Replace PRODUCT_ID with the actual BigCommerce product ID.

### Step 5: Add Cart Widget
1. Add another HTML Embed element where you want the cart to appear
2. Add the following code:
   ```html
   <div data-bc-cart-display></div>
   ```

### Step 6: Add Checkout Button
1. Add a button element in Webflow
2. Add the attribute `data-bc-checkout` to the button
3. Style as desired

## Configuration Options
- Adjust the CSS classes in the JavaScript files to match your Webflow design
- Modify the product display template in `product-display.js`
- Customize the cart widget appearance in `cart-widget.js`

## Troubleshooting
- Ensure all environment variables are correctly set
- Check browser console for JavaScript errors
- Verify BigCommerce API credentials have proper permissions
- Confirm Webflow site is properly configured to load external scripts

## Support
For issues or feature requests, please contact our support team or submit an issue on GitHub.