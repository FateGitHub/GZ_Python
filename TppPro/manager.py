from app import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.extensions import db
import os


# 选择开发环境
config_name = os.environ.get("CONFIG_NAME") or "default"
print(config_name)

app = create_app(config_name)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
