"""Application configuration.

Provides environment-specific configuration classes following the
twelve-factor app methodology.  Secrets are always read from environment
variables (or a .env file loaded by python-dotenv) and are never
hard-coded.
"""

from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Shared defaults for all environments."""

    # Flask
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "dev-secret-change-me")
    JSON_SORT_KEYS: bool = False

    # Supabase – populated at runtime; validated by the service layer.
    SUPABASE_URL: str = os.environ.get("SUPABASE_URL", "")
    SUPABASE_ANON_KEY: str = os.environ.get("SUPABASE_ANON_KEY", "")
    SUPABASE_SERVICE_ROLE_KEY: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")


class DevelopmentConfig(BaseConfig):
    """Local development – verbose errors, no caching."""

    DEBUG: bool = True
    TESTING: bool = False


class TestingConfig(BaseConfig):
    """Isolated test runner – no real DB calls expected."""

    DEBUG: bool = False
    TESTING: bool = True
    SECRET_KEY: str = "test-secret-key"
    WTF_CSRF_ENABLED: bool = False


class ProductionConfig(BaseConfig):
    """Production – no debug, strict secret validation."""

    DEBUG: bool = False
    TESTING: bool = False

    def __init_subclass__(cls, **kwargs: object) -> None:
        super().__init_subclass__(**kwargs)

    @classmethod
    def validate(cls) -> None:
        """Raise RuntimeError if required secrets are missing."""
        required = ["SECRET_KEY", "SUPABASE_URL", "SUPABASE_ANON_KEY"]
        missing = [k for k in required if not os.environ.get(k)]
        if missing:
            raise RuntimeError(
                f"Missing required environment variables: {', '.join(missing)}"
            )


config_map: dict[str, type[BaseConfig]] = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
