from flask import Flask
from flask_mongoengine import MongoEngine

from flask_qrcode import QRcode
from config import MONGODB_HOST, MONGODB_PORT, MONGODB_DB

app = Flask(__name__ , static_url_path='/static')
app.config.from_object('config')

db = MongoEngine()
db.init_app(app)
QRcode(app)

from flaskr.mod_pendaftaran.controllers import mod_pendaftaran
app.register_blueprint(mod_pendaftaran)