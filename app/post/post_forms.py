from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (SelectField,
                     BooleanField, 
                     IntegerField,
                     TextField, 
                     TextAreaField, 
                     HiddenField,
                     validators, 
                     SubmitField )
from wtforms.fields.html5 import EmailField
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import UploadSet, IMAGES

images = UploadSet('images', IMAGES)

class CommonForm(FlaskForm):
    category = SelectField('category',
                           choices=[('cpp', 'C++'), 
                                    ('py', 'Python')] )
    subject = TextField('subject', 
                        [validators.Required(message='필수항목입니다') ] )
    body = TextAreaField('body')
    price = IntegerField('price', 
                         [validators.Required(message='필수항목입니다') ] )
    city = TextField('city', 
                     [validators.Required(message='필수항목입니다') ] )
    image_file = FileField('image', 
                           validators=[FileAllowed(['jpg', 'png'], 
                                       ".jpg .png 이미지 파일만 가능합니다!") ] )
    phone = TextField('phone')
    email = EmailField('email',
                       [validators.Email() ] )
    kakaotalk = TextField('kakaotalk')
    recaptcha = RecaptchaField()
    submit = SubmitField('등록하기')
    
class HomeForm(CommonForm):
    address = TextField('address', 
                        [validators.Required(message='필수항목입니다') ] )
    bedrooms = IntegerField('bedrooms', 
                            [validators.Required(message='필수항목입니다') ] )
    bathrooms = IntegerField('bathrooms', 
                             [validators.Required(message='필수항목입니다') ] )
    parking = IntegerField('parking')    
    sqft = IntegerField('sqft')
    year = IntegerField('year')

class CarForm(CommonForm):
    year = IntegerField('year')
    make = TextField('model', 
                     [validators.Required(message='필수항목입니다') ] )
    model = TextField('model', 
                      [validators.Required(message='필수항목입니다') ] )
    mileage = IntegerField('mileage')