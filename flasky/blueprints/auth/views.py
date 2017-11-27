from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from flasky.blueprints.page.models import User
from .forms import LoginForm, RegistrationForm
from flasky.extensions import db
from sqlalchemy.sql.functions import current_user

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/register', methods=['GET', 'POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        user = User(email=form.email.data, username=form.username.data, password=form.password.data, role_id=3)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()

        flash("Confirmation Email: " + url_for('auth.confirm', token=token))

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        print("You are already confirmed")
        return redirect(url_for('page.index'))
    if current_user.confirm(token):
        print("token confirmed: " + token)
        flash('You have confirmed your account. Thanks!')
    else:
        print('The confirmation link is invalid or has expired.')
        flash('The confirmation link is invalid or has expired.')

    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        print("Found user:",user)

        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('auth.home'))

        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('auth.login'))

@auth.route('/home')
@login_required
def home():
    return render_template('auth/home.html')