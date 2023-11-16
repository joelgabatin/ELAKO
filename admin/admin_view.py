from flask import Flask, Blueprint,render_template, request, redirect, url_for
from jinja2 import TemplateNotFound # For Debugging in -> def render_debug_template():
from models import Database # Include the database.py and create an instance -> db = Database()
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

# Create a Blueprint for the website home page
admin_bp = Blueprint('adminside', __name__,
                             static_folder='static',  # Set the static folder
                             template_folder='templates'  # Set the template folder
                             )

db = Database() # Create an instance of the Database class

@admin_bp.route('/')
def index():
    return render_template('dashboard2.html', title='Dashboard')

@admin_bp.route('/hello_world')
def hello_world():
    return "hello_world"

@admin_bp.route('/logout')
def logout():
    return render_template('logout.html', title='Logout')

@admin_bp.route('/login')
def login():
    return render_template('login.html', title='Login')

@admin_bp.route('/register')
def register():
    return render_template('register.html', title='Login')

@admin_bp.route('/viewall_farmers')
def viewall_farmers():

    farmers_table = "users_tbl"
    farmers_data = db.fetch_all_data(farmers_table)

    return render_template('viewall_farmers.html', data=farmers_data)

@admin_bp.route('/viewall_products')
def viewall_products():

    products = "products_tbl"
    data = db.fetch_all_data(products)

    return render_template('viewall_products.html', data=data)


@admin_bp.route('/viewall_products_categories')
def viewall_products_categories():

    categories = "products_categories_tbl"
    data = db.fetch_all_data(categories)
    return render_template('viewall_products_categories.html', data=data)


@admin_bp.route('/viewall_products_size')
def viewall_products_size():

    size = "products_size_tbl"
    data = db.fetch_all_data(size)

    return render_template('viewall_products_size.html', data=data)

@admin_bp.route('/add_products_categories')
def add_products_categories():
    return render_template('add_products_categories.html')

@admin_bp.route('/add_products_size')
def add_products_size():
    return render_template('add_products_size.html')

@admin_bp.route('/add_farmers')
def add_farmers():
    return render_template('add_farmers.html')

@admin_bp.route('/add_products_categories_now' , methods=['POST'])
def add_products_categories_now():

    if request.method == 'POST':

        # Get form data
        category_name = request.form['category_name']

        data_to_insert = {
            'products_cat_name': category_name
        }

        db.insert_data('products_categories_tbl', **data_to_insert)
        return redirect(url_for('adminside.viewall_products_categories'))

@admin_bp.route('/add_products_size_now' , methods=['POST'])
def add_products_size_now():

    if request.method == 'POST':

        # Get form data
        products_size = request.form['products_size']
        products_short = request.form['products_short']

        data_to_insert = {
            'products_size': products_size,
            'products_size_short': products_short
        }

        db.insert_data('products_size_tbl', **data_to_insert)
        return redirect(url_for('adminside.viewall_products_size'))


@admin_bp.route('/add_farmers_now' , methods=['POST'])
def add_farmers_now():

    if request.method == 'POST':

        # Get form data
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']

        data_to_insert = {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'password': password
        }

        db.insert_data('users_tbl', **data_to_insert)
        return redirect(url_for('adminside.viewall_farmers'))



# Route to trigger a 404 error
@admin_bp.route('/trigger_405')
def trigger_405():
    # Raise a 404 error manually
    return render_template('405_alt.html')

# Custom error handler for 404 (Not Found) errors
@admin_bp.errorhandler(404)
def page_not_found(error):
    if request.path in ['/login', '/logout', '/register']:
        return render_template('404_alt.html'), 404
    else:
        return render_template('404.html'), 404
