# modules/ignore_folders.py
# Version: 1.0.1

from typing import Dict
from .base_module import BaseModule


class IgnoreFolders(BaseModule):
    def collect_data(self, base_path: str) -> Dict[str, list]:
        """Collect ignore folders information"""
        self.log('Collected ignore folders information', 'info')
        return {
            "default_ignore": ['node_modules', 'dist', '.git', 'vendor'],
            "custom_ignore": ['logs', 'temp'],
            "custom_include": ['src/config', 'tests/e2e']
        }
