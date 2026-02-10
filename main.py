from flask import Flask, render_template
from database import get_db_connection, init_db

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)