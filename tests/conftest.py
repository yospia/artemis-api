"""Contem as Fixtures para os testes do Flask"""
import pytest
from artemis_api.factory import create_app
from flask import Flask
from flask.testing import FlaskClient


@pytest.fixture
def client(app) -> FlaskClient:
    """Fixture para testar a API
    
    Pode ser usado como:
        client.get(url, data=data)
        client.post(url, data=data)
        client.put(url, data=data)
        client.delete(url, data=data)
        client.patch(url, data=data)
    """

    return app.test_client()


@pytest.fixture
def app(request) -> Flask:
    """Instancia da API, configurada para testes"""

    app = create_app('artemis_api.config.Testing')

    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()
