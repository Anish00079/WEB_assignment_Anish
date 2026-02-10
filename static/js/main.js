/* ===================================
   Online Bookstore - Custom JavaScript
   =================================== */

// DOM Content Loaded Event
document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initMobileMenu();
    initFormValidation();
    initCartFunctionality();
    initSearchHighlight();
    initAnimations();
    initTooltips();
});

/* ===================================
   Mobile Menu Toggle
   =================================== */
function initMobileMenu() {
    const menuToggle = document.querySelector('.navbar-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            
            // Animate hamburger menu
            const spans = menuToggle.querySelectorAll('span');
            spans.forEach((span, index) => {
                if (navMenu.classList.contains('active')) {
                    if (index === 0) span.style.transform = 'rotate(45deg) translate(5px, 5px)';
                    if (index === 1) span.style.opacity = '0';
                    if (index === 2) span.style.transform = 'rotate(-45deg) translate(5px, -5px)';
                } else {
                    span.style.transform = 'none';
                    span.style.opacity = '1';
                }
            });
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!menuToggle.contains(event.target) && !navMenu.contains(event.target)) {
                navMenu.classList.remove('active');
            }
        });
    }
}

/* ===================================
   Form Validation System
   =================================== */
function initFormValidation() {
    const forms = document.querySelectorAll('form[data-validate]');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(form)) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
        
        // Real-time validation
        const inputs = form.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                validateField(input);
            });
            
            input.addEventListener('input', function() {
                if (input.classList.contains('is-invalid')) {
                    validateField(input);
                }
            });
        });
    });
}

function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('input, textarea, select');
    
    inputs.forEach(input => {
        if (!validateField(input)) {
            isValid = false;
        }
    });
    
    return isValid;
}

function validateField(field) {
    const value = field.value.trim();
    let isValid = true;
    let errorMessage = '';
    
    // Check required
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        errorMessage = 'This field is required';
    }
    
    // Check minlength
    if (isValid && field.hasAttribute('data-minlength')) {
        const minlength = parseInt(field.getAttribute('data-minlength'));
        if (value.length < minlength) {
            isValid = false;
            errorMessage = `Minimum ${minlength} characters required`;
        }
    }
    
    // Check maxlength
    if (isValid && field.hasAttribute('maxlength')) {
        const maxlength = parseInt(field.getAttribute('maxlength'));
        if (value.length > maxlength) {
            isValid = false;
            errorMessage = `Maximum ${maxlength} characters allowed`;
        }
    }
    
    // Check email format
    if (isValid && field.type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid email address';
        }
    }
    
    // Check min value
    if (isValid && field.hasAttribute('min') && value) {
        const min = parseFloat(field.getAttribute('min'));
        if (parseFloat(value) < min) {
            isValid = false;
            errorMessage = `Value must be at least ${min}`;
        }
    }
    
    // Update field classes
    if (field.value.trim() !== '' || field.classList.contains('was-validated')) {
        if (isValid) {
            field.classList.remove('is-invalid');
            field.classList.add('is-valid');
        } else {
            field.classList.remove('is-valid');
            field.classList.add('is-invalid');
            
            // Show error message
            let feedbackEl = field.parentNode.querySelector('.invalid-feedback');
            if (feedbackEl && errorMessage) {
                feedbackEl.textContent = errorMessage;
            }
        }
    }
    
    return isValid;
}

/* ===================================
   Cart Functionality
   =================================== */
function initCartFunctionality() {
    // Add to cart buttons
    const addToCartButtons = document.querySelectorAll('[data-add-to-cart]');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const bookId = this.getAttribute('data-book-id');
            addToCart(bookId, this);
        });
    });
    
    // Update cart quantity
    const quantityInputs = document.querySelectorAll('[data-cart-quantity]');
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            updateCartQuantity(this);
        });
    });
    
    // Remove from cart
    const removeButtons = document.querySelectorAll('[data-remove-from-cart]');
    removeButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            if (confirm('Remove this item from cart?')) {
                const bookId = this.getAttribute('data-book-id');
                removeFromCart(bookId);
            }
        });
    });
}

function addToCart(bookId, button) {
    // Show loading state
    const originalText = button.innerHTML;
    button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Adding...';
    button.disabled = true;
    
    // Simulate API call (replace with actual fetch in production)
    setTimeout(() => {
        button.innerHTML = originalText;
        button.disabled = false;
        
        // Show success message
        showNotification('Item added to cart!', 'success');
        
        // Update cart count
        updateCartCount(1);
        
        // Add visual feedback
        button.classList.add('pulse');
        setTimeout(() => button.classList.remove('pulse'), 500);
    }, 500);
}

function updateCartQuantity(input) {
    const quantity = parseInt(input.value);
    const bookId = input.getAttribute('data-book-id');
    const maxQuantity = parseInt(input.getAttribute('max'));
    
    if (quantity < 1) {
        input.value = 1;
        return;
    }
    
    if (quantity > maxQuantity) {
        input.value = maxQuantity;
        showNotification(`Only ${maxQuantity} items available`, 'warning');
        return;
    }
    
    // Update cart item (replace with actual fetch in production)
    showNotification('Cart updated!', 'success');
}

function removeFromCart(bookId) {
    // Remove item from cart (replace with actual fetch in production)
    const cartItem = document.querySelector(`[data-cart-item="${bookId}"]`);
    if (cartItem) {
        cartItem.style.transition = 'all 0.3s ease';
        cartItem.style.opacity = '0';
        cartItem.style.transform = 'translateX(100px)';
        setTimeout(() => {
            cartItem.remove();
            updateCartCount(-1);
            showNotification('Item removed from cart', 'info');
        }, 300);
    }
}

function updateCartCount(change) {
    const cartBadge = document.getElementById('cart-count');
    if (cartBadge) {
        let currentCount = parseInt(cartBadge.textContent) || 0;
        currentCount += change;
        cartBadge.textContent = currentCount;
        
        // Animate badge
        cartBadge.classList.add('pulse');
        setTimeout(() => cartBadge.classList.remove('pulse'), 300);
    }
}

/* ===================================
   Search Highlight
   =================================== */
function initSearchHighlight() {
    const searchInput = document.querySelector('[name="search"]');
    if (searchInput) {
        searchInput.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        
        searchInput.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
        });
    }
}

/* ===================================
   Animations
   =================================== */
function initAnimations() {
    // Fade in elements
    const fadeElements = document.querySelectorAll('.fade-in');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });
    
    fadeElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'all 0.5s ease';
        observer.observe(el);
    });
    
    // Stagger animation for grid items
    const gridItems = document.querySelectorAll('.book-grid > *');
    gridItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.1}s`;
    });
}

/* ===================================
   Tooltips
   =================================== */
function initTooltips() {
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    
    tooltipElements.forEach(el => {
        el.addEventListener('mouseenter', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'custom-tooltip';
            tooltip.textContent = this.getAttribute('data-tooltip');
            tooltip.style.cssText = `
                position: absolute;
                background: #333;
                color: white;
                padding: 5px 10px;
                border-radius: 4px;
                font-size: 12px;
                z-index: 1000;
                pointer-events: none;
            `;
            
            document.body.appendChild(tooltip);
            
            const rect = this.getBoundingClientRect();
            tooltip.style.top = `${rect.top - 30}px`;
            tooltip.style.left = `${rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2)}px`;
            
            this._tooltip = tooltip;
        });
        
        el.addEventListener('mouseleave', function() {
            if (this._tooltip) {
                this._tooltip.remove();
                this._tooltip = null;
            }
        });
    });
}

/* ===================================
   Notification System
   =================================== */
function showNotification(message, type = 'info') {
    // Remove existing notifications
    const existingNotifications = document.querySelectorAll('.custom-notification');
    existingNotifications.forEach(n => n.remove());
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `custom-notification notification-${type}`;
    notification.innerHTML = `
        <span>${message}</span>
        <button onclick="this.parentElement.remove()">&times;</button>
    `;
    
    // Style notification
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'success' ? '#27ae60' : type === 'warning' ? '#f39c12' : type === 'danger' ? '#c0392b' : '#3498db'};
        color: white;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 9999;
        display: flex;
        align-items: center;
        gap: 1rem;
        animation: slideIn 0.3s ease;
        max-width: 350px;
    `;
    
    // Add animation keyframes if not exists
    if (!document.querySelector('#notification-styles')) {
        const style = document.createElement('style');
        style.id = 'notification-styles';
        style.textContent = `
            @keyframes slideIn {
                from { transform: translateX(100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
            @keyframes slideOut {
                from { transform: translateX(0); opacity: 1; }
                to { transform: translateX(100%); opacity: 0; }
            }
        `;
        document.head.appendChild(style);
    }
    
    // Add close button style
    notification.querySelector('button').style.cssText = `
        background: none;
        border: none;
        color: white;
        font-size: 1.25rem;
        cursor: pointer;
        padding: 0;
        line-height: 1;
    `;
    
    // Append to body
    document.body.appendChild(notification);
    
    // Auto remove after 3 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease forwards';
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

/* ===================================
   Utility Functions
   =================================== */
function formatCurrency(amount) {
    return '$' + parseFloat(amount).toFixed(2);
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function(...args) {
        if (!inThrottle) {
            func.apply(this, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Export functions for use in inline scripts
window.showNotification = showNotification;
window.formatCurrency = formatCurrency;
window.addToCart = addToCart;
window.removeFromCart = removeFromCart;