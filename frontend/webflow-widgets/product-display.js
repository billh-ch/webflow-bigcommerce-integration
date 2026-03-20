// Webflow Widget for BigCommerce Product Display
(function() {
  // Configuration
  const CONFIG = {
    API_BASE_URL: 'https://your-app-domain.com', // Replace with your deployed backend URL
    CART_STORAGE_KEY: 'bigcommerce_cart_id'
  };

  // Initialize the widget
  function initProductWidgets() {
    // Find all product display elements
    const productElements = document.querySelectorAll('[data-bc-product-id]');

    productElements.forEach(element => {
      const productId = element.getAttribute('data-bc-product-id');
      renderProduct(element, productId);
    });
  }

  // Render a product in the Webflow element
  async function renderProduct(element, productId) {
    try {
      // In a real implementation, you would fetch product data from your backend
      // For now, we'll use placeholder data

      // Add loading state
      element.innerHTML = '<div class="loading">Loading product...</div>';

      // Simulate API call delay
      await new Promise(resolve => setTimeout(resolve, 500));

      // Render product (this would normally come from API)
      element.innerHTML = `
        <div class="bc-product" data-product-id="${productId}">
          <div class="bc-product-image">
            <img src="https://placehold.co/300x300?text=Product+Image" alt="Product Image">
          </div>
          <div class="bc-product-info">
            <h3 class="bc-product-name">Sample Product ${productId}</h3>
            <p class="bc-product-price">$29.99</p>
            <button class="bc-add-to-cart" data-product-id="${productId}">Add to Cart</button>
          </div>
        </div>
      `;

      // Attach event listeners
      const addButton = element.querySelector('.bc-add-to-cart');
      if (addButton) {
        addButton.addEventListener('click', () => addToCart(productId));
      }
    } catch (error) {
      console.error('Error rendering product:', error);
      element.innerHTML = '<div class="error">Failed to load product</div>';
    }
  }

  // Add item to cart
  async function addToCart(productId) {
    try {
      // Get or create cart
      let cartId = localStorage.getItem(CONFIG.CART_STORAGE_KEY);

      if (!cartId) {
        // Create new cart
        const response = await fetch(`${CONFIG.API_BASE_URL}/create-cart`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          }
        });

        const data = await response.json();
        cartId = data.cart.id;
        localStorage.setItem(CONFIG.CART_STORAGE_KEY, cartId);
      }

      // Add item to cart
      const response = await fetch(`${CONFIG.API_BASE_URL}/cart/add`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          cart_id: cartId,
          product_id: productId,
          quantity: 1
        })
      });

      const result = await response.json();

      if (response.ok) {
        alert('Item added to cart!');
      } else {
        throw new Error(result.error || 'Failed to add item to cart');
      }
    } catch (error) {
      console.error('Error adding to cart:', error);
      alert('Failed to add item to cart. Please try again.');
    }
  }

  // Initialize cart widget
  function initCartWidget() {
    const cartWidget = document.querySelector('[data-bc-cart]');
    if (cartWidget) {
      updateCartDisplay();
    }
  }

  // Update cart display
  async function updateCartDisplay() {
    const cartWidget = document.querySelector('[data-bc-cart]');
    if (!cartWidget) return;

    try {
      const cartId = localStorage.getItem(CONFIG.CART_STORAGE_KEY);
      if (!cartId) {
        cartWidget.innerHTML = '<div class="bc-cart-empty">Cart is empty</div>';
        return;
      }

      const response = await fetch(`${CONFIG.API_BASE_URL}/cart/${cartId}`);
      const cartData = await response.json();

      if (response.ok) {
        const itemCount = cartData.line_items?.reduce((total, item) => total + item.quantity, 0) || 0;
        cartWidget.innerHTML = `<div class="bc-cart-count">${itemCount} items</div>`;
      } else {
        cartWidget.innerHTML = '<div class="bc-cart-error">Error loading cart</div>';
      }
    } catch (error) {
      console.error('Error updating cart display:', error);
      cartWidget.innerHTML = '<div class="bc-cart-error">Error loading cart</div>';
    }
  }

  // Initialize checkout button
  function initCheckoutButton() {
    const checkoutButtons = document.querySelectorAll('[data-bc-checkout]');
    checkoutButtons.forEach(button => {
      button.addEventListener('click', goToCheckout);
    });
  }

  // Redirect to BigCommerce checkout
  async function goToCheckout() {
    try {
      const cartId = localStorage.getItem(CONFIG.CART_STORAGE_KEY);
      if (!cartId) {
        alert('Your cart is empty');
        return;
      }

      const response = await fetch(`${CONFIG.API_BASE_URL}/checkout-url`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ cart_id: cartId })
      });

      const data = await response.json();

      if (response.ok && data.checkout_url) {
        window.location.href = data.checkout_url;
      } else {
        throw new Error(data.error || 'Failed to create checkout');
      }
    } catch (error) {
      console.error('Error during checkout:', error);
      alert('Failed to proceed to checkout. Please try again.');
    }
  }

  // Initialize everything when DOM is loaded
  document.addEventListener('DOMContentLoaded', function() {
    initProductWidgets();
    initCartWidget();
    initCheckoutButton();
  });

  // Expose functions globally for Webflow interactions
  window.BigCommerceIntegration = {
    initProductWidgets,
    initCartWidget,
    initCheckoutButton,
    addToCart,
    updateCartDisplay,
    goToCheckout
  };
})();