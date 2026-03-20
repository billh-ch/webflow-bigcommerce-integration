# Deployment Guide

## Overview
This guide explains how to deploy the Webflow-BigCommerce Integration Plugin to various hosting platforms.

## Prerequisites
1. A deployed instance of this application
2. Properly configured environment variables
3. Access to your chosen deployment platform

## Environment Variables
Before deploying, ensure you have set the following environment variables:

```
BIGCOMMERCE_STORE_HASH=your_store_hash
BIGCOMMERCE_ACCESS_TOKEN=your_access_token
WEBFLOW_API_KEY=your_webflow_api_key
WEBFLOW_SITE_ID=your_webflow_site_id
```

## Deployment Options

### Heroku (Recommended for beginners)

1. Install the Heroku CLI:
   ```bash
   brew tap heroku/brew && brew install heroku
   ```

2. Login to Heroku:
   ```bash
   heroku login
   ```

3. Create a new Heroku app:
   ```bash
   heroku create your-app-name
   ```

4. Set environment variables:
   ```bash
   heroku config:set BIGCOMMERCE_STORE_HASH=your_store_hash
   heroku config:set BIGCOMMERCE_ACCESS_TOKEN=your_access_token
   heroku config:set WEBFLOW_API_KEY=your_webflow_api_key
   heroku config:set WEBFLOW_SITE_ID=your_webflow_site_id
   ```

5. Deploy the application:
   ```bash
   git push heroku main
   ```

6. Scale the dyno (optional):
   ```bash
   heroku ps:scale web=1
   ```

### AWS Elastic Beanstalk

1. Install the EB CLI:
   ```bash
   pip install awsebcli
   ```

2. Initialize the application:
   ```bash
   eb init
   ```

3. Create an environment:
   ```bash
   eb create webflow-bigcommerce-env
   ```

4. Set environment variables:
   ```bash
   eb setenv BIGCOMMERCE_STORE_HASH=your_store_hash
   eb setenv BIGCOMMERCE_ACCESS_TOKEN=your_access_token
   eb setenv WEBFLOW_API_KEY=your_webflow_api_key
   eb setenv WEBFLOW_SITE_ID=your_webflow_site_id
   ```

5. Deploy the application:
   ```bash
   eb deploy
   ```

### Google Cloud Run

1. Install the Google Cloud SDK:
   ```bash
   curl https://sdk.cloud.google.com | bash
   ```

2. Authenticate with Google Cloud:
   ```bash
   gcloud auth login
   ```

3. Set your project:
   ```bash
   gcloud config set project YOUR_PROJECT_ID
   ```

4. Build and deploy the container:
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/webflow-bigcommerce
   gcloud run deploy --image gcr.io/YOUR_PROJECT_ID/webflow-bigcommerce --platform managed
   ```

5. Set environment variables:
   ```bash
   gcloud run services update webflow-bigcommerce --set-env-vars=BIGCOMMERCE_STORE_HASH=your_store_hash,BIGCOMMERCE_ACCESS_TOKEN=your_access_token,WEBFLOW_API_KEY=your_webflow_api_key,WEBFLOW_SITE_ID=your_webflow_site_id
   ```

### Docker Deployment

1. Build the Docker image:
   ```bash
   docker build -t webflow-bigcommerce .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 \
     -e BIGCOMMERCE_STORE_HASH=your_store_hash \
     -e BIGCOMMERCE_ACCESS_TOKEN=your_access_token \
     -e WEBFLOW_API_KEY=your_webflow_api_key \
     -e WEBFLOW_SITE_ID=your_webflow_site_id \
     webflow-bigcommerce
   ```

### Vercel (Serverless Functions)

1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Create an API endpoint structure:
   ```
   api/
     webhook.js
     products.js
     cart.js
   ```

3. Convert Flask endpoints to serverless functions:
   ```javascript
   // api/webhook.js
   module.exports = (req, res) => {
     // Handle BigCommerce webhook
     res.json({ status: "received" });
   };
   ```

4. Deploy to Vercel:
   ```bash
   vercel --prod
   ```

## Post-Deployment Configuration

### 1. Update Webflow Custom Code
After deployment, update your Webflow site's custom code with the deployed URL:

```html
<script src="https://your-deployed-url/static/product-display.js"></script>
<script src="https://your-deployed-url/static/cart-widget.js"></script>
```

### 2. Configure BigCommerce Webhooks
Set up BigCommerce webhooks to point to your deployed endpoint:

1. Go to BigCommerce Admin → Settings → Webhooks
2. Create a new webhook with:
   - Event: store/product/created
   - Callback URL: https://your-deployed-url/webhook/bigcommerce
3. Repeat for other events:
   - store/product/updated
   - store/product/deleted

### 3. Test the Integration
1. Visit your Webflow site
2. Check that products are displayed correctly
3. Test adding items to cart
4. Test the checkout process

## Monitoring and Maintenance

### Logs
Monitor your application logs through your deployment platform's interface:
- Heroku: `heroku logs --tail`
- AWS: CloudWatch Logs
- Google Cloud: Cloud Logging
- Docker: `docker logs CONTAINER_ID`

### Updates
To update your deployment:

1. Pull the latest code:
   ```bash
   git pull origin main
   ```

2. Deploy the updates:
   ```bash
   git push heroku main  # For Heroku
   ```

### Scaling
Most platforms provide automatic scaling. For manual scaling:

- Heroku: `heroku ps:scale web=3`
- AWS: Auto Scaling Groups
- Google Cloud: Cloud Run automatically scales

## Troubleshooting

### Application Won't Start
1. Check environment variables are set correctly
2. Verify BigCommerce and Webflow API credentials
3. Check application logs for errors

### Products Not Syncing
1. Verify BigCommerce API permissions
2. Check Webflow CMS collection exists
3. Ensure webhook is properly configured

### Cart Issues
1. Check BigCommerce cart API status
2. Verify session storage is working
3. Test cart endpoints directly

### Performance Issues
1. Monitor response times
2. Check API rate limits
3. Consider implementing caching

## Security Considerations

### HTTPS
Ensure your deployment uses HTTPS for all communications.

### API Keys
Never expose API keys in client-side code.

### Webhook Validation
Validate webhook signatures to prevent unauthorized requests.

### Rate Limiting
Implement rate limiting to prevent abuse.

## Backup and Recovery

### Database Backups
If using a database, ensure regular backups are performed.

### Configuration Backups
Keep copies of environment variables and configuration files.

### Version Control
Maintain your code in version control with regular commits.