from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data
users = {
    "testuser": "password123"
}

@app.route('/')
def home():
    return render_template('loginf.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return redirect(url_for('main_page'))
    else:
        return "Invalid credentials", 401

@app.route('/main_page')
def main_page():
    return "Welcome to the main page!"

if __name__ == '__main__':
    app.run(debug=True)
