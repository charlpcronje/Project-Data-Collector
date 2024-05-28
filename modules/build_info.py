# modules/build_info.py
# Version: 1.0.1

import os
from typing import Dict
from .base_module import BaseModule


class BuildInfo(BaseModule):
    def collect_data(self, base_path: str) -> Dict[str, str]:
        """Collect build tool and configuration file information"""
        build_info = {
            "tool": self.get_build_tool(base_path),
            "config_file": self.get_build_config_file(base_path)
        }
        return build_info

    def get_build_tool(self, base_path: str) -> str:
        """Get the build tool used in the project"""
        if os.path.exists(os.path.join(base_path, 'webpack.config.js')):
            self.log('Detected webpack as build tool', 'info')
            return "webpack"
        self.log('No build tool detected', 'warning')
        return "unknown"

    def get_build_config_file(self, base_path: str) -> str:
        """Get the build configuration file used in the project"""
        if os.path.exists(os.path.join(base_path, 'webpack.config.js')):
            self.log('Detected webpack.config.js as build config file', 'info')
            return "webpack.config.js"
        self.log('No build config file detected', 'warning')
        return "none"
