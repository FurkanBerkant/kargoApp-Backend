import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from api import api_bp
from model.db import db
from serialization import ma
from flask_cors import CORS

load_dotenv('.env')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("VT_BAGLANTI")
db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(api_bp, url_prefix="/api")
CORS(app)

if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run()
