"""Tests for the API v1 blueprint."""

from __future__ import annotations

from flask.testing import FlaskClient


def test_api_status(client: FlaskClient) -> None:
    """GET /api/v1/status should return {status: ok}."""
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    data = response.get_json()
    assert data == {"status": "ok"}


def test_api_status_content_type(client: FlaskClient) -> None:
    """API status endpoint must return JSON content type."""
    response = client.get("/api/v1/status")
    assert response.content_type == "application/json"
