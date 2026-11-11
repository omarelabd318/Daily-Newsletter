# Loaded by Python at start-up when run_data.py puts this folder on PYTHONPATH: puts the shared fetch layer
# (sources.py) under every desk script without changing them.
import os
import sys
if os.environ.get("DESK_SOURCES") == "1":
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    try:
        import sources
        sources.install()
    except Exception:
        pass
