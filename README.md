# Webflow-BigCommerce Integration Plugin

## Overview
This plugin enables seamless integration between BigCommerce and Webflow, allowing merchants to display their BigCommerce products in Webflow sites while maintaining full e-commerce functionality through BigCommerce's robust platform.

## GitHub Repository
Code is automatically synced to GitHub: https://github.com/billh-ch/webflow-bigcommerce-integration

## Features
- Display BigCommerce products in Webflow
- Shopping cart functionality
- Seamless checkout process
- Real-time inventory updates (via webhooks)
- Automatic product synchronization

## Architecture
The plugin consists of three main components:

### 1. Backend API (Python/Flask)
Handles authentication, data synchronization, and API integrations:
- `/backend/app.py` - Main Flask application
- `/backend/api/bigcommerce_client.py` - BigCommerce API integration
- `/backend/api/webflow_client.py` - Webflow API integration

### 2. Frontend Widgets (JavaScript)
Webflow-compatible components for displaying products and managing carts:
- `/frontend/webflow-widgets/product-display.js` - Product display widget
- `/frontend/webflow-widgets/cart-widget.js` - Shopping cart widget

### 3. Documentation
- `/docs/setup-guide.md` - User setup guide
- `/README.md` - Developer documentation

## Setup for Developers

### Prerequisites
- Python 3.7+
- pip
- BigCommerce store with API access
- Webflow site

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd bigflow
   ```

2. Install Python dependencies:
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

4. Run the development server:
   ```bash
   python backend/app.py
   ```

## API Endpoints
- `GET /` - Health check endpoint
- `POST /sync-products` - Sync products from BigCommerce to Webflow
- `POST /webhook/bigcommerce` - Handle BigCommerce webhooks
- `POST /cart/add` - Add item to cart
- `POST /checkout-url` - Get BigCommerce checkout URL

## Deployment
The application can be deployed to any cloud platform that supports Python applications:
- Heroku
- AWS Elastic Beanstalk
- Google Cloud Run
- Vercel (with serverless functions)

For Heroku deployment:
1. Create a new Heroku app
2. Set environment variables in Heroku config
3. Deploy using Git:
   ```bash
   git push heroku main
   ```

## Development Roadmap
### MVP (Completed)
- [x] Basic product display in Webflow
- [x] Shopping cart functionality
- [x] Checkout integration
- [x] Product synchronization

### Post-MVP Features
- [ ] Real-time inventory synchronization
- [ ] Customer account integration
- [ ] Analytics and reporting
- [ ] Multi-currency support
- [ ] Performance optimization

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Support
For issues or feature requests, please submit an issue on GitHub.