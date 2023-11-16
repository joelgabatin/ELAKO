from flask import Blueprint,render_template, url_for, jsonify
from models import Database
db = Database()

w_home_bp = Blueprint('w_home_bp', __name__, static_folder='static', template_folder='templates')

@w_home_bp.route('/')
@w_home_bp.route('/home')
def index():

    table_name = "tbl_products"
    data = db.fetch_all_data(table_name)

    return render_template('home.html', data=data)

# FOR TESTING
@w_home_bp.route('/hello_world')
@w_home_bp.route('home/hello_world')
def hello_world():
    return "hello_world"


