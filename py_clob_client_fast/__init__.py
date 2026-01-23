"""
Alias package: import py_clob_client_fast.* as if it were py_clob_client.*
"""

from importlib import import_module
import pkgutil
import sys

_UPSTREAM = "py_clob_client"

# Import upstream root package
_up = import_module(_UPSTREAM)

# Re-export upstream symbols at the top level (optional but convenient)
try:
    from py_clob_client import *  # noqa: F401,F403
except Exception:
    # If upstream doesn't define __all__ cleanly, ignore and rely on submodule imports.
    pass

# Alias all upstream submodules so this works:
#   from py_clob_client_fast.client import ClobClient
#   from py_clob_client_fast.order_builder.constants import BUY
if hasattr(_up, "__path__"):
    for m in pkgutil.walk_packages(_up.__path__, _UPSTREAM + "."):
        upstream_mod = m.name                        # e.g. py_clob_client.client
        fast_mod = __name__ + upstream_mod[len(_UPSTREAM):]  # e.g. py_clob_client_fast.client
        if fast_mod not in sys.modules:
            sys.modules[fast_mod] = import_module(upstream_mod)
