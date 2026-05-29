"""Tests for the Supabase client service."""

from __future__ import annotations

import pytest


def test_get_supabase_raises_without_credentials() -> None:
    """get_supabase should raise ValueError when credentials are missing."""
    from app.services.supabase_client import get_supabase

    # Clear the lru_cache so previous calls don't interfere.
    get_supabase.cache_clear()

    with pytest.raises(ValueError, match="Supabase credentials not configured"):
        get_supabase(url="", key="")

    get_supabase.cache_clear()
