from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from database.database import DatabaseSession, init_db, DATABASE_URL
from views.part_drawings_view import part_drawings_blueprint
from views.parts_view import parts_blueprint
from views.vendors_view import vendors_blueprint

init_db()

application = Flask(__name__)
application.register_blueprint(vendors_blueprint)
application.register_blueprint(parts_blueprint)
application.register_blueprint(part_drawings_blueprint)


# Flask will automatically remove database sessions at the end
# of the request or when the application shuts down
@application.teardown_appcontext
def shutdown_session(exception=None):
    DatabaseSession.remove()

application.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)
migrate = Migrate(application, db)


if __name__ == '__main__':
    application.run()
