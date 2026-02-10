# Online Bookstore - Complete Documentation

## A. Planning & Design Phase

### 1. Project Proposal

#### Project Title
**Online Bookstore** - A Full-Stack E-Commerce Web Application

#### Description
The Online Bookstore is a comprehensive e-commerce platform that allows users to browse, search, and purchase books online. The application features a user-friendly interface with secure authentication, shopping cart functionality, order management, and a review system. Built using Flask framework, it demonstrates modern web development practices including MVC architecture, responsive design, and database integration.

#### Target Audience
- Book readers and enthusiasts
- Students looking for academic materials
- Gift shoppers
- Collectors and hobbyists
- General consumers interested in purchasing books online

#### Problem Statement
Traditional bookstores often have limited inventory and inconvenient operating hours. Online bookstores provide 24/7 access to vast collections, competitive pricing, and doorstep delivery. However, many existing solutions lack user-friendly interfaces, secure authentication, or essential e-commerce features.

#### Objectives and Goals
1. **Primary Goal:** Create a fully functional online bookstore with all essential e-commerce features
2. **User Experience:** Provide an intuitive, responsive interface that works on all devices
3. **Security:** Implement secure user authentication and data protection
4. **Functionality:** Enable complete shopping experience from browsing to checkout
5. **Maintainability:** Follow best practices for code organization and documentation

#### Scope and Limitations
**In Scope:**
- User registration and authentication
- Book catalog with search and filtering
- Shopping cart and checkout functionality
- Order management
- Book reviews and ratings
- Contact form
- Admin capabilities for book and category management

**Out of Scope:**
- Payment gateway integration (Cash on Delivery only)
- Advanced shipping tracking
- Multi-language support
- Wishlist functionality
- Social sharing features

#### Expected Features List

**User Features:**
- User registration and login
- Browse books by category
- Search books by title, author, or ISBN
- View book details and reviews
- Add books to cart
- Manage shopping cart
- Complete checkout process
- View order history
- Write book reviews
- Edit user profile
- Contact the bookstore

**Admin Features:**
- Add new books
- Edit existing books
- Delete books
- Add new categories
- Manage categories

---

### 2. Information Architecture

#### Website Structure/Sitemap

```
Homepage (/)
├── Books (/books)
│   ├── Book Details (/book/<id>)
│   ├── Add Book (/book/add) [Auth Required]
│   └── Edit Book (/book/edit/<id>) [Auth Required]
├── Categories (/categories)
│   └── Category Books (/category/<id>)
├── Cart (/cart)
├── Checkout (/checkout) [Auth Required]
├── Orders (/orders) [Auth Required]
├── Profile (/profile) [Auth Required]
│   ├── Edit Profile (/profile/edit) [Auth Required]
│   └── Order Details (/order/<id>)
├── Contact (/contact)
├── About (/about)
├── Login (/login)
└── Register (/register)
```

#### Page Hierarchy

```
Level 1: Homepage
├── Level 2: Browse Pages
│   ├── Books Listing
│   ├── Categories Listing
│   └── Book Details
├── Level 2: User Pages
│   ├── Login/Register
│   ├── Profile
│   ├── Edit Profile
│   └── Orders
├── Level 2: Shopping Pages
│   ├── Cart
│   ├── Checkout
│   └── Order Confirmation
└── Level 2: Information Pages
    ├── Contact
    └── About
```

#### Navigation Flow
1. User lands on Homepage
2. Can navigate to Books or Categories
3. Selects a book to view details
4. Adds book to cart
5. Proceeds to cart to review items
6. Clicks checkout (redirects to login if not authenticated)
7. Completes checkout process
8. Receives order confirmation
9. Can view order history in profile

---

### 3. Wireframes & UI Design

#### Color Scheme
- **Primary:** #2c3e50 (Dark Blue)
- **Secondary:** #e74c3c (Red)
- **Accent:** #3498db (Blue)
- **Background:** #f8f9fa (Light Gray)
- **Text:** #2c3e50 (Dark Gray)

#### Typography
- **Primary Font:** 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif
- **Heading Font:** 'Segoe UI', sans-serif
- **Font Size:** Base 16px, Headings varying sizes

#### Responsive Design Considerations
- **Mobile:** Single column layout, collapsible navigation
- **Tablet:** Two column layouts, adjusted padding
- **Desktop:** Multi-column layouts, full feature display

#### UI/UX Principles Applied
1. **Consistency:** Uniform design elements across all pages
2. **Feedback:** Visual feedback for user actions (hover states, transitions)
3. **Accessibility:** Semantic HTML, proper contrast, keyboard navigation
4. **Clarity:** Clear calls-to-action, descriptive labels
5. **Efficiency:** Quick access to frequently used features

---

### 4. Database Design

#### Entity-Relationship (ER) Diagram

```
users (1) ───────< (N) orders ───────< (N) order_items >────── (1) books
  │                                          │
  │                                          │
  └──────< (N) reviews >────── (1) ─────────┘
                │
                v
          (1) categories
```

#### Database Schema

**users Table**
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique user ID |
| username | VARCHAR(50) | UNIQUE, NOT NULL | Username for login |
| email | VARCHAR(100) | UNIQUE, NOT NULL | User email address |
| password_hash | VARCHAR(128) | NOT NULL | Hashed password |
| first_name | VARCHAR(50) | NULL | User's first name |
| last_name | VARCHAR(50) | NULL | User's last name |
| address | TEXT | NULL | Shipping address |
| phone | VARCHAR(20) | NULL | Phone number |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Account creation date |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Last update date |

**categories Table**
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique category ID |
| name | VARCHAR(100) | UNIQUE, NOT NULL | Category name |
| description | TEXT | NULL | Category description |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Creation date |

**books Table**
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique book ID |
| title | VARCHAR(200) | NOT NULL | Book title |
| author | VARCHAR(100) | NOT NULL | Author name |
| isbn | VARCHAR(20) | UNIQUE, NOT NULL | ISBN number |
| price | NUMERIC(10,2) | NOT NULL | Book price |
| stock_quantity | INTEGER | NOT NULL DEFAULT 0 | Available stock |
| description | TEXT | NULL | Book description |
| publisher | VARCHAR(100) | NULL | Publisher name |
| published_date | DATE | NULL | Publication date |
| pages | INTEGER | NULL | Number of pages |
| cover_image | VARCHAR(255) | NULL | Cover image path |
| category_id | INTEGER | FOREIGN KEY | References categories.id |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Creation date |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Last update date |

**orders Table**
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique order ID |
| user_id | INTEGER | FOREIGN KEY NOT NULL | References users.id |
| order_date | DATETIME | DEFAULT CURRENT_TIMESTAMP | Order date |
| total_amount | NUMERIC(10,2) | NOT NULL | Order total |
| status | VARCHAR(20) | DEFAULT 'pending' | Order status |
| shipping_address | TEXT | NULL | Shipping address |
| notes | TEXT | NULL | Order notes |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Creation date |
| updated_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Last update date |

**order_items Table**
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique item ID |
| order_id | INTEGER | FOREIGN KEY NOT NULL | References orders.id |
| book_id | INTEGER | FOREIGN KEY NOT NULL | References books.id |
| quantity | INTEGER | NOT NULL DEFAULT 1 | Quantity ordered |
| unit_price | NUMERIC(10,2) | NOT NULL | Price at order time |

**reviews Table**
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique review ID |
| user_id | INTEGER | FOREIGN KEY NOT NULL | References users.id |
| book_id | INTEGER | FOREIGN KEY NOT NULL | References books.id |
| rating | INTEGER | NOT NULL | Rating 1-5 |
| comment | TEXT | NULL | Review text |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Review date |

**contact_messages Table**
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique message ID |
| name | VARCHAR(100) | NOT NULL | Sender name |
| email | VARCHAR(100) | NOT NULL | Sender email |
| subject | VARCHAR(200) | NOT NULL | Message subject |
| message | TEXT | NOT NULL | Message content |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Message date |
| is_read | BOOLEAN | DEFAULT FALSE | Read status |

#### Relationship Definitions
- **User-Order:** One-to-Many (One user can have many orders)
- **Order-OrderItem:** One-to-Many (One order can have many items)
- **OrderItem-Book:** Many-to-One (Many items can reference one book)
- **Book-Category:** Many-to-One (Many books can belong to one category)
- **User-Review:** One-to-Many (One user can write many reviews)
- **Book-Review:** One-to-Many (One book can have many reviews)

#### Sample Data
- Categories: Fiction, Non-Fiction, Science, History, Biography, Self-Help
- Books: Sample titles like "The Great Gatsby", "1984", "To Kill a Mockingbird"
- Users: Sample user accounts for testing

---

### 5. Technical Specification

#### Technology Stack Details

**Frontend:**
- HTML5 for semantic markup
- CSS3 for styling with custom properties
- Bootstrap 5 for responsive grid and components
- JavaScript (Vanilla) for interactivity
- Font Awesome for icons

**Backend:**
- Python 3.8+ as programming language
- Flask 2.0+ as web framework
- Flask-SQLAlchemy for ORM
- Flask-Login for authentication
- Flask-Bcrypt for password hashing
- Jinja2 for templating
- Werkzeug for utilities

**Database:**
- SQLite for development
- SQLAlchemy ORM

**Development Tools:**
- VS Code as IDE
- Git for version control
- Chrome DevTools for debugging

#### Development Environment
- **OS:** Windows 11 / macOS / Linux
- **Python:** 3.8 or higher
- **Package Manager:** pip
- **Virtual Environment:** venv
- **Code Editor:** VS Code with Python extension

#### Project Timeline and Milestones

**Week 1: Planning & Design**
- Day 1-2: Project proposal and requirements analysis
- Day 3-4: Database design and schema creation
- Day 5-7: UI/UX design and wireframes

**Week 2: Database & Backend**
- Day 1-2: Set up Flask project and database models
- Day 3-4: Implement user authentication
- Day 5-7: Create CRUD operations for books and categories

**Week 3: Frontend Development**
- Day 1-3: Build HTML templates with Bootstrap
- Day 4-5: Add JavaScript for interactivity
- Day 6-7: Implement form validation

**Week 4: Integration & Testing**
- Day 1-3: Integrate frontend with backend
- Day 4-5: Test all features
- Day 6-7: Fix bugs and polish UI

**Week 5: Documentation**
- Day 1-3: Write code documentation
- Day 4-5: Create README and user manual
- Day 6-7: Prepare submission materials

#### Resource Requirements
- **Hardware:** Computer with internet access
- **Software:** Python, code editor, web browser
- **Time:** Approximately 40-50 hours total

---

## B. Implementation & Development

### Frontend Development

#### HTML Structure
- Semantic HTML5 elements throughout
- Proper document structure (doctype, head, body)
- Clean and organized code
- Accessibility features (alt text, labels, ARIA)

#### CSS Styling & Layout
- Responsive design implementation
- Modern layout techniques (Flexbox, Grid)
- Bootstrap 5 integration
- Cross-browser compatibility
- Visual appeal and consistency

#### JavaScript Interactivity
- Form validation on client side
- Dynamic content manipulation
- Event handling
- Interactive features (modals, dropdowns, etc.)
- Error-free execution

### Backend Development

#### Flask Application Structure
- Proper MVC architecture
- Clean route definitions
- URL handling and redirects
- Flash messages implementation

#### Database Operations
- CRUD functionality
- Proper model relationships
- Data validation
- Query optimization

#### User Authentication
- Registration system
- Login/logout functionality
- Session management
- Password hashing
- Protected routes

---

## C. Testing, Documentation & Deployment

### Testing Documentation

#### Test Cases

**1. User Registration Test**
| Test Case | Expected Result | Status |
|-----------|-----------------|--------|
| Valid registration | User account created, redirect to login | ✓ |
| Duplicate username | Error message displayed | ✓ |
| Invalid email format | Validation error | ✓ |
| Password mismatch | Validation error | ✓ |

**2. User Login Test**
| Test Case | Expected Result | Status |
|-----------|-----------------|--------|
| Valid credentials | Login successful, redirect to home | ✓ |
| Invalid username | Error message displayed | ✓ |
| Invalid password | Error message displayed | ✓ |

**3. Book Browsing Test**
| Test Case | Expected Result | Status |
|-----------|-----------------|--------|
| View all books | All books displayed | ✓ |
| Search by title | Matching books shown | ✓ |
| Filter by category | Category books displayed | ✓ |
| Sort by price | Books sorted correctly | ✓ |

**4. Shopping Cart Test**
| Test Case | Expected Result | Status |
|-----------|-----------------|--------|
| Add item to cart | Item added successfully | ✓ |
| Update quantity | Quantity updated | ✓ |
| Remove item | Item removed from cart | ✓ |
| Clear cart | All items removed | ✓ |

**5. Checkout Process Test**
| Test Case | Expected Result | Status |
|-----------|-----------------|--------|
| Complete checkout | Order created, redirect to confirmation | ✓ |
| Empty cart | Error message shown | ✓ |
| Invalid address | Validation error | ✓ |

### Browser Compatibility Testing
- Chrome: ✓
- Firefox: ✓
- Safari: ✓
- Edge: ✓

### Responsive Design Testing
- Desktop (1920px): ✓
- Tablet (768px): ✓
- Mobile (375px): ✓

---

## GitHub Repository Setup

### Repository Structure
```
online-bookstore/
├── app.py                 # Main application file
├── models.py              # Database models
├── requirements.txt       # Dependencies
├── README.md              # Main documentation
├── DOCUMENTATION.md       # Detailed documentation
├── .gitignore             # Git ignore rules
├── static/                # Static files
└── templates/             # HTML templates
    ├── base.html
    ├── index.html
    ├── books.html
    ├── book_detail.html
    ├── login.html
    ├── register.html
    ├── cart.html
    ├── checkout.html
    ├── profile.html
    ├── orders.html
    ├── order_confirmation.html
    ├── contact.html
    ├── about.html
    ├── categories.html
    ├── category_books.html
    ├── edit_profile.html
    ├── add_book.html
    ├── edit_book.html
    ├── add_category.html
    └── errors/
        ├── 404.html
        └── 500.html
```

### Commit History
1. Initial project setup
2. Create database models
3. Implement user authentication
4. Add book CRUD operations
5. Create category management
6. Build shopping cart
7. Implement checkout process
8. Add order management
9. Create book review system
10. Build frontend templates
11. Add form validation
12. Implement responsive design
13. Add contact form
14. Create about page
15. Final testing and documentation

---

## User Manual

### Installation from GitHub

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/online-bookstore.git
   cd online-bookstore
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open browser at `http://127.0.0.1:5000`

### User Guide

**Registration:**
1. Click "Register" in the navigation
2. Fill in username, email, password
3. Submit form

**Shopping:**
1. Browse books or search
2. Click "Add to Cart"
3. Review cart items
4. Click "Proceed to Checkout"
5. Enter shipping address
6. Place order

**Order Tracking:**
1. Login to account
2. Click "My Orders" in dropdown
3. View order status

### Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| Application won't start | Check Python version, install dependencies |
| Database errors | Delete instance/bookstore.db and restart |
| Pages not loading | Check Flask is running, correct port |
| CSS not loading | Clear browser cache |
| Login issues | Check credentials, clear cookies |

---

## Conclusion

This Online Bookstore project demonstrates full-stack web development skills using Flask, SQLAlchemy, Bootstrap 5, and modern web practices. The application provides a complete e-commerce experience with user authentication, shopping cart functionality, order management, and review systems.

All technical requirements have been met:
- ✓ Responsive design with HTML5, CSS3, Bootstrap 5
- ✓ Interactive features with JavaScript
- ✓ Flask framework with Jinja2 templating
- ✓ Flask-SQLAlchemy for database operations
- ✓ User authentication and session management
- ✓ Full CRUD operations
- ✓ 7 related database tables with proper relationships
- ✓ Form validation (client-side and server-side)
- ✓ 10+ interconnected pages

---

**Document Version:** 1.0
**Last Updated:** February 2024
**Author:** Anish