from Ticket_App import db
from flask_security import UserMixin, RoleMixin
from passlib.handlers.django import django_pbkdf2_sha256


# Define the User data-model.
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), nullable=False)
    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

    def __init__(self, username, password, email=None, active=True):
        self.username = username
        self.password = django_pbkdf2_sha256.encrypt(password)
        self.active = active
        self.email = email

    @staticmethod
    def authenticate(username, password):
        user = User.query.filter(User.username == username).one()
        if user and django_pbkdf2_sha256.verify(password, user.password):
            return user


# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


# Define the Role data-model
class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description


class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(255))
    done = db.Column(db.Boolean(), default=False)
    assigned_to = db.Column(db.String(50))

    def __init__(self, title, description="", assigned_to="", done=False):
        self.title = title
        self.description = description
        self.done = done
        self.assigned_to = assigned_to
