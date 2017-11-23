#from flask_debugtoolbar import DebugToolbarExtension
#from flask_mail import Mail
#from flask_wtf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#logins
login_manager = LoginManager()
login_manager.session_protection = 'strong' 
login_manager.login_view = 'auth.login'

#db
db = SQLAlchemy()

#debug_toolbar = DebugToolbarExtension()
#mail = Mail()
#Csrf = CSRFProtect()
#login_manager = LoginManager()
