from flask import Flask, jsonify

from config import config


def create_app(config_name="dev"):
    """App factory method for initializing flask extensions and registering
    blueprints."""
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # a simple ping that says hello
    @app.route("/ping")
    def ping():
        return jsonify({"message": "Hello, World"}), 200

    return app
