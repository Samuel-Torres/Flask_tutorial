"""
Auto-register all blueprints from subpackages in the endpoints package.
"""

import pkgutil
import importlib
from flask import Flask, Blueprint


def register_blueprints(app: Flask):
    """Register all Blueprints found in the endpoints package and its subpackages."""
    package_name = __name__  # flaskProject.endpoints

    for _, module_name, is_pkg in pkgutil.iter_modules(__path__):
        if is_pkg:
            full_module_name = f"{package_name}.{module_name}.{module_name}"  # e.g. endpoints.users.users
            try:
                module = importlib.import_module(full_module_name)

                # find all Blueprint instances in the module
                for item in vars(module).values():
                    if isinstance(item, Blueprint):
                        app.register_blueprint(item)
                        print(f"Registered blueprint: {item.name}")
            except Exception as e:
                print(f"Failed to register {full_module_name}: {e}")
