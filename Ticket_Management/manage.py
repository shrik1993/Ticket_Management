from flask_script import Manager, Shell
from flask_migrate import MigrateCommand
from Ticket_App import app

manager = Manager(app)

def make_shell_context():
    return dict(app=app)


# Interactive python shell in flask context
manager.add_command('shell', Shell(make_context=make_shell_context))

# Migrate models into database.
# Use case:
# 1. python mange db init
# 2. python mange db migrate
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
