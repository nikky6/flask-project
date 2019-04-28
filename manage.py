#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 4:24 PM
# @Author  : Nikky
# @Site    : 
# @File    : manage.py
# python3 manage.py db init
# python3 manage.py db migrate
# python3 manage.py db upgrade
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import create_app, db

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
