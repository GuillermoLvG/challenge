import injector
import pytest
import flask
import flask_injector
import injector
import os
from endpoints.api_controller import create_app
import di.provider as provider

@pytest.fixture
def default_dependencies():
    return {
        'max_area_getter': provider.MaxAreaGetterModule()
    }


@pytest.fixture
def test_injector():
    return injector.Injector()


@pytest.fixture
def app(default_dependencies, test_injector):
    app = create_app(
        custom_injector=test_injector,
        injector_modules=default_dependencies,
    )
    app.testing = True

    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client
