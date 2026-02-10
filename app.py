"""
Main Flask Application for Online Bookstore
Handles routing, authentication, and business logic
"""

from flask import Flask, render_template, redirect, url_for, flash, request, abort, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from models import db, User, Category, Book, Order, OrderItem, Review, ContactMessage
from datetime import datetime
import os

# Initialize Flask extensions
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

db.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    """Load user from database for Flask-Login"""
    return User.query.get(int(user_id))

# ==================== AUTH ROUTES ====================

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('register'))
        
        # Create new user
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login route"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user)
            next_page = request.args.get('next')
            flash('Login successful!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    """User logout route"""
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/profile')
@login_required
def profile():
    """User profile route"""
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.order_date.desc()).all()
    return render_template('profile.html', orders=orders)


@app.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    """Edit user profile route"""
    if request.method == 'POST':
        current_user.first_name = request.form.get('first_name')
        current_user.last_name = request.form.get('last_name')
        current_user.phone = request.form.get('phone')
        current_user.address = request.form.get('address')
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    
    return render_template('edit_profile.html')


# ==================== BOOK ROUTES ====================

@app.route('/')
def index():
    """Homepage route with featured books"""
    featured_books = Book.query.filter(Book.stock_quantity > 0).order_by(Book.created_at.desc()).limit(8).all()
    categories = Category.query.all()
    recent_books = Book.query.filter(Book.stock_quantity > 0).order_by(Book.created_at.desc()).limit(4).all()
    return render_template('index.html', featured_books=featured_books, categories=categories, recent_books=recent_books)


@app.route('/books')
def books():
    """Browse all books with search and filter"""
    search_query = request.args.get('search', '')
    category_id = request.args.get('category', type=int)
    sort_by = request.args.get('sort', 'title')
    
    query = Book.query.filter(Book.stock_quantity > 0)
    
    # Search filter
    if search_query:
        query = query.filter(
            (Book.title.ilike(f'%{search_query}%')) |
            (Book.author.ilike(f'%{search_query}%')) |
            (Book.isbn.ilike(f'%{search_query}%'))
        )
    
    # Category filter
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    # Sorting
    if sort_by == 'price_low':
        query = query.order_by(Book.price.asc())
    elif sort_by == 'price_high':
        query = query.order_by(Book.price.desc())
    elif sort_by == 'newest':
        query = query.order_by(Book.created_at.desc())
    else:
        query = query.order_by(Book.title.asc())
    
    books = query.all()
    categories = Category.query.all()
    
    return render_template('books.html', books=books, categories=categories)


@app.route('/book/<int:book_id>')
def book_detail(book_id):
    """Book details page"""
    book = Book.query.get_or_404(book_id)
    reviews = Review.query.filter_by(book_id=book_id).order_by(Review.created_at.desc()).all()
    related_books = Book.query.filter_by(category_id=book.category_id).filter(Book.id != book_id).limit(4).all()
    
    # Calculate average rating
    avg_rating = book.get_average_rating()
    
    return render_template('book_detail.html', book=book, reviews=reviews, related_books=related_books, avg_rating=avg_rating)


@app.route('/book/add', methods=['GET', 'POST'])
@login_required
def add_book():
    """Add new book (admin)"""
    if request.method == 'POST':
        book = Book(
            title=request.form.get('title'),
            author=request.form.get('author'),
            isbn=request.form.get('isbn'),
            price=float(request.form.get('price')),
            stock_quantity=int(request.form.get('stock_quantity')),
            description=request.form.get('description'),
            publisher=request.form.get('publisher'),
            category_id=request.form.get('category_id')
        )
        db.session.add(book)
        db.session.commit()
        flash('Book added successfully!', 'success')
        return redirect(url_for('books'))
    
    categories = Category.query.all()
    return render_template('add_book.html', categories=categories)


@app.route('/book/edit/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    """Edit book (admin)"""
    book = Book.query.get_or_404(book_id)
    
    if request.method == 'POST':
        book.title = request.form.get('title')
        book.author = request.form.get('author')
        book.isbn = request.form.get('isbn')
        book.price = float(request.form.get('price'))
        book.stock_quantity = int(request.form.get('stock_quantity'))
        book.description = request.form.get('description')
        book.publisher = request.form.get('publisher')
        book.category_id = request.form.get('category_id')
        db.session.commit()
        flash('Book updated successfully!', 'success')
        return redirect(url_for('book_detail', book_id=book.id))
    
    categories = Category.query.all()
    return render_template('edit_book.html', book=book, categories=categories)


@app.route('/book/delete/<int:book_id>')
@login_required
def delete_book(book_id):
    """Delete book (admin)"""
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash('Book deleted successfully!', 'success')
    return redirect(url_for('books'))


# ==================== CATEGORY ROUTES ====================

@app.route('/categories')
def categories():
    """Browse all categories"""
    categories_list = Category.query.all()
    return render_template('categories.html', categories=categories_list)


@app.route('/category/<int:category_id>')
def category_books(category_id):
    """Books in a specific category"""
    category = Category.query.get_or_404(category_id)
    books = Book.query.filter_by(category_id=category_id).filter(Book.stock_quantity > 0).all()
    return render_template('category_books.html', category=category, books=books)


@app.route('/category/add', methods=['GET', 'POST'])
@login_required
def add_category():
    """Add new category (admin)"""
    if request.method == 'POST':
        category = Category(
            name=request.form.get('name'),
            description=request.form.get('description')
        )
        db.session.add(category)
        db.session.commit()
        flash('Category added successfully!', 'success')
        return redirect(url_for('categories'))
    
    return render_template('add_category.html')


# ==================== CART & ORDER ROUTES ====================

@app.route('/cart')
def cart():
    """Shopping cart page"""
    cart_items = []
    total = 0
    
    if 'cart' in session:
        for item in session['cart']:
            book = Book.query.get(item['book_id'])
            if book:
                subtotal = float(book.price) * item['quantity']
                cart_items.append({
                    'book': book,
                    'quantity': item['quantity'],
                    'subtotal': subtotal
                })
                total += subtotal
    
    return render_template('cart.html', cart_items=cart_items, total=total)


@app.route('/cart/add/<int:book_id>')
def add_to_cart(book_id):
    """Add item to cart"""
    quantity = int(request.args.get('quantity', 1))
    
    if 'cart' not in session:
        session['cart'] = []
    
    # Check if item already in cart
    found = False
    for item in session['cart']:
        if item['book_id'] == book_id:
            item['quantity'] += quantity
            found = True
            break
    
    if not found:
        session['cart'].append({'book_id': book_id, 'quantity': quantity})
    
    session.modified = True
    flash('Item added to cart!', 'success')
    return redirect(url_for('cart'))


@app.route('/cart/update', methods=['POST'])
def update_cart():
    """Update cart items"""
    session['cart'] = []
    for key, value in request.form.items():
        if key.startswith('quantity_'):
            book_id = int(key.split('_')[1])
            quantity = int(value)
            if quantity > 0:
                session['cart'].append({'book_id': book_id, 'quantity': quantity})
    
    session.modified = True
    flash('Cart updated!', 'success')
    return redirect(url_for('cart'))


@app.route('/cart/clear')
def clear_cart():
    """Clear shopping cart"""
    session.pop('cart', None)
    flash('Cart cleared!', 'info')
    return redirect(url_for('cart'))


@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    """Checkout process"""
    if 'cart' not in session or not session['cart']:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('books'))
    
    if request.method == 'POST':
        # Calculate total
        total = 0
        order_items = []
        
        for item in session['cart']:
            book = Book.query.get(item['book_id'])
            if book and book.stock_quantity >= item['quantity']:
                subtotal = float(book.price) * item['quantity']
                total += subtotal
                order_items.append({
                    'book': book,
                    'quantity': item['quantity'],
                    'unit_price': book.price
                })
            else:
                flash(f'Book "{book.title}" is out of stock!', 'danger')
                return redirect(url_for('cart'))
        
        # Create order
        order = Order(
            user_id=current_user.id,
            total_amount=total,
            shipping_address=request.form.get('shipping_address'),
            notes=request.form.get('notes')
        )
        db.session.add(order)
        db.session.flush()
        
        # Create order items
        for item in order_items:
            order_item = OrderItem(
                order_id=order.id,
                book_id=item['book'].id,
                quantity=item['quantity'],
                unit_price=item['unit_price']
            )
            db.session.add(order_item)
            
            # Update stock
            item['book'].stock_quantity -= item['quantity']
        
        db.session.commit()
        session.pop('cart', None)
        
        flash('Order placed successfully!', 'success')
        return redirect(url_for('order_confirmation', order_id=order.id))
    
    # Calculate total for display
    total = 0
    cart_items = []
    for item in session['cart']:
        book = Book.query.get(item['book_id'])
        if book:
            subtotal = float(book.price) * item['quantity']
            cart_items.append({
                'book': book,
                'quantity': item['quantity'],
                'subtotal': subtotal
            })
            total += subtotal
    
    return render_template('checkout.html', cart_items=cart_items, total=total)


@app.route('/order/<int:order_id>')
@login_required
def order_confirmation(order_id):
    """Order confirmation page"""
    order = Order.query.get_or_404(order_id)
    
    if order.user_id != current_user.id:
        abort(403)
    
    return render_template('order_confirmation.html', order=order)


@app.route('/orders')
@login_required
def orders():
    """User's order history"""
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.order_date.desc()).all()
    return render_template('orders.html', orders=orders)


# ==================== REVIEW ROUTES ====================

@app.route('/book/<int:book_id>/review', methods=['POST'])
@login_required
def add_review(book_id):
    """Add book review"""
    rating = int(request.form.get('rating'))
    comment = request.form.get('comment')
    
    review = Review(
        user_id=current_user.id,
        book_id=book_id,
        rating=rating,
        comment=comment
    )
    db.session.add(review)
    db.session.commit()
    
    flash('Review added successfully!', 'success')
    return redirect(url_for('book_detail', book_id=book_id))


# ==================== CONTACT ROUTE ====================

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact form page"""
    if request.method == 'POST':
        message = ContactMessage(
            name=request.form.get('name'),
            email=request.form.get('email'),
            subject=request.form.get('subject'),
            message=request.form.get('message')
        )
        db.session.add(message)
        db.session.commit()
        flash('Message sent successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('contact.html')


# ==================== ABOUT ROUTE ====================

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found_error(error):
    """404 error handler"""
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    return render_template('errors/500.html'), 500


# ==================== DATABASE INIT ====================

def create_sample_data():
    """Create sample data for testing"""
    # Create categories
    categories = [
        Category(name='Fiction', description='Fiction books and novels'),
        Category(name='Non-Fiction', description='Non-fiction and educational'),
        Category(name='Science', description='Science and technology'),
        Category(name='History', description='Historical books'),
        Category(name='Biography', description='Biographies and memoirs'),
        Category(name='Self-Help', description='Self-improvement books')
    ]
    
    for cat in categories:
        if not Category.query.filter_by(name=cat.name).first():
            db.session.add(cat)
    
    db.session.commit()
    
    # Create sample books
    sample_books = [
        Book(title='The Great Gatsby', author='F. Scott Fitzgerald', isbn='9780743273565',
             price=12.99, stock_quantity=50, description='A novel about the American Dream',
             publisher='Scribner', category_id=1),
        Book(title='To Kill a Mockingbird', author='Harper Lee', isbn='9780061120084',
             price=14.99, stock_quantity=35, description='A novel about racial injustice',
             publisher='Harper Perennial', category_id=1),
        Book(title='1984', author='George Orwell', isbn='9780451524935',
             price=11.99, stock_quantity=40, description='A dystopian social science fiction novel',
             publisher='Signet Classic', category_id=1),
        Book(title='The Art of Programming', author='Donald Knuth', isbn='9780201896831',
             price=79.99, stock_quantity=20, description='Comprehensive guide to programming',
             publisher='Addison-Wesley', category_id=3),
        Book(title='A Brief History of Time', author='Stephen Hawking', isbn='9780553380163',
             price=18.99, stock_quantity=25, description='A popular-science book on cosmology',
             publisher='Bantam Dell', category_id=3),
    ]
    
    for book in sample_books:
        if not Book.query.filter_by(isbn=book.isbn).first():
            db.session.add(book)
    
    db.session.commit()
    print("Sample data created successfully!")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_sample_data()
    app.run(debug=True)