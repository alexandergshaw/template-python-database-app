"""Shared pytest fixtures."""

from __future__ import annotations

from collections.abc import Generator

import pytest
from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner

from app import create_app


@pytest.fixture(scope="session")
def app() -> Generator[Flask, None, None]:
    """Create an application instance configured for testing."""
    flask_app = create_app("testing")
    flask_app.config.update(
        {
            "TESTING": True,
            "SECRET_KEY": "test-secret-key",
        }
    )
    yield flask_app


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    """Return a test client for the app."""
    return app.test_client()


@pytest.fixture()
def runner(app: Flask) -> FlaskCliRunner:
    """Return a CLI test runner for the app."""
    return app.test_cli_runner()
