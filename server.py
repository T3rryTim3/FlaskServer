from flask import Flask, request, render_template, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "#hjgGJ$%^&%$GN$n4gm"
app.permanent_session_lifetime = timedelta(hours=5)

data = []

#* Run server: $ flask --app server run --debug
# TODO: Create git repository and push to github
@app.route('/hi', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return "<p>Hello, World!</p>"
    elif request.method == 'POST':
        data.append("Woo")
        return data

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form["nm"]
        session['user'] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        else:
            return render_template('login.html')
@app.route('/user')
def user():
    if "user" in session:
        print("User in session!")
        user = session["user"]
        return redirect(url_for('home'))
    else:
        print("No user found!")
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html')

@app.route('/requestdata')
def request_data():
    return [request.path, request.method, request.args, request.form]

@app.route('/admin')
def admin():
    return redirect(url_for('hello', name='Admin'))
