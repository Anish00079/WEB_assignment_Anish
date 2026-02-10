# Online Bookstore - Flask Web Application

A fully functional e-commerce website for an online bookstore built with Flask, SQLAlchemy, Bootstrap 5, and modern web technologies.

## 📚 Project Overview

**Theme:** Online Bookstore (E-Commerce & Business)

This project is a complete web application that allows users to browse, search, and purchase books online. It includes user authentication, shopping cart functionality, order management, and review systems.

## 🚀 Live Demo

**PythonAnywhere Deployment:** https://yourusername.pythonanywhere.com

*Note: GitHub Pages only supports static websites. This Flask application requires a Python server. Deploy on PythonAnywhere (free) for live demo.*

## 🛠️ Technology Stack

### Core Features
- **User Authentication:** Registration, login, logout with session management
- **Browse Books:** View all books with search and filter functionality
- **Book Details:** Detailed book information with reviews
- **Shopping Cart:** Add/remove items, update quantities
- **Checkout Process:** Complete purchase with shipping information
- **Order Management:** View order history and status
- **Categories:** Browse books by category
- **Contact Form:** Send messages to the bookstore

### Advanced Features
- Password hashing with Bcrypt
- Form validation (client-side and server-side)
- Responsive design with Bootstrap 5
- Flash messages for user feedback
- Protected routes for authenticated users
- CRUD operations for books and categories

## 🛠️ Technology Stack

### Frontend
- **HTML5:** Semantic markup
- **CSS3:** Custom styling with Bootstrap 5
- **JavaScript:** Client-side validation and interactivity
- **Bootstrap 5:** Responsive grid system and UI components
- **Font Awesome:** Icons

### Backend
- **Python:** Programming language
- **Flask:** Web framework
- **Flask-SQLAlchemy:** ORM for database operations
- **Flask-Login:** User session management
- **Flask-Bcrypt:** Password hashing

### Database
- **SQLite:** Lightweight relational database
- **SQLAlchemy:** ORM for database management

## 📁 Project Structure

```
online-bookstore/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── static/                # Static files (CSS, JS, images)
├── templates/            # Jinja2 HTML templates
│   ├── base.html        # Base template with navbar and footer
│   ├── index.html       # Homepage
│   ├── books.html       # Book listing page
│   ├── book_detail.html # Individual book page
│   ├── login.html       # Login page
│   ├── register.html    # Registration page
│   ├── cart.html        # Shopping cart
│   ├── checkout.html    # Checkout page
│   ├── profile.html     # User profile
│   ├── orders.html      # Order history
│   ├── order_confirmation.html # Order confirmation
│   ├── contact.html     # Contact form
│   ├── about.html       # About page
│   ├── categories.html  # Categories listing
│   ├── category_books.html # Books by category
│   ├── edit_profile.html # Edit profile
│   ├── add_book.html    # Add new book
│   ├── edit_book.html   # Edit book
│   ├── add_category.html # Add new category
│   └── errors/          # Error pages
│       ├── 404.html
│       └── 500.html
└── instance/            # Database and instance files
    └── bookstore.db     # SQLite database
```

## 📋 Database Schema

### Tables

1. **users**
   - id (Integer, Primary Key)
   - username (String, Unique)
   - email (String, Unique)
   - password_hash (String)
   - first_name (String)
   - last_name (String)
   - address (Text)
   - phone (String)
   - created_at (DateTime)
   - updated_at (DateTime)

2. **categories**
   - id (Integer, Primary Key)
   - name (String, Unique)
   - description (Text)
   - created_at (DateTime)

3. **books**
   - id (Integer, Primary Key)
   - title (String)
   - author (String)
   - isbn (String, Unique)
   - price (Numeric)
   - stock_quantity (Integer)
   - description (Text)
   - publisher (String)
   - published_date (Date)
   - pages (Integer)
   - cover_image (String)
   - category_id (Foreign Key)
   - created_at (DateTime)
   - updated_at (DateTime)

4. **orders**
   - id (Integer, Primary Key)
   - user_id (Foreign Key)
   - order_date (DateTime)
   - total_amount (Numeric)
   - status (String)
   - shipping_address (Text)
   - notes (Text)

5. **order_items**
   - id (Integer, Primary Key)
   - order_id (Foreign Key)
   - book_id (Foreign Key)
   - quantity (Integer)
   - unit_price (Numeric)

6. **reviews**
   - id (Integer, Primary Key)
   - user_id (Foreign Key)
   - book_id (Foreign Key)
   - rating (Integer)
   - comment (Text)
   - created_at (DateTime)

7. **contact_messages**
   - id (Integer, Primary Key)
   - name (String)
   - email (String)
   - subject (String)
   - message (Text)
   - created_at (DateTime)
   - is_read (Boolean)

## 🏃‍♂️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd online-bookstore
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python app.py
   ```
   The database will be automatically created with sample data.

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your browser and navigate to: `http://127.0.0.1:5000`

## 📖 User Manual

### For Customers

1. **Registration**
   - Click "Register" in the navigation
   - Fill in the required information
   - Submit the form

2. **Login**
   - Click "Login" in the navigation
   - Enter username and password
   - Click "Login"

3. **Browsing Books**
   - Use the "Books" menu to view all books
   - Use filters to narrow down results
   - Search by title, author, or ISBN

4. **Adding to Cart**
   - Click "Add to Cart" on any book
   - View cart by clicking the cart icon

5. **Checkout**
   - Click "Proceed to Checkout"
   - Enter shipping information
   - Place your order

6. **Viewing Orders**
   - Login to your account
   - Click "My Orders" from the profile menu

### For Admin

1. **Access Admin Features**
   - Login with admin credentials
   - Navigate to book management

2. **Managing Books**
   - Add new books via "Add Book"
   - Edit existing books
   - Delete books

3. **Managing Categories**
   - Add new categories
   - Edit existing categories

## 🧪 Testing

### Test Cases

1. **User Registration**
   - Valid registration with all fields
   - Duplicate username/email handling
   - Password mismatch validation

2. **User Login**
   - Valid credentials
   - Invalid credentials
   - Session management

3. **Book Operations**
   - Browse books
   - Search functionality
   - Filter by category
   - Sort by price/title

4. **Shopping Cart**
   - Add item to cart
   - Update quantity
   - Remove item
   - Clear cart

5. **Checkout Process**
   - Valid shipping address
   - Order creation
   - Stock update

6. **Form Validation**
   - Required fields
   - Email format
   - Numeric validation
   - Length validation

## 📝 API Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Homepage |
| `/books` | GET | List all books |
| `/book/<id>` | GET | Book details |
| `/login` | GET/POST | User login |
| `/register` | GET/POST | User registration |
| `/logout` | GET | User logout |
| `/cart` | GET | View cart |
| `/cart/add/<id>` | GET | Add to cart |
| `/checkout` | GET/POST | Checkout process |
| `/orders` | GET | User orders |
| `/contact` | GET/POST | Contact form |

## 🔒 Security Features

- Password hashing with Bcrypt
- CSRF protection via Flask-WTF (can be added)
- Session-based authentication
- Input validation on all forms
- SQL injection prevention via SQLAlchemy

## 📈 Future Enhancements

- Payment gateway integration (Stripe/PayPal)
- Email notifications
- Admin dashboard
- Order tracking
- Wishlist functionality
- Social media login
- Advanced search with filters
- Book recommendations
- File upload for book covers
- User roles and permissions

## ☁️ Deployment Guide

### Deploy on PythonAnywhere (Recommended - Free)

PythonAnywhere is the easiest way to deploy Flask applications for free.

**Steps to Deploy:**

1. **Create PythonAnywhere Account**
   - Go to: https://www.pythonanywhere.com/
   - Sign up for a free account

2. **Open a Bash Console**
   - Click "Bash" in the top menu

3. **Clone the Repository**
   ```bash
git clone https://github.com/Anish00079/WEB_assignment_Anish.git
   cd WEB_assignment_Anish
   ```

4. **Create Virtual Environment**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.9 venv
   pip install -r requirements.txt
   ```

5. **Configure Web App**
   - Click "Web" in the top menu
   - Click "Add a new web app"
   - Choose "Flask" and Python version

6. **Configure WSGI File**
   - Edit the WSGI configuration file
   - Add the following:
   ```python
   import sys
   sys.path.insert(0, '/home/yourusername/WEB_assignment_Anish')
   from app import app as application
   ```

7. **Virtualenv Path**
   - Set virtualenv path to: `/home/yourusername/.virtualenvs/venv`

8. **Reload Web App**
   - Click "Reload" button

**Your site will be live at:** https://yourusername.pythonanywhere.com

### Alternative: Deploy on Render (Free)

1. Go to https://render.com and sign up
2. Connect your GitHub repository
3. Create a new Web Service
4. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

### Alternative: Deploy on Railway

1. Go to https://railway.app and sign up
2. Connect GitHub and select your repository
3. Deploy with default settings

## 📄 License

This project is for educational purposes and is open source.

## 👨‍💻 Author

- Name: Anish
- Email: anish@example.com
- Institution: LCID

## 📅 Project Timeline

- **Week 1:** Planning and Design
- **Week 2:** Database and Models
- **Week 3:** Backend Development
- **Week 4:** Frontend Development
- **Week 5:** Testing and Documentation
- **Week 6:** Final Review and Deployment

---

**Last Updated:** February 2024