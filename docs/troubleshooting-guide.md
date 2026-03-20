# Troubleshooting Guide

## Overview
This guide helps diagnose and resolve common issues with the Webflow-BigCommerce Integration Plugin.

## Common Issues and Solutions

### 1. Products Not Displaying

#### Symptoms
- Empty product containers in Webflow
- "Failed to load product" messages
- Products not syncing from BigCommerce

#### Diagnosis
1. Check browser console for JavaScript errors
2. Verify BigCommerce API credentials
3. Confirm Webflow CMS collection exists
4. Check network requests in browser DevTools

#### Solutions
```javascript
// Check if required environment variables are set
console.log('API Base URL:', CONFIG.API_BASE_URL);

// Test BigCommerce connection
fetch('/test-bigcommerce-connection')
  .then(response => response.json())
  .then(data => console.log('Connection test:', data));
```

### 2. Cart Functionality Issues

#### Symptoms
- Items not adding to cart
- Cart count not updating
- Checkout button not working

#### Diagnosis
1. Check localStorage for cart ID
2. Verify BigCommerce cart API status
3. Inspect network requests for cart operations
4. Check browser console for errors

#### Solutions
```javascript
// Debug cart issues
function debugCart() {
  const cartId = localStorage.getItem(CONFIG.CART_STORAGE_KEY);
  console.log('Cart ID:', cartId);

  if (!cartId) {
    console.warn('No cart ID found');
    return;
  }

  // Test cart retrieval
  fetch(`/cart/${cartId}`)
    .then(response => response.json())
    .then(data => console.log('Cart data:', data))
    .catch(error => console.error('Cart error:', error));
}
```

### 3. Authentication Errors

#### Symptoms
- 401 Unauthorized responses
- API credentials rejected
- "Invalid token" errors

#### Diagnosis
1. Verify environment variables are set correctly
2. Check BigCommerce token expiration
3. Confirm Webflow API key permissions
4. Test API credentials independently

#### Solutions
```bash
# Test BigCommerce API credentials
curl -X GET \
  https://api.bigcommerce.com/stores/YOUR_STORE_HASH/v3/catalog/products \
  -H "X-Auth-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json"
```

### 4. Webhook Issues

#### Symptoms
- Product updates not reflecting in Webflow
- Webhook errors in logs
- Delayed synchronization

#### Diagnosis
1. Check BigCommerce webhook configuration
2. Verify webhook URL accessibility
3. Review webhook delivery logs
4. Test webhook endpoint manually

#### Solutions
```python
# Test webhook endpoint
import requests

def test_webhook():
    payload = {
        "scope": "store/product/updated",
        "data": {"id": 123, "name": "Test Product"},
        "hash": "test123",
        "created_at": "2026-03-19T12:00:00Z",
        "store_id": "store123"
    }

    response = requests.post(
        'http://localhost:5000/webhook/bigcommerce',
        json=payload
    )

    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
```

### 5. Performance Issues

#### Symptoms
- Slow page loading
- API timeouts
- High server resource usage

#### Diagnosis
1. Monitor API response times
2. Check server resource utilization
3. Profile database queries
4. Analyze network requests

#### Solutions
```python
# Add performance monitoring
import time
from functools import wraps

def monitor_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@monitor_performance
def sync_products():
    # Sync logic here
    pass
```

## Debugging Tools

### Browser Developer Tools
1. **Network Tab**: Monitor API requests and responses
2. **Console Tab**: Check for JavaScript errors
3. **Application Tab**: Inspect localStorage and sessionStorage
4. **Performance Tab**: Analyze page load performance

### Server-Side Debugging
```python
# Add detailed logging
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/debug/info')
def debug_info():
    logger.debug("Debug info requested")
    return {
        "environment": os.environ.get("ENVIRONMENT", "unknown"),
        "bigcommerce_configured": bool(BIGCOMMERCE_STORE_HASH),
        "webflow_configured": bool(WEBFLOW_API_KEY),
        "python_version": sys.version,
        "flask_version": flask.__version__
    }
```

### Command Line Debugging
```bash
# Check environment variables
printenv | grep -E "(BIGCOMMERCE|WEBFLOW)"

# Test network connectivity
ping api.bigcommerce.com
curl -I https://api.webflow.com

# Check running processes
ps aux | grep python

# Monitor logs
tail -f /var/log/application.log
```

## Error Codes and Meanings

### HTTP Status Codes
- **200**: Success
- **400**: Bad request (invalid parameters)
- **401**: Unauthorized (authentication failed)
- **403**: Forbidden (insufficient permissions)
- **404**: Not found (resource doesn't exist)
- **429**: Too many requests (rate limited)
- **500**: Internal server error
- **502**: Bad gateway
- **503**: Service unavailable

### BigCommerce API Errors
- **4000**: Invalid syntax
- **4001**: Invalid parameters
- **4002**: Missing required parameters
- **4010**: Authentication failed
- **4030**: Insufficient permissions
- **4040**: Resource not found
- **4290**: Rate limit exceeded

### Webflow API Errors
- **400**: Bad request
- **401**: Unauthorized
- **402**: Payment required
- **403**: Forbidden
- **404**: Not found
- **422**: Unprocessable entity
- **429**: Too many requests
- **500**: Internal server error
- **503**: Service unavailable

## Log Analysis

### Common Log Patterns
```bash
# Search for errors
grep -i "error" /var/log/application.log

# Search for specific error codes
grep "401" /var/log/application.log

# Count occurrences of errors
grep -c "ERROR" /var/log/application.log

# Tail recent errors
tail -f /var/log/application.log | grep -i "error"
```

### Log Levels
- **DEBUG**: Detailed information for diagnosing problems
- **INFO**: General information about application flow
- **WARNING**: Warning conditions that may indicate problems
- **ERROR**: Error conditions that prevent normal operation
- **CRITICAL**: Critical conditions that require immediate attention

## Recovery Procedures

### Resetting Application State
```bash
# Clear application cache
redis-cli FLUSHALL

# Restart application
sudo systemctl restart webflow-bigcommerce

# Clear browser storage
# In browser console:
localStorage.clear();
sessionStorage.clear();
```

### Database Recovery
```sql
-- Check database integrity
PRAGMA integrity_check;

-- Repair database if needed
REINDEX;
ANALYZE;

-- Restore from backup if necessary
.quit
sqlite3 backup.db .dump | sqlite3 production.db
```

### Credential Rotation
1. Generate new BigCommerce API token
2. Create new Webflow API key
3. Update environment variables
4. Restart application
5. Test connectivity

## Prevention Strategies

### Regular Maintenance
1. Monitor API usage limits
2. Update dependencies regularly
3. Review security certificates
4. Check backup integrity
5. Test failover procedures

### Monitoring Setup
```python
# Example monitoring endpoint
@app.route('/health')
def health_check():
    checks = {
        "database": check_database(),
        "bigcommerce": check_bigcommerce_api(),
        "webflow": check_webflow_api(),
        "disk_space": check_disk_space(),
        "memory": check_memory_usage()
    }

    status = "healthy" if all(checks.values()) else "unhealthy"
    return {"status": status, "checks": checks}
```

### Automated Testing
```python
# Integration tests for common failure scenarios
def test_bigcommerce_timeout():
    with pytest.raises(requests.Timeout):
        bc_client.get_products(timeout=0.001)

def test_invalid_credentials():
    with pytest.raises(AuthenticationError):
        client = BigCommerceClient("invalid", "invalid")
        client.get_products()
```

## Support Resources

### Documentation
- Official BigCommerce API documentation
- Webflow API documentation
- Flask documentation
- Python requests library documentation

### Community Support
- GitHub Issues for this project
- BigCommerce Developer Community
- Webflow Community Forum
- Stack Overflow

### Professional Support
- BigCommerce Partner Program
- Webflow Experts directory
- Professional consulting services

## Emergency Procedures

### Immediate Actions
1. Check system status pages for service outages
2. Verify internet connectivity
3. Restart application services
4. Check server resources (CPU, memory, disk)
5. Review recent deployments or changes

### Escalation Path
1. Local debugging and log analysis
2. Team lead notification
3. Infrastructure team involvement
4. Vendor support contact
5. Executive notification for critical outages

By following this troubleshooting guide, you should be able to diagnose and resolve most common issues with the Webflow-BigCommerce Integration Plugin.