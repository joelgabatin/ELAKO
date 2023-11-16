from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app
from models import Database
import os  # for the uploading of image. used for the os.path
from werkzeug.utils import secure_filename  # for the securing the image is not duplicated by providing unique ID
from auth import check_seller_login  # Import the functions to check login session

seller_product_bp = Blueprint('seller_product_bp', __name__, static_folder='static',
                            template_folder='templates')
seller_product_bp.before_request(check_seller_login)  # before request check_login function to check login session


# Initialize the Database class once in your application
@seller_product_bp.route('/view_all_products')
def view_all_farmer():
    db = Database()
    table_name = "tbl_users"  # Set the table name
    condition_column = "role"  # Set the column to use for deletion
    condition_value = "farmer"

    # Call the delete_data method to delete the room type
    all_farmer_data = db.select_all(table_name, condition_column, condition_value)

    # Render the template with the formatted data
    return render_template('view_all_farmer.html', all_farmer_data=all_farmer_data)


