import pytest
from config import config
from app import init_app
from app.controllers.test_controller import seed_test, clean_test

configuration = config['development']

@pytest.fixture(scope="session", autouse=True)
def app():
    app = init_app(configuration)
    app.config.update({
        "TESTING": True
    })
    seed_test()
    yield app
    
    clean_test()


    

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
