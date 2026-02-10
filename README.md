# Online Bookstore - Web Application

A fully functional e-commerce website built with SQLAlchemy, Bootstrap 5, HTML, CSS, and JavaScript.

## 📁 GitHub Repository

**https://github.com/Anish00079/WEB_assignment_Anish**

## Features

- User Registration & Login
- Browse & Search Books
- Shopping Cart System
- Order Management
- Book Reviews & Ratings
- Contact Form
- Responsive Design

## Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend:** Python, SQLAlchemy
- **Database:** SQLite

## Run Locally

```bash
git clone https://github.com/Anish00079/WEB_assignment_Anish.git
cd WEB_assignment_Anish
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

## Deploy to GitHub Pages

### Option 1: Static Site (No Backend)

GitHub Pages only supports static files. To deploy here:

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/Anish00079/WEB_assignment_Anish.git
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repository on GitHub
   - Click **Settings** → **Pages** (in left sidebar)
   - Under **Source**, select **Deploy from a branch**
   - Select branch: `main` (or `gh-pages`)
   - Select folder: `/ (root)`
   - Click **Save**

3. **Your site will be live at:**
   ```
   https://anish00079.github.io/WEB_assignment_Anish/
   ```

### Option 2: Full Backend (Requires External Hosting)

For dynamic features (login, cart, orders), deploy the backend to:
- **Render.com** (Free tier available)
- **Railway.app** (Free tier available)
- **Fly.io** (Paid, but good performance)

---

Built with Bootstrap 5
