# Webflow Usage Example

## Overview
This guide shows how to use the Webflow widgets in your Webflow site.

## Adding Product Display Widgets

### 1. Add Custom Code to Webflow
In your Webflow site, go to:
Site Settings → Custom Code → Head Code

Add the following script tags:

```html
<script src="https://your-deployed-backend-url/static/product-display.js"></script>
<script src="https://your-deployed-backend-url/static/cart-widget.js"></script>
```

### 2. Display Individual Products
To display a specific product, add an HTML Embed element with:

```html
<div data-bc-product-id="PRODUCT_ID"></div>
```

Replace `PRODUCT_ID` with the actual BigCommerce product ID.

### 3. Display Product Lists
To display multiple products, add an HTML Embed element with:

```html
<div data-bc-product-list>
  <div data-bc-product-id="PRODUCT_ID_1"></div>
  <div data-bc-product-id="PRODUCT_ID_2"></div>
  <div data-bc-product-id="PRODUCT_ID_3"></div>
</div>
```

## Adding Cart Widget

### 1. Add Cart Display
Add an HTML Embed element where you want the cart to appear:

```html
<div data-bc-cart-display></div>
```

### 2. Add Cart Counter
To display a simple cart item counter:

```html
<div data-bc-cart></div>
```

## Adding Checkout Functionality

### 1. Add Checkout Button
Add a button element and give it the attribute:

```
data-bc-checkout
```

### 2. Add Checkout Form
For a more customized checkout experience:

```html
<div data-bc-checkout-form></div>
```

## Customization

### CSS Classes
The widgets use the following CSS classes that you can style:

- `.bc-product` - Container for product display
- `.bc-product-image` - Product image container
- `.bc-product-name` - Product name
- `.bc-product-price` - Product price
- `.bc-add-to-cart` - Add to cart button
- `.bc-cart-display` - Cart display container
- `.bc-cart-items` - Cart items container
- `.bc-cart-item` - Individual cart item
- `.bc-checkout-button` - Checkout button

### Example Custom Styling
Add this to your Webflow site's custom CSS:

```css
.bc-product {
  border: 1px solid #eee;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
}

.bc-product-image img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
}

.bc-add-to-cart {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}

.bc-add-to-cart:hover {
  background-color: #0056b3;
}
```

## Initialization

The widgets automatically initialize when the DOM is loaded. If you need to manually initialize them (e.g., after dynamically adding elements), you can call:

```javascript
// Re-initialize product widgets
window.BigCommerceIntegration.initProductWidgets();

// Re-initialize cart widget
window.BigCommerceCart.initCartWidget();

// Re-initialize checkout button
window.BigCommerceIntegration.initCheckoutButton();
```

## Troubleshooting

### Scripts Not Loading
1. Check that the backend URL is correct
2. Verify the server is running
3. Check browser developer console for errors

### Products Not Displaying
1. Verify the product ID exists in BigCommerce
2. Check BigCommerce API credentials
3. Ensure product is visible in BigCommerce

### Cart Not Working
1. Check browser storage for cart ID
2. Verify BigCommerce cart API is working
3. Check network requests in browser developer tools

## Advanced Usage

### Custom Event Handlers
You can attach custom event handlers:

```javascript
document.addEventListener('bc:productLoaded', function(event) {
  console.log('Product loaded:', event.detail);
});

document.addEventListener('bc:itemAddedToCart', function(event) {
  console.log('Item added to cart:', event.detail);
});
```

### Programmatic Cart Management
You can programmatically interact with the cart:

```javascript
// Add item to cart
window.BigCommerceIntegration.addToCart('PRODUCT_ID');

// Update cart display
window.BigCommerceCart.updateCartDisplay();

// Go to checkout
window.BigCommerceIntegration.goToCheckout();
```