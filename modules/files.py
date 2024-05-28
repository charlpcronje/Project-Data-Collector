# modules/files.py
# Version: 1.0.1

import os
import json
import subprocess
from datetime import datetime
from typing import Dict, Any
from .base_module import BaseModule


class Files(BaseModule):
    def collect_data(self, base_path: str) -> Dict[str, Any]:
        """Collect information about files in the project"""
        files_info = {
            "counts": self.get_file_counts(base_path),
            "extensions": self.get_file_extensions(base_path),
            "last_updated_file": self.get_last_file_info(base_path, 'updated'),
            "last_created_file": self.get_last_file_info(base_path, 'created'),
            "last_deleted_file": self.get_last_file_info(base_path, 'deleted'),
            "lines_of_code": self.get_lines_of_code(base_path)
        }
        return files_info

    def get_file_counts(self, base_path: str) -> Dict[str, int]:
        """Count the total number of files in the project"""
        ignore_folders = ['node_modules', 'dist', '.git', 'vendor']
        total_files = 0
        for root, dirs, files in os.walk(base_path):
            if any(ignored in root for ignored in ignore_folders):
                continue
            total_files += len(files)
        self.log(f'Collected file counts for {base_path}', 'info')
        return {"total_files": total_files}

    def get_file_extensions(self, base_path: str) -> Dict[str, int]:
        """Count the number of files by extension"""
        extensions = {}
        for root, dirs, files in os.walk(base_path):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in extensions:
                    extensions[ext] += 1
                else:
                    extensions[ext] = 1
        self.log(f'Collected file extensions for {base_path}', 'info')
        return extensions

    def get_last_file_info(self, base_path: str, action: str) -> Dict[str, str]:
        """Get information about the last updated, created, or deleted file"""
        command = ['git', '-C', base_path, 'log', '-1', '--diff-filter={}'.format(
            action[0].upper()), '--name-only', '--pretty=format:%H %ci']
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.split('\n')
            if len(lines) > 1:
                file_info = {
                    "path": lines[1],
                    "timestamp": lines[0].split()[1] + " " + lines[0].split()[2]
                }
                self.log(
                    f'Collected last {action} file info for {base_path}', 'info')
                return file_info
        self.log(f'No files {action} recently in {base_path}', 'warning')
        return {}

    def get_lines_of_code(self, base_path: str) -> Dict[str, Any]:
        """Get the lines of code in the project using cloc"""
        command = ['cloc', base_path, '--json']
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            cloc_data = json.loads(result.stdout)
            self.log(f'Collected lines of code for {base_path}', 'info')
            return cloc_data
        self.log(f'Failed to collect lines of code for {base_path}', 'error')
        return {}
