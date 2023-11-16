from flask import Blueprint, render_template, url_for

# Create a Blueprint for the website home page
website_about_bp = Blueprint('website_about', __name__,
                             static_folder='static',  # Set the static folder
                             template_folder='templates'  # Set the template folder
                             )

@website_about_bp.route('/')
def index():

    year = 2024

    return render_template("dashboard2.html", current_year=year)

@website_about_bp.route('/hello_world')
def hello_world():
    return "hello_world"

@website_about_bp.errorhandler(404)
def page_not_found(error):
    return render_template('website_404.html'), 404
