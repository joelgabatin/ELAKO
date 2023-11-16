from functools import wraps
from flask import session, request, redirect, url_for

def check_login():
    if not session.get('logged_in') and not request.endpoint.startswith('admin_auth_bp.login'):
        return redirect(url_for('admin_auth_bp.login'))

def check_seller_login():
    if not session.get('seller_logged_in') and not request.endpoint.startswith('seller_auth_bp.login'):
        return redirect(url_for('seller_auth_bp.login'))
