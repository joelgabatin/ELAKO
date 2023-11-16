from flask import Blueprint, render_template, url_for

# Create a Blueprint for the website home page
w_wishlist_bp = Blueprint('w_wishlist', __name__,
                             static_folder='static',  # Set the static folder
                             template_folder='templates'  # Set the template folder
                             )

@w_wishlist_bp.route('/')
def index():
    return render_template("wishlist.html")

@w_wishlist_bp.route('/hello_world')
def hello_world():
    return "hello_world"

@w_wishlist_bp.errorhandler(404)
def page_not_found(error):
    return render_template('website_404.html'), 404
