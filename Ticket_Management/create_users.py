#!/usr/bin/env python

from Ticket_App import app, db
from Ticket_App.APIs.models import User, Role, UserRoles


if  __name__ == "__main__":
    # Create 'guest' user with no roles
    if not User.query.filter(User.email == 'guest@example.com').first():
        user = User(
            email='guest@example.com',
            username='guest',
            password='guest123',
        )
        user.roles.append(Role(name='Guest', description=""))
        db.session.add(user)
        db.session.commit()

    # Create 'admin' user with 'Admin' roles
    if not User.query.filter(User.email == 'admin@example.com').first():
        user = User(
            email='admin@example.com',
            username='admin',
            password='admin123',
        )
        user.roles.append(Role(name='Admin', description=""))
        db.session.add(user)
        db.session.commit()
