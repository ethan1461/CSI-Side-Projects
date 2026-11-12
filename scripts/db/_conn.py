"""Read-only database connection helper for local export scripts.

Purpose: give every script in scripts/db/ one way to reach CSI's production database,
         read-only, with the connection string supplied by the environment and never
         by a file in this repository.
Inputs:  CSI_DB_URL environment variable (a SQLAlchemy URL).
Outputs: a SQLAlchemy Engine, or a clear error explaining what is missing.
Owner:   data-analyst
Date:    2026-11-12

CLAUDE.md compliance:
  §8  — no credentials in code; config only. No bare except.
  §7.2 — the connection is read-only; callers must still select columns explicitly
         and never select decedent or family name fields.
"""

from __future__ import annotations

import os

from sqlalchemy import Engine, create_engine

_ENV_VAR = "CSI_DB_URL"


class MissingDatabaseURL(RuntimeError):
    """Raised when CSI_DB_URL is not set, with instructions rather than a stack trace."""


def get_engine(echo: bool = False) -> Engine:
    """Return a read-only Engine for the CSI database.

    Raises MissingDatabaseURL when the environment variable is absent, so the failure
    explains itself rather than surfacing as a driver error.
    """
    url = os.environ.get(_ENV_VAR)
    if not url:
        raise MissingDatabaseURL(
            f"{_ENV_VAR} is not set.\n\n"
            "Set it in your shell before running this script:\n"
            f"    export {_ENV_VAR}='postgresql://readonly_user:...@host:5432/dbname'\n\n"
            "Use the READ-ONLY database user. Do not put this in a file in the repo "
            "and do not commit it (CLAUDE.md section 8)."
        )
    # future=True keeps 2.x behaviour explicit; pool_pre_ping survives a laptop sleeping.
    return create_engine(url, echo=echo, future=True, pool_pre_ping=True)
