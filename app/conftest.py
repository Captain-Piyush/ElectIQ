import os
import pytest

# Ensure GEMINI_API_KEY is set for tests before importing main
os.environ["GEMINI_API_KEY"] = "test-key"

from main import app as flask_app

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
    })
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()
