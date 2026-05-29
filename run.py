"""Application entry point.

Run with::

    python run.py

Or, for production, use Gunicorn::

    gunicorn "app:create_app()" --bind 0.0.0.0:8000 --workers 4
"""

from __future__ import annotations

import os

from app import create_app

app = create_app(os.environ.get("FLASK_ENV", "development"))

if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "127.0.0.1"),
        port=int(os.environ.get("PORT", 5000)),
    )
