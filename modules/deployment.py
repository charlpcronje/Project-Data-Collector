# modules/deployment.py
# Version: 1.0.1

import os
from typing import Dict
from .base_module import BaseModule


class Deployment(BaseModule):
    def collect_data(self, base_path: str) -> Dict[str, str]:
        """Collect deployment platform and configuration file"""
        deployment_info = {
            "platform": self.detect_platform(base_path),
            "config_file": self.get_deployment_config_file(base_path)
        }
        return deployment_info

    def detect_platform(self, base_path: str) -> str:
        """Detect the deployment platform used in the project"""
        procfile_path = os.path.join(base_path, 'Procfile')
        if os.path.exists(procfile_path):
            self.log('Detected deployment platform: heroku', 'info')
            return "heroku"
        self.log('Deployment platform unknown', 'warning')
        return "unknown"

    def get_deployment_config_file(self, base_path: str) -> str:
        """Get the deployment configuration file used in the project"""
        procfile_path = os.path.join(base_path, 'Procfile')
        if os.path.exists(procfile_path):
            self.log('Found deployment config file: Procfile', 'info')
            return "Procfile"
        self.log('Deployment config file not found', 'warning')
        return "none"
