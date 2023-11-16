from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app
from models import Database
import os  # for the uploading of image. used for the os.path
from werkzeug.utils import secure_filename  # for the securing the image is not duplicated by providing unique ID
from auth import check_login  # Import the functions to check login session

admin_farmer_bp = Blueprint('admin_farmer_bp', __name__, static_folder='static',
                            template_folder='templates')
admin_farmer_bp.before_request(check_login)  # before request check_login function to check login session


# Initialize the Database class once in your application


@admin_farmer_bp.route('/view_all_farmer')
def view_all_farmer():
    db = Database()
    table_name = "tbl_farmer_users"  # Set the table name
    condition_column = "role"  # Set the column to use for deletion
    condition_value = "farmer"

    # Call the delete_data method to delete the room type
    all_farmer_data = db.select_all(table_name, condition_column, condition_value)

    # Render the template with the formatted data
    return render_template('view_all_farmer.html', all_farmer_data=all_farmer_data)


@admin_farmer_bp.route('/add_farmer', methods=['GET', 'POST'])
def add_farmer():
    # Configuration for file uploads
    UPLOAD_FOLDER = ('static/uploads/farmers')

    if request.method == 'POST':

        try:
            # Get the data from the form
            email = request.form['email']
            full_name = request.form['full-name']
            phone_number = request.form['phone-number']
            address = request.form['address']
            date_of_birth = request.form['date-of-birth']

            # Handle image upload
            if 'image' in request.files:
                image = request.files['image']

                # Ensure the directory exists, create it if necessary
                os.makedirs(UPLOAD_FOLDER, exist_ok=True)

                # Save the uploaded image with a unique name to avoid overwriting
                filename = secure_filename(image.filename)
                image.save(os.path.join(UPLOAD_FOLDER, filename))

                # Use the insert_data method to add the data to the database
                table_name = "tbl_farmer_users"
                data = {
                    "email": email,
                    "full_name": full_name,
                    "role": "none",
                    "phone_number": phone_number,
                    "address": address,
                    "profile_picture": filename,
                    "date_of_birth": date_of_birth,
                }

                db = Database()
                result = db.insert_data(table_name, **data)

                if result is True:
                    # Insert successful, you can redirect to a success page or the receptionist list page
                    flash("New Farmer added successfully", "success")
                    return redirect(url_for('admin_farmer_bp.view_all_farmer'))
                else:
                    # Insert failed, handle the error
                    flash(f"Failed to add farmer: {result}", "danger")
                    return redirect(url_for('admin_farmer_bp.view_all_farmer'))
            else:
                flash("No image file uploaded", "danger")
                return redirect(url_for('admin_farmer_bp.view_all_farmer'))
        except Exception as e:
            # Handle any other exceptions that might occur during the insertion
            flash(f"An error occurred during the insertion: {str(e)}", "danger")
            return redirect(url_for('admin_farmer_bp.view_all_farmer'))

    # Render the add_staff.html template for GET requests
    return render_template('add_farmer.html')


@admin_farmer_bp.route('/delete_farmer/<string:user_id>')
def delete_farmer(user_id):
    db = Database()
    table_name = ("tbl_farmer_users")  # Set the table name
    where_column = "user_id"  # Set the column to use for deletion
    where_value = user_id

    # Call the delete_data method to delete the room type
    result = db.delete_data(table_name, where_column, where_value)

    if result is True:
        flash(" Farmer Deleted Sucessfully", "success")
        return redirect(url_for('admin_farmer_bp.view_all_farmer'))

    else:
        flash(f"Failed To Delete Farmer: {result}", "danger")
        return redirect(url_for('admin_farmer_bp.view_all_farmer'))


@admin_farmer_bp.route('/edit_farmer/<string:user_id>', methods=['GET', 'POST'])
def edit_farmer(user_id):
    UPLOAD_FOLDER = ('static/uploads/farmers')

    if request.method == 'POST':


        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        full_name = request.form['full-name']
        phone_number = request.form['phone-number']
        gender = request.form['gender']
        address = request.form['address']
        date_of_birth = request.form['date-of-birth']
        alternative_phone = request.form['alternative-phone']
        facebook = request.form['facebook']
        instagram = request.form['instagram']
        twitter = request.form['twitter']


        table_name = "tbl_farmer_users"
        where_column = "user_id"
        where_value = user_id

        data = {
            "username": username,
            "password": password,
            "email": email,
            "full_name": full_name,
            "phone_number": phone_number,
            "gender": gender,
            "address": address,
            "date_of_birth": date_of_birth,
            "alternative_phone": alternative_phone,
            "facebook": facebook,
            "instagram": instagram,
            "twitter": twitter
        }

        db = Database()
        result = db.update_data(table_name, where_column, where_value, **data)

        if result is True:
            # Insert successful, you can redirect to a success page or the receptionist list page
            flash("Updated Successfully", "success")
            return redirect(url_for('admin_farmer_bp.view_all_farmer'))
        else:
            # Insert failed, handle the error
            flash(f"Failed To Update: {result}", "danger")
            return redirect(url_for('admin_farmer_bp.view_all_farmer'))

    else:
        # Render the add_roomtype.html template for GET requests
        db = Database()
        table_name = "tbl_farmer_users"  # Set the table name
        condition_column = "user_id"  # Set the column to use for deletion
        condition_value = user_id

        edit_user_data = db.select_all(table_name, condition_column, condition_value)

        return render_template('edit_farmer.html', edit_user_data=edit_user_data)
