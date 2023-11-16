from flask import Blueprint, render_template, request, redirect, session, url_for
from auth import check_login  # Import the functions to check login session

admin_dashboard_bp = Blueprint('admin_dashboard_bp', __name__, static_folder='static', template_folder='templates')
admin_dashboard_bp.before_request(check_login)  # before request check_login function to check login session

@admin_dashboard_bp.route('/')
@admin_dashboard_bp.route('/dashboard')
def index():
   return render_template("dashboard.html")

# FOR TESTING
@admin_dashboard_bp.route('/hello_world')
def hello_world():
    return "hello_world"

