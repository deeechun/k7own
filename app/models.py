from flask_sqlalchemy import SQLAlchemy
from flask_login import ( LoginManager,
                          UserMixin, 
                          current_user )
from werkzeug import ( generate_password_hash, 
                       check_password_hash )
import time

db = SQLAlchemy()
login_manager = LoginManager()
# config action on login_required views
login_manager.login_view = '/login'
login_manager.login_message = '로그인을 먼저 해주세요.'
login_manager.login_message_category = 'warning'

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    date_joined = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    verified = db.Column(db.Boolean, nullable=False, default=0)
    
    def __init__(self, email, username, password_input):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password_input, method='pbkdf2:sha256:10000')
        self.date_joined = time.strftime('%Y-%m-%d')
        self.verified = 0
    
    def __repr__(self):
        return '<User %r>' % self.username

    # set password attribute of instance by hashing password input using werkzeug
    def set_password(self, password_input):
        self.password = generate_password_hash(password_input, method='pbkdf2:sha256:10000')

    # check password input against hashed password using werkzeug
    # returns true if input and hashed password match, false otherwise
    def check_password(self, password_input):
        if self.password is None:
            return False
        return check_password_hash(self.password, password_input)

    # authenticates user using username and password inputs taken from user
    # returns type tuple with username and boolean
    # boolean is true if user is authenticated, false otherwise
    @classmethod
    def authenticate(cls, username_input, password_input):
        user = User.query.filter(db.or_(User.username == username_input)).first()
        if user:
            authenticated = user.check_password(password_input)
        else:
            authenticated = False
        return user, authenticated
    
    # checks db if username or email is taken
    # .scalar() returns first element of the first result or None if no rows present
    @classmethod
    def is_username_taken(cls, username):
        return db.session.query(db.exists().where(User.username==username)).scalar()
    @classmethod
    def is_email_taken(cls, email):
        return db.session.query(db.exists().where(User.email==email)).scalar()

    # fetch db for user by 'id'
    # create and return new User object
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

class Post(object):
    category = db.Column(db.String(12), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    viewed = db.Column(db.Integer, nullable=False, default=0)
    username = db.Column(db.String(30), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(30), nullable=False)
    image_ext = db.Column(db.String(300), default='/static/images/no-photo.png')
    phone = db.Column(db.String(12))
    email = db.Column(db.String(120))
    kakaotalk = db.Column(db.String(30))

class PostHome(db.Model, Post):
    __tablename__ = 'home_posts'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(300))
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    parking = db.Column(db.Integer)
    sqft = db.Column(db.Integer)
    year = db.Column(db.Integer)

    def __init__(self, category, date_posted, viewed, username, subject, body, 
    	         price, city, image_ext, phone, email, kakaotalk,
                 address, bedrooms, bathrooms, parking, sqft, year):
        self.category = category
        self.date_posted = date_posted
        self.viewed = viewed
        self.username = username
        self.subject = subject
        self.body = body
        self.price = price
        self.city = city
        self.image_ext = image_ext
        self.phone = phone
        self.email = email
        self.kakaotalk = kakaotalk

        self.address = address
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.parking = parking
        self.sqft = sqft
        self.year = year

    #def __repr__(self):
    #    return '<%>' % self.subject
    
    def serialize(self):
        return {
            'id': self.id,
            'category': self.category,
            'date_posted': self.date_posted,
            'viewed': self.viewed,
            'username': self.username,
            'subject': self.subject,
            'body': self.body,
            'price': self.price,
            'city': self.city,
            'image_ext': self.image_ext,
            'phone': self.phone,
            'email': self.email,
            'kakaotalk': self.kakaotalk,

            'address': self.address,
            'bedrooms': self.bedrooms,
            'bathrooms': self.bathrooms,
            'parking': self.parking,
            'sqft': self.sqft,
            'year': self.year
        }

class PostCar(db.Model, Post):
    # common post components
    __tablename__ = 'car_posts'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    make = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    mileage = db.Column(db.Integer)

    def __init__(self, category, date_posted, viewed, username, subject, body, 
    	         price, city, image_ext, phone, email, kakaotalk,
                 year, make, model, mileage):
        self.category = category
        self.date_posted = date_posted
        self.viewed = viewed
        self.username = username
        self.subject = subject
        self.body = body
        self.price = price
        self.city = city
        self.image_ext = image_ext
        self.phone = phone
        self.email = email
        self.kakaotalk = kakaotalk

        self.year = year
        self.make = make
        self.model = model
        self.mileage = mileage

    #def __repr__(self):
    #    return '<%>' % self.subject
    
    def serialize(self):
        return {
            'id': self.id,
            'category': self.category,
            'date_posted': self.date_posted,
            'viewed': self.viewed,
            'username': self.username,
            'subject': self.subject,
            'body': self.body,
            'price': self.price,
            'city': self.city,
            'image_ext': self.image_ext,
            'phone': self.phone,
            'email': self.email,
            'kakaotalk': self.kakaotalk,

            'year': self.year,
            'make': self.make,
            'model': self.model,
            'mileage': self.mileage
        }