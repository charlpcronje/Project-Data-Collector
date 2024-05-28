# modules/environment.py
# Version: 1.0.1

import os
from dotenv import dotenv_values
from typing import Dict
from .base_module import BaseModule


class Environment(BaseModule):
    def collect_data(self, base_path: str) -> Dict[str, str]:
        """Collect environment variables from .env file"""
        env_path = os.path.join(base_path, '.env')
        if os.path.exists(env_path):
            env_vars = {k: v for k, v in dotenv_values(
                env_path).items() if v is not None}
            self.log(
                f'Collected environment variables from {env_path}', 'info')
            return env_vars
        self.log(f'{env_path} not found', 'error')
        return {}
