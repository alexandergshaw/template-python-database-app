"""Supabase client service.

Provides a thin singleton wrapper around the ``supabase-py`` client so
the rest of the application never instantiates it directly.  This keeps
credentials and initialisation logic in one place and makes it trivial
to swap the backend in tests.
"""

from __future__ import annotations

import os
from functools import lru_cache

from supabase import Client, create_client


@lru_cache(maxsize=1)
def get_supabase(
    url: str | None = None,
    key: str | None = None,
) -> Client:
    """Return a cached Supabase client.

    Reads ``SUPABASE_URL`` and ``SUPABASE_ANON_KEY`` from the environment
    when *url* / *key* are not supplied explicitly (typical production
    usage).

    Args:
        url: Supabase project URL.  Defaults to the ``SUPABASE_URL`` env var.
        key: Supabase anon key.  Defaults to ``SUPABASE_ANON_KEY`` env var.

    Returns:
        A ready-to-use ``supabase.Client`` instance.

    Raises:
        ValueError: If either *url* or *key* is empty.
    """
    resolved_url = url or os.environ.get("SUPABASE_URL", "")
    resolved_key = key or os.environ.get("SUPABASE_ANON_KEY", "")

    if not resolved_url or not resolved_key:
        raise ValueError(
            "Supabase credentials not configured. "
            "Set SUPABASE_URL and SUPABASE_ANON_KEY environment variables."
        )

    return create_client(resolved_url, resolved_key)
