"""Flask extension initialization.

Extensions are instantiated here (without binding to an app) so they can
be imported anywhere in the codebase.  The ``init_extensions`` function
wires them to a concrete Flask app via the application-factory pattern.
"""

from __future__ import annotations

from flask import Flask


def init_extensions(app: Flask) -> None:
    """Bind all extensions to *app*.

    Args:
        app: The Flask application instance created by the factory.
    """
    # Nothing to initialize yet – add extensions here as the project grows
    # (e.g. Flask-Login, Flask-Limiter, Flask-Caching, …).
    pass
