"""
This file makes the models directory a package and gives you one shared Base:

PACKAGE:
auto-loads every file inside models/ so you don’t need to manually
add new imports when you make more schemas
"""

import pkgutil
import importlib
from sqlalchemy.orm import declarative_base

# creates table if it doesn't exist
Base = declarative_base()

# Auto-discover and import all modules inside this package
PACKAGE = __name__
for _, module_name, _ in pkgutil.iter_modules(__path__):
    if module_name.endswith("_model"):
        importlib.import_module(f"{PACKAGE}.{module_name}")
