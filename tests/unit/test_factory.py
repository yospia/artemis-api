from artemis_api.factory import create_app


def test_app_factory():
    """Testa a instancializacao da API"""

    app = create_app('artemis_api.config.Testing')

    assert app.name == 'artemis_api'
    assert app.testing == True
    