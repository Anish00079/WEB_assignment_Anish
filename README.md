# Online Bookstore - Flask Web Application

A fully functional e-commerce website built with Flask, SQLAlchemy, Bootstrap 5, HTML, CSS, and JavaScript.

## 🌐 Live Demo

**GitHub Repository:** https://github.com/Anish00079/WEB_assignment_Anish

**Deployed URL:** [Deploy on Render/Railway]()

## Features

✅ User Registration & Login  
✅ Browse & Search Books  
✅ Shopping Cart System  
✅ Order Management  
✅ Book Reviews & Ratings  
✅ Contact Form  
✅ Responsive Design  

## Tech Stack

| Frontend | Backend | Database |
|----------|---------|----------|
| HTML5 | Flask | SQLite |
| CSS3 | Flask-SQLAlchemy | |
| JavaScript | Flask-Login | |
| Bootstrap 5 | Flask-Bcrypt | |

## Quick Start (Local)

```bash
# Clone the repository
git clone https://github.com/Anish00079/WEB_assignment_Anish.git
cd WEB_assignment_Anish

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Open browser at http://127.0.0.1:5000
```

## 🚀 Deploy for Free (Git-based)

### Option 1: Render (Recommended)
1. Go to https://render.com and sign up with GitHub
2. Click "New Web Service"
3. Connect your GitHub repository
4. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Click "Create Web Service"

### Option 2: Railway
1. Go to https://railway.app and sign up with GitHub
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Click "Deploy"

### Option 3: Cyclic
1. Go to https://cyclic.sh and sign up with GitHub
2. Click "Link Your Own"
3. Select your repository
4. Click "Deploy"

## Project Structure

```
WEB_assignment_Anish/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── static/
│   ├── css/styles.css    # Custom CSS
│   └── js/main.js        # Custom JavaScript
└── templates/            # HTML templates (20+ pages)
    ├── base.html
    ├── index.html
    ├── books.html
    ├── login.html
    ├── register.html
    ├── cart.html
    └── ...
```

## Pages

- Homepage, Books, Book Details
- Login, Register, Profile
- Cart, Checkout, Orders
- Contact, About
- Categories, and more...

---

**Built with ❤️ using Flask, Bootstrap 5, and SQLite**
