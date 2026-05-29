"""Vercel serverless entry point.

Vercel looks for a WSGI-compatible ``app`` object in this file.
All requests are routed here via ``vercel.json``.
"""

from __future__ import annotations

import os

from app import create_app

app = create_app(os.environ.get("FLASK_ENV", "production"))
