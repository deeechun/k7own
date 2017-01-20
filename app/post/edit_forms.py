from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (BooleanField, TextField, TextAreaField, HiddenField,
    validators, IntegerField, SubmitField)
from wtforms.fields.html5 import EmailField
from flask_wtf.file import FileField, FileAllowed
from flask_uploads import UploadSet, IMAGES

images = UploadSet('images', IMAGES)

class EditForm(FlaskForm):
    subject = TextField('subject', [
        validators.Required(message='필수항목입니다'),
        ])
    body = TextAreaField('body')
    phone = TextField('phone')
    email = EmailField('email', [
        validators.Email()
        ])
    kakaotalk = TextField('kakaotalk')
    address = TextField('address', [
        validators.Required(message='필수항목입니다'),
        ])
    city = TextField('city', [
        validators.Required(message='필수항목입니다'),
        ])
    price = IntegerField('price', [
        validators.Required(message='필수항목입니다'),
        ])
    bedrooms = IntegerField('bedrooms', [
        validators.Required(message='필수항목입니다'),
        ])
    bathrooms = IntegerField('bathrooms', [
        validators.Required(message='필수항목입니다'),
        ])
    parking = IntegerField('parking')
    
    utilities = BooleanField('utilities')
    internet = BooleanField('internet')
    furniture = BooleanField('furniture')
    
    sqft = IntegerField('sqft')
    year = IntegerField('year')
    image_file = FileField('image', validators=[
            FileAllowed(['jpg', 'png'], ".jpg .png 이미지 파일만 가능합니다!")
        ])
    recaptcha = RecaptchaField()
    submit = SubmitField('등록하기')