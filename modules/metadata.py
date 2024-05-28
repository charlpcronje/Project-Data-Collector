# modules/metadata.py
# Version: 1.0.2

import os
from datetime import datetime
from typing import Dict
from .base_module import BaseModule


class Metadata(BaseModule):
    def collect_data(self, base_path: str) -> Dict[str, str]:
        """Collect metadata about the project directory"""
        metadata = self.get_metadata(base_path)
        return metadata

    def get_metadata(self, path: str) -> Dict[str, str]:
        """Get creation and modification times of the project directory"""
        stat = os.stat(path)
        created_at = datetime.fromtimestamp(stat.st_ctime).isoformat()
        updated_at = datetime.fromtimestamp(stat.st_mtime).isoformat()
        self.log(f'Collected metadata for {path}', 'info')
        return {
            "created_at": created_at,
            "updated_at": updated_at
        }
