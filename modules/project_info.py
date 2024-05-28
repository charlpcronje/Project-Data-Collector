# modules/project_info.py
# Version: 1.0.1

import os
import json
from typing import Dict, Any
from .base_module import BaseModule


class ProjectInfo(BaseModule):
    def collect_data(self, base_path: str) -> Dict[str, Any]:
        """Collect project information from package.json"""
        package_json_path = os.path.join(base_path, 'package.json')
        if os.path.exists(package_json_path):
            with open(package_json_path, 'r') as f:
                package_data = json.load(f)
                self.log(
                    f'Collected project info from {package_json_path}', 'info')
                return {
                    "name": package_data.get("name"),
                    "description": package_data.get("description"),
                    "version": package_data.get("version"),
                    "author": package_data.get("author"),
                    "license": package_data.get("license"),
                    "repository": package_data.get("repository")
                }
        self.log(f'{package_json_path} not found', 'error')
        return {}
