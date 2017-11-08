from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms_components import StringField
from wtforms.validators import DataRequired, Length, Required

class NameForm(FlaskForm):
    name = StringField("What's your name?", validators=[Required()])
    sumbit = SubmitField("Submit")