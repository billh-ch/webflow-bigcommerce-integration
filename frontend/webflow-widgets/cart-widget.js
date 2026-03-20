// Webflow Widget for BigCommerce Cart
(function() {
  // Configuration
  const CONFIG = {
    API_BASE_URL: 'https://your-app-domain.com', // Replace with your deployed backend URL
    CART_STORAGE_KEY: 'bigcommerce_cart_id'
  };

  // Initialize cart widget
  function initCartWidget() {
    const cartWidgets = document.querySelectorAll('[data-bc-cart-display]');

    cartWidgets.forEach(widget => {
      updateCartDisplay(widget);
    });
  }

  // Update cart display
  async function updateCartDisplay(widget) {
    try {
      const cartId = localStorage.getItem(CONFIG.CART_STORAGE_KEY);

      if (!cartId) {
        renderEmptyCart(widget);
        return;
      }

      const response = await fetch(`${CONFIG.API_BASE_URL}/cart/${cartId}`);

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const cartData = await response.json();
      renderCartContents(widget, cartData);
    } catch (error) {
      console.error('Error updating cart display:', error);
      renderCartError(widget, error.message);
    }
  }

  // Render empty cart
  function renderEmptyCart(widget) {
    widget.innerHTML = `
      <div class="bc-cart-empty">
        <p>Your cart is empty</p>
      </div>
    `;
  }

  // Render cart contents
  function renderCartContents(widget, cartData) {
    const lineItems = cartData.line_items || [];
    const subtotal = cartData.subtotal || 0;

    if (lineItems.length === 0) {
      renderEmptyCart(widget);
      return;
    }

    const itemsHtml = lineItems.map(item => `
      <div class="bc-cart-item" data-item-id="${item.id}">
        <div class="bc-cart-item-image">
          <img src="${item.image_url || 'https://placehold.co/50x50?text=Product'}" alt="${item.name}">
        </div>
        <div class="bc-cart-item-details">
          <h4 class="bc-cart-item-name">${item.name}</h4>
          <p class="bc-cart-item-price">$${(item.sale_price || item.price)?.toFixed(2) || '0.00'}</p>
        </div>
        <div class="bc-cart-item-quantity">
          <button class="bc-qty-btn" data-action="decrease" data-item-id="${item.id}">-</button>
          <span class="bc-qty-value">${item.quantity}</span>
          <button class="bc-qty-btn" data-action="increase" data-item-id="${item.id}">+</button>
        </div>
        <div class="bc-cart-item-total">
          $${(item.sale_price * item.quantity || item.price * item.quantity || 0).toFixed(2)}
        </div>
        <button class="bc-remove-item" data-item-id="${item.id}">✕</button>
      </div>
    `).join('');

    widget.innerHTML = `
      <div class="bc-cart-items">
        ${itemsHtml}
      </div>
      <div class="bc-cart-summary">
        <div class="bc-cart-subtotal">
          <span>Subtotal:</span>
          <span>$${subtotal.toFixed(2)}</span>
        </div>
        <button class="bc-checkout-button" data-bc-checkout>
          Proceed to Checkout
        </button>
      </div>
    `;

    // Attach event listeners
    attachCartEventListeners(widget);
  }

  // Render cart error
  function renderCartError(widget, errorMessage) {
    widget.innerHTML = `
      <div class="bc-cart-error">
        <p>Error loading cart: ${errorMessage}</p>
        <button class="bc-retry-button">Retry</button>
      </div>
    `;

    widget.querySelector('.bc-retry-button').addEventListener('click', () => {
      updateCartDisplay(widget);
    });
  }

  // Attach event listeners to cart elements
  function attachCartEventListeners(widget) {
    // Quantity buttons
    widget.querySelectorAll('.bc-qty-btn').forEach(button => {
      button.addEventListener('click', handleQuantityChange);
    });

    // Remove item buttons
    widget.querySelectorAll('.bc-remove-item').forEach(button => {
      button.addEventListener('click', handleRemoveItem);
    });

    // Checkout button
    const checkoutButton = widget.querySelector('[data-bc-checkout]');
    if (checkoutButton) {
      checkoutButton.addEventListener('click', handleCheckout);
    }
  }

  // Handle quantity change
  async function handleQuantityChange(event) {
    const button = event.target;
    const action = button.getAttribute('data-action');
    const itemId = button.getAttribute('data-item-id');

    try {
      const cartId = localStorage.getItem(CONFIG.CART_STORAGE_KEY);
      if (!cartId) return;

      // Update quantity
      const newQuantity = action === 'increase' ? 1 : -1;

      const response = await fetch(`${CONFIG.API_BASE_URL}/cart/${cartId}/items/${itemId}`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          quantity: newQuantity
        })
      });

      if (response.ok) {
        // Refresh cart display
        const cartWidget = button.closest('[data-bc-cart-display]');
        updateCartDisplay(cartWidget);
      } else {
        throw new Error('Failed to update quantity');
      }
    } catch (error) {
      console.error('Error updating quantity:', error);
      alert('Failed to update item quantity. Please try again.');
    }
  }

  // Handle remove item
  async function handleRemoveItem(event) {
    const button = event.target;
    const itemId = button.getAttribute('data-item-id');

    try {
      const cartId = localStorage.getItem(CONFIG.CART_STORAGE_KEY);
      if (!cartId) return;

      const response = await fetch(`${CONFIG.API_BASE_URL}/cart/${cartId}/items/${itemId}`, {
        method: 'DELETE'
      });

      if (response.ok) {
        // Refresh cart display
        const cartWidget = button.closest('[data-bc-cart-display]');
        updateCartDisplay(cartWidget);
      } else {
        throw new Error('Failed to remove item');
      }
    } catch (error) {
      console.error('Error removing item:', error);
      alert('Failed to remove item from cart. Please try again.');
    }
  }

  // Handle checkout
  async function handleCheckout() {
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

  // Initialize when DOM is loaded
  document.addEventListener('DOMContentLoaded', function() {
    initCartWidget();
  });

  // Expose functions globally
  window.BigCommerceCart = {
    initCartWidget,
    updateCartDisplay
  };
})();