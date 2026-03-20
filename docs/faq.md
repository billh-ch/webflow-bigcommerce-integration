# Frequently Asked Questions (FAQ)

## General Questions

### What is the Webflow-BigCommerce Integration Plugin?
The Webflow-BigCommerce Integration Plugin is a solution that connects BigCommerce stores with Webflow sites, allowing merchants to display their BigCommerce products in Webflow while maintaining full e-commerce functionality through BigCommerce's platform.

### Who is this plugin for?
This plugin is designed for:
- BigCommerce merchants who want to use Webflow for their storefront design
- Webflow designers who work with BigCommerce clients
- E-commerce businesses seeking headless commerce solutions
- Developers looking to integrate these two platforms

### What are the system requirements?
**Backend:**
- Python 3.7 or higher
- Flask web framework
- BigCommerce store with API access
- Webflow site with CMS collections

**Frontend:**
- Modern web browser
- Webflow account
- Access to Webflow site settings

### Is this plugin free to use?
The plugin is open-source and free to use. However:
- You need paid BigCommerce and Webflow accounts
- Hosting costs for deploying the backend
- Optional premium features may be charged separately

## Installation and Setup

### How do I install the plugin?
1. Clone the repository or download the source code
2. Install Python dependencies with `pip install -r requirements.txt`
3. Set environment variables for API credentials
4. Deploy the backend to your preferred hosting platform
5. Add JavaScript widgets to your Webflow site

### What credentials do I need?
You need:
- BigCommerce Store Hash
- BigCommerce Access Token
- Webflow API Key
- Webflow Site ID

### How do I get BigCommerce credentials?
1. Log into your BigCommerce admin panel
2. Go to Settings > API Accounts
3. Create a new API account with required scopes
4. Copy the Store Hash and Access Token

### How do I get Webflow credentials?
1. Log into your Webflow account
2. Go to Site Settings > API Access
3. Generate a new API token with appropriate permissions
4. Copy the API Key and Site ID

## Technical Questions

### What programming languages are used?
- Backend: Python (Flask framework)
- Frontend: JavaScript (ES6+)
- Deployment: Docker-ready with Procfile for Heroku

### Can I customize the product display?
Yes, you can:
- Modify CSS classes in the JavaScript widgets
- Create custom product templates
- Adjust styling to match your brand
- Add custom fields and attributes

### How does the cart functionality work?
The cart works by:
1. Creating a BigCommerce cart via API
2. Storing the cart ID in browser localStorage
3. Adding/removing items through API calls
4. Redirecting to BigCommerce checkout when ready

### Is inventory synchronized in real-time?
Basic inventory is synchronized during product sync. Real-time inventory synchronization is available as an advanced feature through webhooks.

### How are webhooks handled?
Webhooks are processed by:
1. Receiving notifications from BigCommerce
2. Transforming data formats between platforms
3. Updating Webflow CMS items accordingly
4. Handling different event types (create, update, delete)

## Deployment Questions

### Where can I deploy the backend?
Supported deployment platforms:
- Heroku (recommended for beginners)
- AWS Elastic Beanstalk
- Google Cloud Run
- Docker containers
- Any Python-compatible hosting

### How do I configure environment variables?
Set these environment variables:
```
BIGCOMMERCE_STORE_HASH=your_store_hash
BIGCOMMERCE_ACCESS_TOKEN=your_access_token
WEBFLOW_API_KEY=your_webflow_api_key
WEBFLOW_SITE_ID=your_webflow_site_id
```

### What ports does the application use?
The application runs on port 5000 by default, but can be configured through the PORT environment variable.

### How do I scale the application?
Scaling options:
- Horizontal scaling with load balancers
- Multiple worker processes (Gunicorn)
- Database connection pooling
- CDN for static assets

## Troubleshooting

### Why aren't my products showing?
Check:
1. BigCommerce API credentials are correct
2. Webflow CMS collection exists
3. Product IDs are valid
4. JavaScript console for errors
5. Network requests in browser DevTools

### How do I debug cart issues?
1. Check localStorage for cart ID
2. Verify BigCommerce cart API status
3. Inspect network requests for cart operations
4. Check browser console for JavaScript errors

### What should I do if I get authentication errors?
1. Verify all environment variables are set
2. Check BigCommerce token expiration
3. Confirm Webflow API key permissions
4. Test API credentials independently

### How do I monitor performance?
Monitor:
- API response times
- Server resource utilization
- Database query performance
- User experience metrics
- Error rates and patterns

## Security Questions

### How are API credentials protected?
- Stored as environment variables
- Never committed to version control
- Transmitted only over HTTPS
- Limited to required permissions only

### Is customer data secure?
The plugin:
- Doesn't store customer payment information
- Uses secure HTTPS connections
- Follows OAuth 2.0 best practices
- Implements proper error handling

### How do you handle data privacy?
- Complies with GDPR and CCPA regulations
- Minimizes data collection to essentials
- Provides data deletion capabilities
- Offers transparent privacy policies

## Feature Questions

### Does it support product variants?
Yes, product variants are supported:
- Size, color, and other options
- Variant-specific pricing
- Inventory tracking per variant
- Custom field mapping

### Can customers create accounts?
Customer account integration is available:
- BigCommerce customer API integration
- Secure authentication flows
- Order history tracking
- Saved payment methods

### Is there analytics support?
Analytics features include:
- Sales tracking and reporting
- Traffic monitoring
- Conversion rate optimization
- Custom dashboard integration

### Does it support multiple currencies?
Multi-currency support is planned:
- Automatic currency detection
- Exchange rate management
- Localized pricing display
- Currency conversion calculations

## Development Questions

### How can I contribute to the project?
1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests for new functionality
5. Submit a pull request

### What testing framework is used?
- Pytest for Python backend tests
- Unit tests for API clients
- Integration tests for workflows
- JavaScript testing (planned)

### How is the code structured?
Directory structure:
- `/backend` - Python Flask application
- `/frontend` - JavaScript widgets
- `/docs` - Documentation files
- `/tests` - Test suite

### Are there coding standards?
Yes, we follow:
- PEP 8 for Python code
- Standard JavaScript best practices
- Conventional commit messages
- Comprehensive documentation requirements

## Support Questions

### Where can I get help?
Support channels:
- GitHub Issues for bug reports
- Documentation for self-service help
- Community forums for discussions
- Professional support for enterprise users

### How quickly are issues addressed?
- Critical bugs: Within 24 hours
- High priority: Within 3 business days
- Medium priority: Within 1 week
- Low priority: Within 2 weeks

### Is there commercial support available?
Yes, commercial support options:
- Priority bug fixes
- Feature development assistance
- Custom integration services
- Training and consultation

### How do I report a security vulnerability?
1. Contact security@webflow-bigcommerce.com
2. Provide detailed vulnerability description
3. Include steps to reproduce
4. Allow time for investigation before disclosure

## Billing Questions

### Are there any hidden costs?
No hidden costs:
- Plugin code is completely free
- Hosting costs are separate
- BigCommerce/Webflow subscriptions apply
- Premium features may have costs

### How does the freemium model work?
Freemium tiers:
- Free: Basic product display and cart
- Premium: Advanced features and support
- Enterprise: Custom features and SLA

### What payment methods are accepted?
Payment methods for premium features:
- Credit cards (Visa, MasterCard, American Express)
- PayPal
- Bank transfers for enterprise plans
- Custom billing for large organizations

## Future Development

### What features are planned?
Upcoming features:
- Real-time inventory synchronization
- Customer account integration
- Analytics and reporting dashboard
- Multi-currency support
- Performance optimization tools

### How can I request new features?
1. Submit feature requests on GitHub Issues
2. Vote on existing feature requests
3. Contact the development team directly
4. Participate in user surveys

### When will new features be released?
Release schedule:
- Monthly minor updates
- Quarterly major feature releases
- Emergency patches as needed
- Roadmap published publicly

This FAQ covers the most common questions about the Webflow-BigCommerce Integration Plugin. For more detailed information, please refer to the specific documentation files in the `/docs` directory.