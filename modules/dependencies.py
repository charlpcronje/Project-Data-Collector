# modules/dependencies.py
# Version: 1.0.1

import os
import json
from typing import Dict, Any
from .base_module import BaseModule


class Dependencies(BaseModule):
    def collect_data(self, base_path: str) -> Dict[str, Any]:
        """Collect dependencies for Python, PHP, and Node.js"""
        dependencies = {
            "python": self.get_python_dependencies(base_path),
            "php": self.get_php_dependencies(base_path),
            "node": self.get_node_dependencies(base_path)
        }
        return dependencies

    def get_python_dependencies(self, base_path: str) -> Any:
        """Get Python dependencies from requirements.txt"""
        requirements_path = os.path.join(base_path, 'requirements.txt')
        if os.path.exists(requirements_path):
            with open(requirements_path, 'r') as f:
                deps = [line.strip() for line in f if line.strip()]
                self.log(
                    f'Collected Python dependencies from {requirements_path}', 'info')
                return deps
        self.log(f'{requirements_path} not found', 'error')
        return []

    def get_php_dependencies(self, base_path: str) -> Any:
        """Get PHP dependencies from composer.json"""
        composer_path = os.path.join(base_path, 'composer.json')
        if os.path.exists(composer_path):
            with open(composer_path, 'r') as f:
                composer_data = json.load(f)
                self.log(
                    f'Collected PHP dependencies from {composer_path}', 'info')
                return composer_data.get("require", [])
        self.log(f'{composer_path} not found', 'error')
        return []

    def get_node_dependencies(self, base_path: str) -> Dict[str, Any]:
        """Get Node.js dependencies from package.json"""
        package_json_path = os.path.join(base_path, 'package.json')
        if os.path.exists(package_json_path):
            with open(package_json_path, 'r') as f:
                package_data = json.load(f)
                self.log(
                    f'Collected Node.js dependencies from {package_json_path}', 'info')
                return {
                    "dependencies": package_data.get("dependencies", {}),
                    "devDependencies": package_data.get("devDependencies", {})
                }
        self.log(f'{package_json_path} not found', 'error')
        return {}
