import os
import re


def create_file_from_code_blocks(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regex to find all code blocks and their respective file paths
    code_block_pattern = re.compile(
        r"```python\n# ([^\n]+)\n# Version: [^\n]+\n(.*?)```", re.DOTALL)
    matches = code_block_pattern.findall(content)

    for relative_path, code in matches:
        # Normalize the relative path
        relative_path = relative_path.strip()
        code = code.strip()

        # Create necessary directories
        dir_path = os.path.dirname(relative_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        # Write the code to the file
        with open(relative_path, 'w') as file:
            file.write(code)


if __name__ == "__main__":
    input_file_path = '/mnt/data/Your Responses.md'
    create_file_from_code_blocks(input_file_path)
