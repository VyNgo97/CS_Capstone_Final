import markdown
import os
import sqlite3
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

DATABASE = 'devices.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        c = db.cursor()
        c.execute("CREATE TABLE devices (identifier, device_name, device_type, controller_gateway)")
        c.execute("INSERT INTO devices VALUES (12345, 'microcontroller', 'LED_Controller', 123123123)")
        db.commit()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():

    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        content = markdown_file.read()

        return markdown.markdown(content)

class DeviceStore(Resource):
    def get(self):
        db = get_db()
        c = db.cursor()
        rows = c.execute('SELECT device_type FROM devices')
        rows = rows.fetchall()
        print(rows)

        devices = []

        for key in rows:
            devices.append(key)

        return {'message': 'Success', 'data': devices}, 200

    def post(self):
        db = get_db()
        c = db.cursor()
        c.execute("INSERT INTO devices VALUES (12345, 'microcontroller', 'LED_Controller', 123123123)")
        db.commit()

        return {'message': 'Resource Added', 'data': devices}

    

api.add_resource(DeviceStore, '/devices')