from flask import Flask, jsonify
from flask_marshmallow import Marshmallow

from config import config

ma = Marshmallow()

def create_app(config_name='dev'):
    """App factory method for initializing flask extensions and registering
    blueprints."""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config[config_name]) 
    ma.init_app(app)

    # a simple ping that says hello
    @app.route('/ping')
    def ping():
        return jsonify({"message": "Hello, World"}), 200

    return app