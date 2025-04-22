# src/__init__.py

"""
E‑Commerce Revenue Management
-----------------------------
Basic tools for:
- data loading & preprocessing  
- feature engineering  
- model training & evaluation
"""

__version__ = "0.1.0"

from pathlib import Path
import logging
from logging import StreamHandler, Formatter

# ——— Project paths ———
PACKAGE_ROOT       = Path(__file__).parent
RAW_DATA_DIR       = PACKAGE_ROOT.parent / "data" / "raw"
INTERIM_DATA_DIR   = PACKAGE_ROOT.parent / "data" / "interim"
PROCESSED_DATA_DIR = PACKAGE_ROOT.parent / "data" / "processed"
FIGURES_DIR        = PACKAGE_ROOT.parent / "reports"

# ——— Logging setup ———
logger = logging.getLogger(__name__)
if not logger.handlers:
    handler = StreamHandler()
    handler.setFormatter(Formatter("[%(levelname)s %(asctime)s] %(name)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

# ——— Public API ———
# Data I/O
from .data.data import load_raw, save_processed

# Feature engineering
from .features.feature_engineering import (
    drop_unused_columns,
    add_delivery_delay,
    categorize_delivery,
)

# Modeling
from .models.train import train_rf
from .models.evaluate import evaluate_classifier

__all__ = [
    # metadata & logging
    "__version__", "logger",
    # paths
    "PACKAGE_ROOT", "RAW_DATA_DIR", "INTERIM_DATA_DIR", "PROCESSED_DATA_DIR", "FIGURES_DIR",
    # Data I/O
    "load_raw", "save_processed",
    # Feature engineering
    "drop_unused_columns", "add_delivery_delay", "categorize_delivery",
    # Modeling
    "train_rf", "evaluate_classifier",
]
