from flask import Blueprint, render_template
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

page = Blueprint('page', __name__, template_folder='templates')

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@page.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('page/index.html', form=form, name=name)

@page.route('/user/<name>')
def user(name):
    return render_template('page/user.html', name=name)

@page.app_errorhandler(404)
def page_not_found(e):
    return render_template('page/404.html'), 404

@page.app_errorhandler(500)
def internal_server_error(e):
    return render_template('page/500.html'), 500