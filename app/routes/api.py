"""REST API blueprint (v1).

All JSON endpoints live under the ``/api/v1`` prefix.  Add new resource
modules here and register them as nested blueprints or additional routes
as the project grows.
"""

from __future__ import annotations

from flask import Blueprint, Response, jsonify

api_bp = Blueprint("api", __name__)


@api_bp.route("/status")
def status() -> Response:
    """API status / heartbeat.

    Returns:
        JSON payload with ``{"status": "ok"}``.
    """
    return jsonify({"status": "ok"})
