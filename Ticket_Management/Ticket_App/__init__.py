"""
    @brief Flask blueprint are registered in _init__.py file.
    @details The file contains a blueprint registered for Ticket Management app which is
    apis_blueprint.
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_security import SQLAlchemyUserDatastore, Security
from config import app_config

# Set configuration with help of env variable in bash
config_env = os.getenv('env', 'development')

app = Flask(__name__)

app.config.from_object(app_config[config_env])

db = SQLAlchemy(app)
# database migration
migrate = Migrate(app, db)

from .APIs.models import User, Role, UserRoles

from .APIs import APIs as apis_blueprint

# Register blueprints
app.register_blueprint(apis_blueprint)

# Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security().init_app(app, user_datastore, register_blueprint=False)
