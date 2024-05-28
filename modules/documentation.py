# modules/documentation.py
# Version: 1.0.2

import os
from typing import Optional, Dict
from .base_module import BaseModule


class Documentation(BaseModule):
    def collect_data(self, base_path: str) -> Dict[str, Optional[str]]:
        """Collect documentation files information"""
        documentation = {
            "readme": self.get_file_path(base_path, 'README.md'),
            "changelog": self.get_file_path(base_path, 'CHANGELOG.md'),
            "contributing": self.get_file_path(base_path, 'CONTRIBUTING.md')
        }
        return documentation

    def get_file_path(self, base_path: str, filename: str) -> Optional[str]:
        """Check if a documentation file exists"""
        file_path = os.path.join(base_path, filename)
        if os.path.exists(file_path):
            self.log(f'Found documentation file: {file_path}', 'info')
            return filename
        self.log(f'Documentation file {filename} not found', 'warning')
        return None
