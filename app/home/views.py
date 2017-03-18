from flask import Flask, flash, request, render_template, redirect, session, url_for, Blueprint

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
def home():
    return render_template('home.html')

# error page
@home_blueprint.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404