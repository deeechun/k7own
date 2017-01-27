from app.models import User, PostHome
from app import app, db
import datetime
from time import strftime
import os

# Add seed data to the database
with app.app_context():
    newuser = User(
                date_joined = strftime("%Y-%m-%d"),
                email = 'ejh2163@gmail.com',
                username = 'ejh2163',
                password = '48cd3f6p',
                verified = 1
                )

    new_post = PostHome(
                category='realestate',
                date_posted=datetime.datetime.now(),
                viewed=0, 
                username='ejh2163', 
                subject='하숙 샘플 포스팅입니다2', 
                body='하숙 샘플 포스팅입니다', 
                price=390000, 
                city='Los Angeles, CA', 
                image_ext='',
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                address='1234 Wilshire Blvd.', 
                bedrooms=2, 
                bathrooms=2,
                parking=1, 
                sqft=1234, 
                year=1991
                )
    new_post2 = PostHome(
                category='homestay',
                date_posted=datetime.datetime.now(),
                viewed=0, 
                username='ejh2163', 
                subject='하숙 샘플 포스팅입니다2', 
                body='하숙 샘플 포스팅입니다', 
                price=390000, 
                city='Los Angeles, CA', 
                image_ext='',
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                address='1234 Wilshire Blvd.', 
                bedrooms=2, 
                bathrooms=2,
                parking=1, 
                sqft=1234, 
                year=1991
                )
    new_post3 = PostHome(
                category='rent',
                date_posted=datetime.datetime.now(),
                viewed=0, 
                username='ejh2163', 
                subject='하숙 샘플 포스팅입니다2', 
                body='하숙 샘플 포스팅입니다', 
                price=390000, 
                city='Los Angeles, CA', 
                image_ext='',
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                address='1234 Wilshire Blvd.', 
                bedrooms=2, 
                bathrooms=2,
                parking=1, 
                sqft=1234, 
                year=1991
                )
    db.session.add(newuser)
    db.session.add(new_post)
    db.session.add(new_post2)
    db.session.add(new_post3)
    db.session.commit()