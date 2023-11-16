from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app
from models import Database
import os  # for the uploading of image. used for the os.path
from werkzeug.utils import secure_filename  # for the securing the image is not duplicated by providing unique ID
from auth import check_login  # Import the functions to check login session

admin_products_bp = Blueprint('admin_products_bp', __name__, static_folder='static',
                            template_folder='templates')
admin_products_bp.before_request(check_login)  # before request check_login function to check login session


# Initialize the Database class once in your application


@admin_products_bp.route('/view_all_farmer')
def view_all_products():
    db = Database()

    # Call the delete_data method to delete the room type
    all_products_data = db.join_multiple_tables(['tbl_product_categories', 'tbl_products', 'tbl_farmer_users'], ['product_cat_id', 'user_id'])

    # Render the template with the formatted data
    return render_template('view_all_products.html', all_products_data=all_products_data)


@admin_products_bp.route('/add_products', methods=['GET', 'POST'])
def add_products():
    # Configuration for file uploads
    UPLOAD_FOLDER = ('static/uploads')

    if request.method == 'POST':

        try:

            farmer_id = request.form[('farmer_id')]
            product_name = request.form['product_name']
            product_category_id = request.form['product_category_id']
            product_description = request.form['product_description']

            # Handle image upload
            if 'image' in request.files:
                image = request.files['image']

                # Ensure the directory exists, create it if necessary
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)

                # Save the uploaded image with a unique name to avoid overwriting
                filename = secure_filename(image.filename)
                image.save(os.path.join(UPLOAD_FOLDER, filename))

                # Use the insert_data method to add the data to the database
                table_name = "tbl_products"
                data = {
                    "product_cat_id": product_category_id,
                    "user_id": farmer_id,
                    "product_name": product_name,
                    "product_description": product_description,
                    "product_photo": filename
                }

                db = Database()
                result = db.insert_data(table_name, **data)

                if result is True:
                    # Insert successful, you can redirect to a success page or the receptionist list page
                    flash("New product added successfully", "success")
                    return redirect(url_for('admin_products_bp.view_all_products'))
                else:
                    # Insert failed, handle the error
                    flash(f"Failed to add product: {result}", "danger")
                    return redirect(url_for('admin_products_bp.view_all_products'))
            else:
                flash("No image file uploaded", "danger")
                return redirect(url_for('admin_products_bp.view_all_products'))
        except Exception as e:
            # Handle any other exceptions that might occur during the insertion
            flash(f"An error occurred during the insertion: {str(e)}", "danger")
            return redirect(url_for('admin_products_bp.view_all_products'))

    # Render the add_staff.html template for GET requests

    db = Database()
    all_product_category_data = db.select_all("tbl_product_categories")
    return render_template('add_products.html', all_product_category_data=all_product_category_data)


@admin_products_bp.route('/delete_product/<string:product_id>')
def delete_product(product_id):
    db = Database()
    table_name = ("tbl_products")  # Set the table name
    where_column = "product_id"  # Set the column to use for deletion
    where_value = product_id

    # Call the delete_data method to delete the room type
    result = db.delete_data(table_name, where_column, where_value)

    if result is True:
        flash(" Product deleted sucessfully", "success")
        return redirect(url_for('admin_products_bp.view_all_products'))

    else:
        flash(f"Failed to delete product: {result}", "danger")
        return redirect(url_for('admin_products_bp.view_all_products'))



@admin_products_bp.route('/edit_product/<string:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    UPLOAD_FOLDER = ('static/uploads/farmers')

    if request.method == 'POST':

        image = request.files['image']
        farmer_id = request.form[('farmer_id')]
        product_name = request.form['product_name']
        product_category_id = request.form['product_category_id']
        product_description = request.form['product_description']

        # Handle image upload
        if image and image.filename:

            # Ensure the directory exists, create it if necessary
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)

            # Save the uploaded image with a unique name to avoid overwriting
            filename = secure_filename(image.filename)
            image.save(os.path.join(UPLOAD_FOLDER, filename))

            # Use the insert_data method to add the data to the database
            table_name = "tbl_products"
            where_column = "product_id"
            where_value = product_id

            data = {
                "product_cat_id": product_category_id,
                "user_id": farmer_id,
                "product_name": product_name,
                "product_description": product_description,
                "product_photo": filename
            }

            db = Database()
            result = db.update_data(table_name, where_column, where_value, **data)

            if result is True:
                # Insert successful, you can redirect to a success page or the receptionist list page
                flash("Product updated successfully", "success")
                return redirect(url_for('admin_products_bp.view_all_products'))
            else:
                # Insert failed, handle the error
                flash(f"Failed to update product: {result}", "danger")
                return redirect(url_for('admin_products_bp.view_all_products'))
        else:
            # Use the insert_data method to add the data to the database
            table_name = "tbl_products"
            where_column = "product_id"
            where_value = product_id

            data = {
                "product_cat_id": product_category_id,
                "user_id": farmer_id,
                "product_name": product_name,
                "product_description": product_description
            }

            db = Database()
            result = db.update_data(table_name, where_column, where_value, **data)

            if result is True:
                # Update successful, you can redirect to a success page or the room type list page
                flash("Product updated sucessfully", "success")
                return redirect(url_for('admin_products_bp.view_all_products'))
            else:
                # Update failed, handle the error
                flash(f"Failed to update product: {result}", "danger")
                return redirect(url_for('admin_products_bp.view_all_products'))
    else:
        # Render the add_roomtype.html template for GET requests
        db = Database()
        table_name = "tbl_products"  # Set the table name
        condition_column = "product_id"  # Set the column to use for deletion
        condition_value = product_id

        edit_product_data = db.select_all(table_name, condition_column, condition_value)

        all_product_category_data = db.select_all("tbl_product_categories")

        return render_template('edit_products.html', edit_product_data=edit_product_data, all_product_category_data=all_product_category_data)
