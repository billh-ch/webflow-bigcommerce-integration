# API Documentation

## Overview
This document describes the API endpoints available in the Webflow-BigCommerce Integration Plugin.

## Authentication
All API requests require proper environment variables to be set:
- `BIGCOMMERCE_STORE_HASH`
- `BIGCOMMERCE_ACCESS_TOKEN`
- `WEBFLOW_API_KEY`
- `WEBFLOW_SITE_ID`

## Endpoints

### GET /
**Description**: Health check endpoint
**Response**:
```json
{
  "message": "Webflow-BigCommerce Integration Plugin API"
}
```

### POST /sync-products
**Description**: Sync products from BigCommerce to Webflow CMS
**Request Body**: None
**Response**:
```json
{
  "status": "success",
  "message": "Synced X products to Webflow"
}
```

### POST /webhook/bigcommerce
**Description**: Handle BigCommerce webhooks for real-time updates
**Request Body**: BigCommerce webhook payload
**Response**:
```json
{
  "status": "received"
}
```

### POST /cart/add
**Description**: Add item to BigCommerce cart
**Request Body**:
```json
{
  "cart_id": "cart123",
  "product_id": "product123",
  "quantity": 1
}
```
**Response**: BigCommerce cart response

### POST /checkout-url
**Description**: Get BigCommerce checkout URL for cart
**Request Body**:
```json
{
  "cart_id": "cart123"
}
```
**Response**:
```json
{
  "checkout_url": "https://store.example.com/checkout/..."
}
```

### POST /create-cart
**Description**: Create a new BigCommerce cart
**Request Body**: None
**Response**: BigCommerce cart creation response

### GET /cart/{cart_id}
**Description**: Get BigCommerce cart details
**Response**: BigCommerce cart details

### PUT /cart/{cart_id}/items/{item_id}
**Description**: Update item quantity in cart
**Request Body**:
```json
{
  "quantity": 2
}
```
**Response**: Updated cart details

### DELETE /cart/{cart_id}/items/{item_id}
**Description**: Remove item from cart
**Response**:
```json
{
  "status": "removed"
}
```

### GET /static/{filename}
**Description**: Serve static files from frontend directory
**Response**: Requested static file (JavaScript, CSS, etc.)

## Error Handling
All endpoints return appropriate HTTP status codes:
- 200: Success
- 400: Bad request
- 401: Unauthorized
- 500: Internal server error

Error responses follow this format:
```json
{
  "error": "Error message"
}
```