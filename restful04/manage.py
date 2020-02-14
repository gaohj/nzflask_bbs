from app import app
from flask_script import Manager
import models
from extensions import db
from flask_migrate import Migrate,MigrateCommand

migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
#python manage.py db init


if __name__ == "__main__":
    manager.run()