from app import db, login_manager
from flask_login import UserMixin, current_user
from werkzeug import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    date_joined = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    verified = db.Column(db.Boolean, nullable=False, default=0)
    
    def __init__(self, date_joined, email, username, password, verified):
        self.date_joined = date_joined
        self.email = email
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256:100000')
        self.verified = verified
    
    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password_input):
        self.password = generate_password_hash(password_input)

    def check_password(self, password_input):
        if self.password is None:
            return False
        return check_password_hash(self.password, password_input)

    @classmethod
    def authenticate(cls, username, password):
        user = User.query.filter(db.or_(User.username == username)).first()
        if user:
            authenticated = user.check_password(password)
        else:
            authenticated = False
        return user, authenticated
      
    @classmethod
    def is_username_taken(cls, username):
        return db.session.query(db.exists().where(User.username==username)).scalar()
    
    @classmethod
    def is_email_taken(cls, email):
        return db.session.query(db.exists().where(User.email==email)).scalar()

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


class PostHome(db.Model):
    # common post components
    __tablename__ = 'home_posts'
    id = db.Column(db.Integer, primary_key=True)
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
    
    address = db.Column(db.String(300))
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    parking = db.Column(db.Integer)
    sqft = db.Column(db.Integer)
    year = db.Column(db.Integer)

    #utilities = db.Column(db.Boolean, default=0)
    #internet = db.Column(db.Boolean, default=0)
    #furniture = db.Column(db.Boolean, default=0)
    
    def __init__(self, category, date_posted, viewed, username, 
                subject, body, price, city, image_ext,
                 phone, email, kakaotalk,
                 address, bedrooms, bathrooms, parking, sqft, year):
        # common post components
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

        #self.utilities = utilities
        #self.internet = internet
        #self.furniture = furniture
 
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