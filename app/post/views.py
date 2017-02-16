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

from app import db
from app.scripts import verify_required
from app.models import PostHome, PostCar
from app.post.edit_forms import HomeForm

post_blueprint = Blueprint('post', __name__, template_folder='templates')

def process_common_filters():
    pmin, pmax = 0, 0
    if request.args.get('pmin') and request.args.get('pmax'):
        pmin = int(re.search(r'\d+', request.args.get('pmin')).group())
        pmax = int(re.search(r'\d+', request.args.get('pmax')).group())
    
    city = ''
    if request.args.get('city'):
        city = request.args.get('city')

    return pmin, pmax, city

def process_home_filters():
    beds, baths = 0, 0
    if request.args.get('beds') and request.args.get('baths'):
        beds = request.args.get('beds')
        baths = request.args.get('baths')

    return beds, baths

def process_car_filters():
    year, make, model, mileage = 0, '', '', 0
    if request.args.get('year'):
        year = request.args.get('year')
        make = request.args.get('make')
        model = request.args.get('model')
        mileage = request.args.get('mileage')

    return year, make, model, mileage

def process_home_prices(pmin, pmax):
    price_min = db.session.query(db.func.min(PostHome.price)).scalar()
    price_max = db.session.query(db.func.max(PostHome.price)).scalar()
    # refactor this process; same part with process_car_prices()
    if pmin or pmax:
        pmin_filtered = pmin
        pmax_filtered = pmax
    else: 
        pmin_filtered = price_min
        pmax_filtered = price_max

    return price_min, price_max, pmin_filtered, pmax_filtered

def process_car_prices(pmin, pmax):
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
def home_posts():
    try:
        category= 'test'

        pmin, pmax, city = process_common_filters()
        beds, baths = process_home_filters()
        price_min, price_max, pmin_filtered, pmax_filtered = process_home_prices(pmin, pmax)
        cities = db.session.query(PostHome.city.distinct().label('city')).order_by(PostHome.city).limit(100).all()
        
        posts = (PostHome.query
                 .filter(PostHome.price >= pmin_filtered)
                 .filter(PostHome.price <= pmax_filtered)
                 .filter(PostHome.city.contains(city))
                 .filter(PostHome.bedrooms >= beds)
                 .filter(PostHome.bathrooms >= baths)
                 .order_by(PostHome.id.desc()) )
        
        return render_template('/home_posts.html',
                               page='homes',
                               category=category,
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
def car_posts():
    try:
        category= 'test'

        pmin, pmax, city = process_common_filters()
        year, make, model, mileage = process_car_filters()
        price_min, price_max, pmin_filtered, pmax_filtered = process_home_prices(pmin, pmax)       
        cities = db.session.query(PostCar.city.distinct().label('city')).order_by(PostCar.city).limit(100).all()
        
        posts = (PostCar.query
                 .filter(PostCar.price >= pmin_filtered)
                 .filter(PostCar.price <= pmax_filtered)
                 .filter(PostCar.city.contains(city))
                 .filter(PostCar.year >= year)
                 .filter(PostCar.make >= make)
                 .filter(PostCar.model >= model)
                 .filter(PostCar.mileage >= mileage)
                 .order_by(PostCar.id.desc()) )
        
        return render_template('/car_posts.html',
                               page='cars',
                               category=category,
                               price_min=price_min,
                               price_max=price_max, 
                               pmin_filtered=pmin_filtered, 
                               pmax_filtered=pmax_filtered, 
                               cities=cities, 
                               posts=posts,
                               today=datetime.datetime.now() )         
    except:
        abort(404)
    
@post_blueprint.route('/<category>/<int:post_id>/view')
def get_post(category, post_id):
    # update post.viewed count
    post = PostHome.query.filter(PostHome.id==post_id).first()
    post.viewed += 1
    db.session.commit()
    
    price_deco = ''
    if category in ['rent','homestay']:
        price_deco = '월'
    elif category=='bnb':
        price_deco = '일'
    
    return render_template(
        '/view.html', 
        category=category,
        post=post,
        price_deco=price_deco,
        today=datetime.datetime.now()
    )

@post_blueprint.route('/<category>/new', methods=['GET', 'POST'])
@login_required
@verify_required
def create_post(category):
    form = EditForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            
            
            return render_template('edit.html', category=category, form=form)
        else:
            return render_template('edit.html', category=category, form=form)
    elif request.method == 'GET':
        return render_template('edit.html', category=category, form=form)

@post_blueprint.route('/<category>/edit', methods=['GET', 'POST'])
@login_required
@verify_required
def edit_post(category):
        
    form = EditForm()
    
    return render_template('edit.html', category=category, form=form)
    '''
    if request.method == 'GET':
        return render_template('/edit.html', category=category)
    elif request.method == 'POST':
        listings = {
            'subject': request.form['subject'],
            'region': request.form['region'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'body': reqwuest.form['body'],
            'homes_type': request.form['homes_type'],
            'homes_price': request.form['homes_price'],
            'homes_bedrooms': request.form['homes_bedrooms'],
            'homes_parking': request.form['homes_parking'],
            'homes_year': request.form['homes_year'],
            'homes_sqft': request.form['homes_sqft'],
        }
        # store data in data store
        # code
        # code 
        return render_template('/view.html', category=category, posts=posts)
    else:
        return render_template(error_category.html)
        '''