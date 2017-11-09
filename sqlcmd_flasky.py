from sqlalchemy_utils import database_exists, create_database
from flasky.app import create_app
from flasky.extensions import db
from flasky.blueprints.page.models import User, Role

def init(with_testdb = True):
    db.drop_all()
    db.create_all()

    if with_testdb:
        db_uri = '{0}_test'.format(app.config['SQLALCHEMY_DATABASE_URI'])

        if not database_exists(db_uri):
            create_database(db_uri)

    return None

def seed():
    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')

    user_john = User(username='john', role=admin_role)
    user_susan = User(username='susan', role=user_role)
    user_david = User(username='david', role=user_role)

    db.session.add(admin_role)
    db.session.add(mod_role)
    db.session.add(user_role)
    db.session.add(user_john)
    db.session.add(user_susan)
    db.session.add(user_david)
    
    db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])
    db.session.commit()


if __name__ == "__main__":
    app = create_app()
    db.app = app
    print(app.config['SERVER_NAME'])
    seed()

    #db.drop_all()
    #db.create_all()
    #seed()
