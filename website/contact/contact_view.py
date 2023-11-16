from flask import Blueprint, render_template, url_for
from models import Database
db = Database()

w_contact_bp = Blueprint('w_contact', __name__, static_folder='static', template_folder='templates')


@w_contact_bp.route('/')
def index():
    table_name = "contactus_tbl"
    data = db.fetch_all_data(table_name)
    return render_template('contact.html', data=data)

@w_contact_bp.route('/hello_world')
def hello_world():
    return "hello_world"
