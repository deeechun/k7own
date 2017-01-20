from flask import Flask, flash, request, render_template, redirect, session, url_for, Blueprint

home_blueprint = Blueprint('home', __name__, template_folder='templates')

@home_blueprint.route('/')
def home():
    return render_template('/home.html')

