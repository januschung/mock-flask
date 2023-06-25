from flask import Flask
from mock_blueprint import mock_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(mock_blueprint, url_prefix="/")

    return app
