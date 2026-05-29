"""Tests for main blueprint routes."""

from __future__ import annotations

from flask.testing import FlaskClient


def test_index_returns_200(client: FlaskClient) -> None:
    """Home page should respond with HTTP 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_index_contains_heading(client: FlaskClient) -> None:
    """Home page should contain the hero heading."""
    response = client.get("/")
    assert b"Hello, World!" in response.data


def test_health_endpoint(client: FlaskClient) -> None:
    """Health-check route should return JSON {status: ok}."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data == {"status": "ok"}


def test_404_for_unknown_route(client: FlaskClient) -> None:
    """Requests for unknown routes should return HTTP 404."""
    response = client.get("/this-does-not-exist")
    assert response.status_code == 404
