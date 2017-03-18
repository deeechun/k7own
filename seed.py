from app.models import User, PostHome, PostCar
from app import app, db
import datetime
import os

# Add seed data to the database
with app.app_context():
    newuser = User(
                date_joined = datetime.datetime.now(),
                email = 'ejh2163@gmail.com',
                username = 'ejh2163',
                password = '48cd3f6p',
                verified = 1
                )

    new_home = PostHome(
                category='realestate',
                date_posted=datetime.datetime.now(),
                viewed=0, 
                username='ejh2163', 
                subject='하숙 샘플 포스팅입니다2', 
                body='하숙 샘플 포스팅입니다', 
                price=212000, 
                city='Los Angeles, CA', 
                image_ext='',
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                address='1234 studio st.', 
                bedrooms=0, 
                bathrooms=1,
                parking=1, 
                sqft=1234, 
                year=1991
                )
    new_home2 = PostHome(
                category='homestay',
                date_posted=datetime.datetime.now(),
                viewed=0, 
                username='ejh2163', 
                subject='하숙 샘플 포스팅입니다2', 
                body='하숙 샘플 포스팅입니다', 
                price=750, 
                city='Los Angeles, CA', 
                image_ext='',
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                address='923 s Harvard Blvd.', 
                bedrooms=1, 
                bathrooms=1,
                parking=1, 
                sqft=1234, 
                year=1991
                )
    new_car = PostCar(
                category='lease',
                date_posted=datetime.datetime.now(),
                viewed=0, 
                username='ejh2163', 
                subject='리 스 자 동 차', 
                body='샘플 포스팅입니다', 
                price=220, 
                city='Los Angeles, CA', 
                image_ext='',
                phone='123-456-7890', 
                email='calbang.noreply@gmail.com', 
                kakaotalk='calbang', 
                year=1991,
                make='kia',
                model='optima',
                mileage=1200
                )
    #db.session.add(newuser)
    db.session.add(new_home)
    db.session.add(new_home2)
    db.session.add(new_car)
    db.session.commit()