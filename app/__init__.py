"""Flask application factory."""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from flask import Flask

from app.config import config_map


def create_app(config_name: str = "default") -> Flask:
    """Create and configure the Flask application.

    Args:
        config_name: One of "development", "production", "testing", or "default".

    Returns:
        A fully configured Flask application instance.
    """
    app = Flask(__name__, instance_relative_config=False)

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------
    app.config.from_object(config_map[config_name])

    # ------------------------------------------------------------------
    # Extensions
    # ------------------------------------------------------------------
    from app.extensions import init_extensions  # noqa: PLC0415

    init_extensions(app)

    # ------------------------------------------------------------------
    # Blueprints
    # ------------------------------------------------------------------
    from app.routes.api import api_bp  # noqa: PLC0415
    from app.routes.main import main_bp  # noqa: PLC0415

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api/v1")

    # ------------------------------------------------------------------
    # Error handlers
    # ------------------------------------------------------------------
    _register_error_handlers(app)

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------
    _configure_logging(app)

    return app


def _register_error_handlers(app: Flask) -> None:
    from flask import render_template  # noqa: PLC0415

    @app.errorhandler(404)
    def not_found(error: Exception) -> tuple[str, int]:  # noqa: ANN001
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(error: Exception) -> tuple[str, int]:  # noqa: ANN001
        return render_template("errors/500.html"), 500


def _configure_logging(app: Flask) -> None:
    if app.debug:
        return

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    )

    # Try to write logs to a rotating file; fall back to stdout (e.g. on
    # read-only filesystems such as Vercel serverless functions).
    try:
        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)
        handler: logging.Handler = RotatingFileHandler(
            log_dir / "app.log",
            maxBytes=10 * 1024 * 1024,  # 10 MB
            backupCount=5,
        )
    except OSError:
        handler = logging.StreamHandler()

    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

