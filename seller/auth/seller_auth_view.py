from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from models import Database

seller_auth_bp = Blueprint('seller_auth_bp', __name__, static_folder='static', template_folder='templates')


@seller_auth_bp.route('/logout')
def logout():
    session.pop('seller_logged_in', None)
    return render_template("seller_login.html")

@seller_auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['emailaddress']
        password = request.form['password']

        # Call your Database model to check if the username and password exist
        db = Database()

        # You may need to modify the method name according to your model's structure
        user = db.get_seller_user_by_username(username)

        if user is not None and user['password'] == password:
            # Valid credentials, set the user session
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            session['user_role'] = user['role']
            session['seller_logged_in'] = True

            flash("Login successful", "success")
            return redirect(url_for('seller_dashboard_bp.index'))  # Redirect to the dashboard or desired page after login
        else:
            flash("Invalid username or password", "danger")

    return render_template('seller_login.html')

@seller_auth_bp.route('/signup')
def signup():
    return render_template("signup.html")

@seller_auth_bp.route('/hello_world')
def hello_world():
    return "hello_world"
