from app.models import User, Post
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
    newpost_rent = Post(
                date_posted=datetime.datetime.now(),
                page = 'rent',
                username='admin', 
                viewed=0, 
                subject='asdfasdfasdfasdfasdf2', 
                body='asdfasdfasdf', 
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                city='Los Angeles, CA', 
                price=725, 
                image_ext='',
                address='1234 Wilshire Blvd.', 
                bedrooms=1, 
                bathrooms=0,
                parking=1, 
                utilities=1, 
                internet=1,
                furniture=1, 
                sqft=1234, 
                year=1991
                )
    newpost_homestay = Post(
                date_posted=datetime.datetime.now(),
                page = 'homestay',
                username='admin', 
                viewed=0, 
                subject='하숙 샘플 포스팅입니다2', 
                body='하숙 샘플 포스팅입니다', 
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                city='Los Angeles, CA', 
                price=725, 
                image_ext='',
                address='1234 Wilshire Blvd.', 
                bedrooms=1, 
                bathrooms=0,
                parking=1, 
                utilities=1, 
                internet=1,
                furniture=1, 
                sqft=1234, 
                year=1991
                )
    newpost_realestate = Post(
                date_posted=datetime.datetime.now(),
                page = 'realestate',
                username='admin', 
                viewed=0, 
                subject='하숙 샘플 포스팅입니다2', 
                body='하숙 샘플 포스팅입니다', 
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                city='Los Angeles, CA', 
                price=725, 
                image_ext='',
                address='1234 Wilshire Blvd.', 
                bedrooms=1, 
                bathrooms=0,
                parking=1, 
                utilities=1, 
                internet=1,
                furniture=1, 
                sqft=1234, 
                year=1991
                )
    newpost_realestate2 = Post(
                date_posted=datetime.datetime.now(),
                page = 'realestate',
                username='admin', 
                viewed=0, 
                subject='하숙 샘플 포스팅입니다2', 
                body='하숙 샘플 포스팅입니다', 
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                city='Los Angeles, CA', 
                price=390000, 
                image_ext='',
                address='1234 Wilshire Blvd.', 
                bedrooms=2, 
                bathrooms=2,
                parking=1, 
                utilities=1, 
                internet=1,
                furniture=1, 
                sqft=1234, 
                year=1991
                )
    db.session.add(newpost_rent)
    db.session.add(newpost_homestay)
    db.session.add(newpost_realestate)
    db.session.add(newpost_realestate2)
    db.session.commit()