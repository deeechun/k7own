from flask import Flask, flash, request, render_template, redirect, session, url_for, Blueprint
from flask_login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh
from time import strftime

from app.models import User
from app.user.user_forms import LoginForm, RegisterForm
from app import db, verify_required
from app.user.token import generate_confirmation_token, confirm_token
from app.user.email import send_mail


user_blueprint = Blueprint('user', __name__, template_folder='templates')


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    page = 'register'
    if current_user.is_authenticated:
        flash('이미 로그인된 상태입니다.', 'danger')
        return redirect(url_for('home.home'))
    
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if User.is_email_taken(form.email.data):
                flash('이메일이 이미 가입되어 있습니다.', 'danger')
            elif User.is_username_taken(form.username.data):
                flash('아이디가 이미 가입되어 있습니다.', 'danger')
            else:    
                new_user = User(
                    date_joined = strftime("%Y-%m-%d"),
                    email = form.email.data,
                    username = form.username.data,
                    password = form.password.data,
                    verified = 0
                    )
                db.session.add(new_user)
                db.session.commit()
                
                # generate token and verify token url
                token = generate_confirmation_token(new_user.email)
                verify_url = url_for('user.verify_email', token=token, _external=True)
                # create email message and send
                email_html = render_template('/verify_msg.html', verify_url=verify_url)
                email_subject = '캘방 계정확인 이메일입니다'
                send_mail(new_user.email, email_subject, email_html)
                
                flash_message = '환영합니다 ' + new_user.username+'님!'
                flash(flash_message, 'success')
                login_user(new_user)
                
                db.session.close()
                return redirect(url_for('user.unverified'))
            return render_template('/register.html', form=form, page=page)
        else:
            return render_template('/register.html', form=form, page=page)
    elif request.method == 'GET':
        return render_template('/register.html', form=form, page=page)

@user_blueprint.route('/verify/<token>')
@login_required
def verify_email(token):
    try:
        email = confirm_token(token)
        user = User.query.filter_by(email=email).first_or_404()
        if user.verified:
            flash('계정 이메일이 이미 확인되었습니다. 로그인 해주세요.', 'success')
        else:
            user.verified = True
            db.session.add(user)
            db.session.commit()
            flash('계정 이메일이 확인되었습니다. 감사합니다!', 'success')
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
    return redirect(url_for('home.home'))

@user_blueprint.route('/unverified')
@login_required
def unverified():
    if current_user.verified==1:
        return redirect('home.home')
    else:
        flash('계정확인이 먼저 필요합니다. 계정확인을 위해 이메일을 확인해주세요', 'warning')
        return render_template('/unverified.html')

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    page = 'login'
    if current_user.is_authenticated:
        flash('이미 로그인된 상태입니다.', 'danger')
        return redirect(url_for('home.home'))
    
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user, authenticated = User.authenticate(form.username.data, form.password.data)
            if user:
                if authenticated:
                    login_user(user, remember=form.remember_me.data)
                    
                    db.session.close()
                    return redirect(url_for('home.home'))
                else:
                    flash('아이디와 비밀번호가 일치하지 않습니다', 'danger')
                    return render_template('/login.html', form=form, page=page)
            else:
                flash('아이디가 가입되어있지 않습니다', 'danger')
                return render_template('/login.html', form=form, page=page)
        else:
            return render_template('/login.html', form=form, page=page)
    elif request.method == 'GET':
        return render_template('/login.html', form=form, page=page)

@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))

@user_blueprint.route('/reset')
def reset():
    return render_template('/reset.html')

@user_blueprint.route('/profile')
@login_required
@verify_required
def profile():
    return render_template('/profile.html')

