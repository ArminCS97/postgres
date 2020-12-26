from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

from database.database import DatabaseSession, init_db
from views.vendors_view import vendors_blueprint
from views.parts_view import parts_blueprint
from views.part_drawings_view import part_drawings_blueprint
from database.database import DATABASE_URL

application = Flask(__name__)
application.register_blueprint(vendors_blueprint)
application.register_blueprint(parts_blueprint)
application.register_blueprint(part_drawings_blueprint)

application.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(application)
migrate = Migrate(application, db)
manager = Manager(application)
manager.add_command('db', MigrateCommand)

init_db()


# Flask will automatically remove database sessions at the end
# of the request or when the application shuts down
@application.teardown_appcontext
def shutdown_session(exception=None):
    DatabaseSession.remove()


if __name__ == '__main__':
    manager.run()
