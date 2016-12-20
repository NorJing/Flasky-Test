from flask import Flask, render_template, json, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"  # return a string

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # if login has issue
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/register_successfully')
def register_successfully():
    print "Register successfully"  # return a string
    return redirect(url_for('login'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    error = None
    if request.method == 'POST':
        if request.form['username'] == '' or request.form['password'] == '':
            error = "Register wrong. Miss username or password"
        else:
            info = "Register successfully"
            return redirect(url_for('register_successfully'))
    return render_template('register.html', error=error)

if __name__ == "__main__":
    app.run()
