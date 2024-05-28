# project_data_factory.py
# Version: 1.0.1

import os
import json
import importlib
from utils.logger import Logger
from typing import Dict, Any


class ProjectDataFactory:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.projects: Dict[str, Any] = {}
        self.logger = Logger(
            os.getenv('LOG_FILE_PATH', 'logs/logs.log')).get_logger()
        self.load_config()

    def load_config(self):
        """Load the configuration from the JSON file"""
        with open(self.config_path, 'r') as f:
            self.config = json.load(f)

    def get_module(self, module_name: str):
        """Dynamically import the specified module"""
        return importlib.import_module(f'modules.{module_name}')

    def collect_data(self, base_path: str):
        """Collect data for the specified project"""
        project_data = self.process_section(base_path, self.config['project'])
        self.projects[base_path] = project_data

    def process_section(self, base_path: str, section: Dict[str, Any]) -> Dict[str, Any]:
        """Process a section of the configuration and collect data"""
        data = {}
        for key, module_name in section.items():
            if isinstance(module_name, dict):
                data[key] = self.process_section(base_path, module_name)
            else:
                module = self.get_module(module_name)
                class_name = ''.join([part.capitalize()
                                     for part in module_name.split('_')])
                instance = getattr(module, class_name)(self.logger)
                data[key] = instance.collect_data(base_path)
        return data
