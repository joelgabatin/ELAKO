from flask import Blueprint, render_template, url_for
from models import Database


w_shop_bp = Blueprint('w_shop', __name__, static_folder='static', template_folder='templates')

@w_shop_bp.route('/')
def index():
    db = Database()

    # Call the delete_data method to delete the room type
    products_data = db.join_multiple_tables(['tbl_product_categories', 'tbl_products', 'tbl_farmer_users'], ['product_cat_id', 'user_id'])

    cat_table_name = "tbl_product_categories"
    product_cat = db.fetch_all_data(cat_table_name)

    size_table_name = "tbl_product_size"
    size_cat = db.fetch_all_data(size_table_name)

    return render_template('shop.html', products_data=products_data, product_cat=product_cat, size_cat=size_cat)

# FOR TESTING
@w_shop_bp.route('/hello_world')
def hello_world():
    return "hello_world"
