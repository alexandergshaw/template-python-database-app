"""Main (HTML) blueprint.

Handles server-rendered page routes.
"""

from __future__ import annotations

from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index() -> str:
    """Landing / home page."""
    return render_template("index.html")


@main_bp.route("/health")
def health() -> tuple[dict[str, str], int]:
    """Simple health-check endpoint used by load balancers / uptime monitors."""
    return {"status": "ok"}, 200
