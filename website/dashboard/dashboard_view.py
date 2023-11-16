from flask import Blueprint, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from models import Database
db = Database()

# Create a Blueprint for the website home page
w_dashboard_bp = Blueprint('w_dashboard', __name__,
                             static_folder='static',  # Set the static folder
                             template_folder='templates'  # Set the template folder
                             )

# Define the folder where you want to store uploaded files
UPLOAD_FOLDER = 'static/website/img/product'

@w_dashboard_bp.route('/')
def index():
    return render_template('website_dashboard.html')

@w_dashboard_bp.route('/add_products', methods=['POST'])
def add_products():

    if request.method == 'POST':
        # Get form data
        products_name = request.form['products_name']
        products_old_price = request.form['products_old_price']
        products_new_price = request.form['products_new_price']
        photo = request.files['photo']


        # Securely save the uploaded file to the "joel" folder
        if photo:
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(UPLOAD_FOLDER, filename))

            # Insert the user data into the database
            data_to_insert = {
                'products_name': products_name,
                'products_old_price': products_old_price,
                'products_new_price': products_new_price,
                'products_photo': filename
            }

            # Insert data into the database using your database module
            # Replace 'database.insert_data' with your actual database function
            if db.insert_data('products_tbl', **data_to_insert):
                flash('New Product Added!', 'success')  # Flash success message
                return redirect(url_for('w_dashboard.index'))
            else:
                flash('Failed!', 'failed')  # Flash success message
                return redirect(url_for('w_dashboard.index'))

        # Redirect back to the form or another page
        return redirect(url_for('w_dashboard.index'))

    return "Invalid request method"
