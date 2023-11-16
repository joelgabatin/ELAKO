from flask import Blueprint, url_for, redirect, render_template, request, flash
from models import Database
from forms import RegistrationForm

db = Database()
w_auth_bp = Blueprint('w_auth', __name__, static_folder='static', template_folder='templates')


@w_auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('w_dashboard.index'))
    return render_template('auth_login.html')


@w_auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    email_exists = False  # Initialize email_exists to False

    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data

        # Check if the email already exists in the database
        existing_user = db.fetch_all_data('users_tbl')
        for user in existing_user:
            if user['email'] == email:
                email_exists = True  # Set email_exists to True if email exists
                flash('Email already used. Please use a different email.', 'email_error')
                break  # No need to continue checking

        if not email_exists:  # Proceed with registration if email doesn't exist
            # Insert the new user into the database
            user_data = {
                'firstname': first_name,
                'lastname': last_name,
                'email': email,
                'password': password,
            }

            if db.insert_data('users_tbl', **user_data):
                flash('Registration successful! You can now log in.', 'success')
                return redirect(url_for('w_auth.login'))  # Redirect to login page
            else:
                flash('Registration failed. Please try again later.', 'error')

    return render_template('auth_register.html', form=form, email_exists=email_exists)

