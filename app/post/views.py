from flask import Flask, flash, request, render_template, redirect, session, url_for, Blueprint, jsonify
from flask_login import login_required
from flask_sqlalchemy import *
import datetime

from app.models import PostHome
from app import db, verify_required
from app.post.edit_forms import EditForm

post_blueprint = Blueprint('post', __name__, template_folder='templates')

# ********************************************************************************
# Posts view
# 
# - url passes in category
# - filters pass in url parameters, grabbed using request.args.get and updates
#   new posts DB query
# ********************************************************************************
@post_blueprint.route('/<category>', methods=['GET'])
def get_posts_list(category):
    try:
        # request.args url parameters
        pmin = 0
        pmax = 0
        if request.args.get('pmin') and request.args.get('pmax'):
            pmin = int(re.search(r'\d+', request.args.get('pmin')).group())
            pmax = int(re.search(r'\d+', request.args.get('pmax')).group())
        beds = 0
        if request.args.get('beds'):
            beds = request.args.get('beds')
        baths = 0
        if request.args.get('baths'):
            baths = request.args.get('baths')
        city = ''
        if request.args.get('city'):
            city = request.args.get('city')

        # query filter components
        price_min = db.session.query(db.func.min(PostHome.price)).filter(PostHome.category==category).scalar()
        price_max = db.session.query(db.func.max(PostHome.price)).filter(PostHome.category==category).scalar()
        if pmin and pmax:
            pmin_filtered = pmin
            pmax_filtered = pmax
        else: 
            pmin_filtered = price_min
            pmax_filtered = price_max
        price_deco = ''
        if category in ['rent','homestay']:
            price_deco = '월'
        elif category=='bnb':
            price_deco = '일'
        cities = db.session.query(PostHome.city.distinct().label('city')).filter(PostHome.category==category).order_by(PostHome.city).limit(100).all()
        
        # query post and post components
        posts = (
            PostHome.query
            .filter(PostHome.category==category)
            .filter(PostHome.price >= pmin_filtered)
            .filter(PostHome.price <= pmax_filtered)
            .filter(PostHome.bedrooms >= beds)
            .filter(PostHome.bathrooms >= baths)
            .filter(PostHome.city.contains(city))
            .order_by(PostHome.id.desc())
            #.offset((category_num-1)*(100)).limit(100).all()
        )
        db.session.close()
        
        return render_template(
            '/posts.html', 
            category=category, 
            #category_num=category_num, 
            price_min=price_min, 
            price_max=price_max, 
            pmin_filtered=pmin_filtered, 
            pmax_filtered=pmax_filtered, 
            price_deco=price_deco, 
            cities=cities, 
            posts=posts,
            today=datetime.datetime.now()
        )
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