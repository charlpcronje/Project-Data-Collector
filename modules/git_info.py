# modules/git_info.py
# Version: 1.0.1

import subprocess
from typing import Dict, Any
from .base_module import BaseModule


class GitInfo(BaseModule):
    def collect_data(self, base_path: str) -> Dict[str, Any]:
        """Collect Git information: last commit message, author, and contributors"""
        return {
            "last_commit_message": self.get_last_commit_message(base_path),
            "last_commit_author": self.get_last_commit_author(base_path),
            "contributors": self.get_contributors(base_path)
        }

    def get_last_commit_message(self, base_path: str) -> str:
        """Get the last commit message"""
        command = ['git', '-C', base_path, 'log', '-1', '--pretty=format:%s']
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            self.log('Collected last commit message', 'info')
            return result.stdout
        self.log('Failed to collect last commit message', 'error')
        return "unknown"

    def get_last_commit_author(self, base_path: str) -> str:
        """Get the last commit author"""
        command = ['git', '-C', base_path, 'log', '-1', '--pretty=format:%an']
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            self.log('Collected last commit author', 'info')
            return result.stdout
        self.log('Failed to collect last commit author', 'error')
        return "unknown"

    def get_contributors(self, base_path: str) -> Any:
        """Get the list of contributors"""
        command = ['git', '-C', base_path, 'shortlog', '-sn']
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            contributors = []
            for line in result.stdout.split('\n'):
                if line:
                    count, name = line.strip().split('\t')
                    contributors.append({"name": name, "commits": int(count)})
            self.log('Collected contributors', 'info')
            return contributors
        self.log('Failed to collect contributors', 'error')
        return []
