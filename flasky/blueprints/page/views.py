from flask import Blueprint, render_template, session, redirect, url_for, flash
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from .forms import NameForm

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():

        old_name = session.get('name')

        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')

        session['name'] = form.name.data
        return redirect(url_for('page.index'))
    return render_template('page/index.html', form=form, name=session.get('name'))

@page.route('/user/<name>')
def user(name):
    return render_template('page/user.html', name=name)

@page.app_errorhandler(404)
def page_not_found(e):
    return render_template('page/404.html'), 404

@page.app_errorhandler(500)
def internal_server_error(e):
    return render_template('page/500.html'), 500