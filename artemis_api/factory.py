"""Module to create a new API instance"""


from flask import Flask


def create_app(config_filename: str) -> Flask:
    """Create a new API instance"""
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from artemis_api.blueprints import base_blueprint
    app.register_blueprint(base_blueprint, url_prefix='/v1')

    return app