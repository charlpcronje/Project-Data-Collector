# singleton_collector.py
# Version: 1.0.1

from utils.singleton import Singleton
from project_data_factory import ProjectDataFactory
from typing import List, Dict, Any
import json


class ProjectDataCollector(metaclass=Singleton):
    def __init__(self, config_path: str):
        self.factory = ProjectDataFactory(config_path)
        self.projects: Dict[str, Any] = {}

    def collect_data_for_all_projects(self, base_paths: List[str]):
        """Collect data for all specified projects"""
        for base_path in base_paths:
            self.factory.collect_data(base_path)
            self.projects[base_path] = self.factory.projects[base_path]


# Usage example
if __name__ == '__main__':
    import os
    from dotenv import load_dotenv

    load_dotenv()
    collector = ProjectDataCollector('config.json')
    collector.collect_data_for_all_projects(
        ['/path/to/project1', '/path/to/project2'])
    print(json.dumps(collector.projects, indent=2))
