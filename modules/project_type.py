# modules/project_type.py
# Version: 1.0.1

import os
import json
from typing import Dict, Any
from .base_module import BaseModule


class ProjectType(BaseModule):
    def collect_data(self, base_path: str) -> Dict[str, Any]:
        """Collect project type, framework, and entry point"""
        project_type = self.detect_project_type(base_path)
        framework = self.detect_framework(base_path)
        entry_point = self.detect_entry_point(base_path)
        return {
            "project_type": project_type,
            "framework": framework,
            "entry_point": entry_point
        }

    def detect_project_type(self, base_path: str) -> str:
        """Detect the type of project based on its files"""
        if os.path.exists(os.path.join(base_path, 'package.json')):
            self.log('Detected project type: node', 'info')
            return "node"
        elif os.path.exists(os.path.join(base_path, 'requirements.txt')):
            self.log('Detected project type: python', 'info')
            return "python"
        elif os.path.exists(os.path.join(base_path, 'composer.json')):
            self.log('Detected project type: php', 'info')
            return "php"
        self.log('Project type unknown', 'warning')
        return "unknown"

    def detect_framework(self, base_path: str) -> str:
        """Detect the framework used in the project"""
        if os.path.exists(os.path.join(base_path, 'package.json')):
            with open(os.path.join(base_path, 'package.json'), 'r') as f:
                package_data = json.load(f)
                dependencies = package_data.get("dependencies", {})
                if "express" in dependencies:
                    self.log('Detected framework: express', 'info')
                    return "express"
                elif "react" in dependencies:
                    self.log('Detected framework: react', 'info')
                    return "react"
        self.log('Framework unknown', 'warning')
        return "unknown"

    def detect_entry_point(self, base_path: str) -> str:
        """Detect the entry point file of the project"""
        if os.path.exists(os.path.join(base_path, 'src/index.js')):
            self.log('Detected entry point: src/index.js', 'info')
            return "src/index.js"
        self.log('Entry point unknown', 'warning')
        return "unknown"
