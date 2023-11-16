from flask import Blueprint, render_template, request, redirect, session, url_for
from auth import check_seller_login  # Import the functions to check login session

seller_dashboard_bp = Blueprint('seller_dashboard_bp', __name__, static_folder='static', template_folder='templates')
seller_dashboard_bp.before_request(check_seller_login)  # before request check_login function to check login session

@seller_dashboard_bp.route('/')
def index():
   return render_template("seller_dashboard.html")

# FOR TESTING
@seller_dashboard_bp.route('/hello_world')
def hello_world():
    return "hello_world"

