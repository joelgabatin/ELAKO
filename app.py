from flask import Flask, render_template, redirect, url_for
from config import Config
import mysql.connector

app = Flask(__name__)
app.config.from_object(Config)

try:
    # Attempt to initialize the database connection
    db_connection = mysql.connector.connect(
        host=app.config['DATABASE_HOST'],
        user=app.config['DATABASE_USER'],
        password=app.config['DATABASE_PASSWORD'],
        database=app.config['DATABASE_NAME'],
        port=app.config['DATABASE_PORT']
    )
    db_connection.close()

except mysql.connector.Error as err:
    # Handle the database connection error
    app.config['DATABASE_CONNECTED'] = False
    app.config['DATABASE_ERROR'] = str(err)  # Store the error message

else:
    app.config['DATABASE_CONNECTED'] = True

# Check if the database is connected
if app.config['DATABASE_CONNECTED']:
    # Database is connected, proceed with other routes and logic

    # Import and register your blueprints here (if not already done)
    from website.home.home_view import w_home_bp
    from website.shop.shop_view import w_shop_bp
    from website.contact.contact_view import w_contact_bp
    from website.auth.auth_view import w_auth_bp
    from website.dashboard.dashboard_view import w_dashboard_bp
    from website.wishlist.wishlist_view import w_wishlist_bp

    app.register_blueprint(w_home_bp, url_prefix='/elako/')
    app.register_blueprint(w_shop_bp, url_prefix='/elako/shop')
    app.register_blueprint(w_contact_bp, url_prefix='/elako/contact')
    app.register_blueprint(w_auth_bp, url_prefix='/elako/auth')
    app.register_blueprint(w_dashboard_bp, url_prefix='/elako/user_dashboard')
    app.register_blueprint(w_wishlist_bp, url_prefix='/elako/wishlist')

    # Admin Blueprint
    from admin.auth.auth_view import admin_auth_bp
    from admin.dashboard.dashboard_view import admin_dashboard_bp
    from admin.farmer.farmer_view import admin_farmer_bp
    from admin.product_category.product_category_view import admin_product_category_bp
    from admin.products.products_view import admin_products_bp

    app.register_blueprint(admin_auth_bp, url_prefix='/elako/auth/')
    app.register_blueprint(admin_dashboard_bp, url_prefix='/elako/admin/')
    app.register_blueprint(admin_farmer_bp, url_prefix='/elako/admin/farmer')
    app.register_blueprint(admin_product_category_bp, url_prefix='/elako/admin/product_category')
    app.register_blueprint(admin_products_bp, url_prefix='/elako/admin/product')

    # Seller Blueprint
    from seller.auth.seller_auth_view import seller_auth_bp
    from seller.dashboard.seller_dashboard_view import seller_dashboard_bp

    app.register_blueprint(seller_auth_bp, url_prefix='/elako/seller/auth')
    app.register_blueprint(seller_dashboard_bp, url_prefix='/elako/seller/dashboard')

    @app.route('/')
    def redirect_to_website():
        return redirect(url_for('w_home_bp.index'))
else:
    # Database is not connected, redirect to a database error page
    @app.route('/')
    def database_error():
        error_message = app.config.get('DATABASE_ERROR', 'Unknown database error')  # Get the error message
        return render_template('database_error.html', error_message=error_message)


# Define a custom 404 error page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
