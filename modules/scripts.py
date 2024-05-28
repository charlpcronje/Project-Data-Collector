# modules/scripts.py
# Version: 1.0.1

import os
import json
from typing import Dict
from .base_module import BaseModule


class Scripts(BaseModule):
    def collect_data(self, base_path: str) -> Dict[str, str]:
        """Collect scripts from package.json"""
        package_json_path = os.path.join(base_path, 'package.json')
        if os.path.exists(package_json_path):
            with open(package_json_path, 'r') as f:
                package_data = json.load(f)
                self.log(f'Collected scripts from {package_json_path}', 'info')
                return package_data.get("scripts", {})
        self.log(f'{package_json_path} not found', 'error')
        return {}
