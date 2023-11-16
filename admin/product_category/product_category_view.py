from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app
from models import Database
import os  # for the uploading of image. used for the os.path
from werkzeug.utils import secure_filename  # for the securing the image is not duplicated by providing unique ID
from auth import check_login  # Import the functions to check login session

admin_product_category_bp = Blueprint('admin_product_category_bp', __name__, static_folder='static',
                            template_folder='templates')
admin_product_category_bp.before_request(check_login)  # before request check_login function to check login session


@admin_product_category_bp.route('/viewall_products_categories')
def viewall_products_categories():

    table = "tbl_product_categories"
    db = Database()
    data = db.fetch_all_data(table)
    return render_template('view_all_product_category.html', data=data)

@admin_product_category_bp.route('/add_products_categories' , methods=['GET', 'POST'])
def add_products_categories():

    if request.method == 'POST':
        db = Database()
        # Get form data
        category_name = request.form['category_name']
        category_description = request.form['category_description']

        table_name = "tbl_product_categories"
        data_to_insert = {
            'product_cat_name': category_name,
            "product_cat_description": category_description
        }

        result = db.insert_data(table_name, **data_to_insert)

        if result is True:
            # Insert successful, you can redirect to a success page or the receptionist list page
            flash("New product category added successfully", "success")
            return redirect(url_for('admin_product_category_bp.viewall_products_categories'))
        else:
            # Insert failed, handle the error
            flash(f"Failed to add product category: {result}", "danger")
            return redirect(url_for('admin_product_category_bp.viewall_products_categories'))

    return render_template('add_products_categories.html')

@admin_product_category_bp.route('/edit_product_category/<string:cat_id>', methods=['GET', 'POST'])
def edit_product_category(cat_id):

    if request.method == 'POST':

        category_name = request.form['category_name']
        category_description = request.form['category_description']

        table_name = "tbl_product_categories"
        where_column = "product_cat_id"
        where_value = cat_id

        data = {
            "product_cat_name": category_name,
            "product_cat_description": category_description
        }

        db = Database()
        result = db.update_data(table_name, where_column, where_value, **data)

        if result is True:
            # Insert successful, you can redirect to a success page or the receptionist list page
            flash("Updated Successfully", "success")
            return redirect(url_for('admin_product_category_bp.viewall_products_categories'))
        else:
            # Insert failed, handle the error
            flash(f"Failed To Update: {result}", "danger")
            return redirect(url_for('admin_product_category_bp.viewall_products_categories'))
    else:
        db = Database()
        table_name = "tbl_product_categories"  # Set the table name
        condition_column = "product_cat_id"  # Set the column to use for deletion
        condition_value = cat_id

        edit_product_category_data = db.select_all(table_name, condition_column, condition_value)

        return render_template('edit_product_category.html', edit_product_category_data=edit_product_category_data)

@admin_product_category_bp.route('/delete_product_category/<string:cat_id>', methods=['GET', 'POST'])
def delete_product_category(cat_id):
    db = Database()
    table_name = ("tbl_product_categories")  # Set the table name
    where_column = "product_cat_id"  # Set the column to use for deletion
    where_value = cat_id

    # Call the delete_data method to delete the room type
    result = db.delete_data(table_name, where_column, where_value)

    if result is True:
        flash("Deleted Sucessfully", "success")
        return redirect(url_for('admin_product_category_bp.viewall_products_categories'))

    else:
        flash(f"Failed To Delete: {result}", "danger")
        return redirect(url_for('admin_product_category_bp.viewall_products_categories'))
