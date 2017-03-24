from flask import (Blueprint,
                   Flask, 
                   flash, 
                   redirect, 
                   render_template, 
                   request, 
                   session, 
                   url_for )
from flask_login import login_required
from flask_sqlalchemy import *
import datetime

from app.scripts import verify_required
from app.models import db, PostHome, PostCar
from app.post.post_forms import HomeForm, CarForm

post_blueprint = Blueprint('post', __name__, template_folder='templates')

def apply_common_filters():
    pmin, pmax = 0, 0
    if request.args.get('pmin') and request.args.get('pmax'):
        pmin = int(re.search(r'\d+', request.args.get('pmin')).group())
        pmax = int(re.search(r'\d+', request.args.get('pmax')).group())
    
    city = ''
    if request.args.get('city'):
        city = request.args.get('city')

    return pmin, pmax, city

def apply_home_prices(pmin, pmax):
    price_min = db.session.query(db.func.min(PostHome.price)).scalar()
    price_max = db.session.query(db.func.max(PostHome.price)).scalar()
    # refactor this process; same part with apply_car_prices()
    if pmin or pmax:
        pmin_filtered = pmin
        pmax_filtered = pmax
    else: 
        pmin_filtered = price_min
        pmax_filtered = price_max

    return price_min, price_max, pmin_filtered, pmax_filtered

def apply_car_prices(pmin, pmax):
    price_min = db.session.query(db.func.min(PostCar.price)).scalar()
    price_max = db.session.query(db.func.max(PostCar.price)).scalar()
    if pmin or pmax:
        pmin_filtered = pmin
        pmax_filtered = pmax
    else: 
        pmin_filtered = price_min
        pmax_filtered = price_max

    return price_min, price_max, pmin_filtered, pmax_filtered

@post_blueprint.route('/homes', methods=['GET'])
def show_home_posts():
    try:
        pmin, pmax, city = apply_common_filters()
        price_min, price_max, pmin_filtered, pmax_filtered = apply_home_prices(pmin, pmax)
        cities = db.session.query(PostHome.city.distinct().label('city')).order_by(PostHome.city).limit(140).all()
        posts = PostHome.query.order_by(PostHome.id.desc()).limit(140)
        
        return render_template('/home_posts.html',
                               page='homes',
                               price_min=price_min,
                               price_max=price_max, 
                               pmin_filtered=pmin_filtered, 
                               pmax_filtered=pmax_filtered, 
                               cities=cities, 
                               posts=posts,
                               today=datetime.datetime.now() )         
    except:
        abort(404)

@post_blueprint.route('/cars', methods=['GET'])
def show_car_posts():
    try:
        pmin, pmax, city = apply_common_filters()
        price_min, price_max, pmin_filtered, pmax_filtered = apply_home_prices(pmin, pmax)       
        cities = db.session.query(PostCar.city.distinct().label('city')).order_by(PostCar.city).limit(100).all()
        posts = PostCar.query.order_by(PostCar.id.desc()).limit(140)
        
        return render_template('/car_posts.html',
                               page='cars',
                               price_min=price_min,
                               price_max=price_max, 
                               pmin_filtered=pmin_filtered, 
                               pmax_filtered=pmax_filtered, 
                               cities=cities, 
                               posts=posts,
                               today=datetime.datetime.now() )         
    except:
        abort(404)
    
@post_blueprint.route('/<page>/edit', methods=['GET', 'POST'])
@login_required
@verify_required
def edit_home_post(page):
    form = HomeForm()

    if request.method == 'GET':
        return render_template('home_edit.html', page=page, form=form)
    if request.method == 'POST':
        if form.validate_on_submit():
                       
            return render_template('home_edit.html', page=page, form=form)
        else:
            return render_template('home_edit.html', page=page, form=form)