# Project Data Collector

## Overview

The Project Data Collector is a modular Python application designed to scan project directories and collect various pieces of information such as project metadata, dependencies, environment variables, documentation, and more. This data is collected using various modules that adhere to a common interface and can be easily extended or modified.

## Features

- Modular architecture for easy extension and maintenance
- Collects project information, dependencies, environment variables, documentation, and more
- Uses Git to collect commit and contributor information
- Supports both Flask endpoints and terminal execution for data collection
- Comprehensive logging to both terminal and file


### Data to collect from each project

1. Project Information (project_info.py)
    - name: Extracted from `package.json` (Node.js), `setup.py` (Python), or similar project file.
    - description: Extracted from `package.json` (Node.js), `setup.py` (Python), or similar project file.
    - version: Extracted from `package.json` (Node.js), `setup.py` (Python), or similar project file.
    - author: Extracted from `package.json` (Node.js), `setup.py` (Python), or similar project file.
    - license: Extracted from `package.json` (Node.js), `setup.py` (Python), or similar project file.
    - repository: Extracted from `package.json` (Node.js), `setup.py` (Python), or similar project file.

2. Dependencies (dependencies.py)
    - python: Extracted from `requirements.txt`.
    - php: Extracted from `composer.json`.
    - node: Extracted from `package.json` (dependencies and devDependencies).

3. Scripts (scripts.py)
    - start: Extracted from `package.json`.
    - test: Extracted from `package.json`.

4. Build Information (build_info.py)
    - tool: Inferred from the presence of files like `webpack.config.js`.
    - config_file: Inferred from the presence of files like `webpack.config.js`.

5. Environment Variables (environment.py)
    - variables: Extracted from `.env`.

6. Documentation (documentation.py)
    - readme: Detected by the presence of `README.md`.
    - changelog: Detected by the presence of `CHANGELOG.md`.
    - contributing: Detected by the presence of `CONTRIBUTING.md`.

7. Metadata (metadata.py)
    - created_at: Extracted using `os.stat` to get file creation time.
    - updated_at: Extracted using `os.stat` to get file modification time.

8. Project Type (project_type.py)
    - project_type: Inferred from the presence of `package.json` (Node.js), `requirements.txt` (Python), `composer.json` (PHP).
    - framework: Inferred from dependencies in `package.json` (e.g., presence of `express` for Express.js).
    - entry_point: Inferred from common entry point files like `src/index.js`.

9. Deployment Information (deployment.py)
    - platform: Inferred from the presence of deployment files like `Procfile`.
    - config_file: Inferred from the presence of deployment files like `Procfile`.

10. Files (files.py)
    - counts: Total file counts excluding and including ignored folders, using `os.walk`.
    - extensions: Count of files by extension, using `os.walk`.
    - last_updated_file: Last updated file information using `git log`.
    - last_created_file: Last created file information using `git log`.
    - last_deleted_file: Last deleted file information using `git log`.
    - lines_of_code: Counted using `cloc`.

11. Git Information (git_info.py)
    - last_commit_message: Extracted using `git log`.
    - last_commit_author: Extracted using `git log`.
    - contributors: Extracted using `git shortlog -sn`.

12. Repository Information (repo_info.py)
    - open_issues: Placeholder, ideally extracted using GitHub/GitLab API.
    - closed_issues: Placeholder, ideally extracted using GitHub/GitLab API.
    - pull_requests: Placeholder, ideally extracted using GitHub/GitLab API.
        - open: Placeholder.
        - closed: Placeholder.
        - merged: Placeholder.

13. CI/CD Information (ci_cd.py)
    - enabled: Placeholder, typically extracted from CI/CD configuration files.
    - tool: Placeholder, typically inferred from CI/CD configuration files.
    - status: Placeholder, typically extracted from CI/CD service API.

14. Test Coverage (test_coverage.py)
    - percentage: Placeholder, typically extracted from test coverage reports.
    - tool: Placeholder, inferred from the testing tool used.

15. Code Quality (code_quality.py)
    - score: Placeholder, typically extracted from code quality reports.
    - tool: Placeholder, inferred from the code quality tool used.

16. Security Vulnerabilities (security.py)
    - count: Placeholder, typically extracted from security scanning tools.
    - last_scanned: Placeholder, typically extracted from security scanning tools.
    - tool: Placeholder, inferred from the security scanning tool used.

17. Ignore Folders (ignore_folders.py)
    - default_ignore: Default ignored folders (`node_modules`, `dist`, `.git`, `vendor`).
    - custom_ignore: Custom ignored folders (`logs`, `temp`).
    - custom_include: Custom included folders (`src/config`, `tests/e2e`).

## Prerequisites

- Conda
- Git
- Python 3.8+
- Flask
- Cloc
- Python-dotenv

## Installation

### Step 1: Clone the Repository

```sh
git clone https://github.com/yourusername/project_data_collector.git
cd project_data_collector
```

### Step 2: Create and Activate Conda Environment

```sh
conda create -n project_data_collector_env python=3.8
conda activate project_data_collector_env
```

### Step 3: Install Required Packages

```sh
pip install flask python-dotenv cloc
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the project root with the following content:

```conf
FLASK_APP=app.py
FLASK_ENV=production
HOST=0.0.0.0
PORT=5000
LOG_FILE_PATH=logs/app.log
```

### Step 5: Set Up Project Structure

Ensure the project directory has the following structure:

```sh
project_data_collector/
├── .env
├── README.md
├── app.py
├── config.json
├── logs/
│   └── app.log
├── modules/
│   ├── __init__.py
│   ├── base_module.py
│   ├── project_info.py
│   ├── dependencies.py
│   ├── scripts.py
│   ├── build_info.py
│   ├── environment.py
│   ├── documentation.py
│   ├── metadata.py
│   ├── project_type.py
│   ├── deployment.py
│   ├── files.py
│   ├── git_info.py
│   ├── repo_info.py
│   ├── ci_cd.py
│   ├── test_coverage.py
│   ├── code_quality.py
│   ├── security.py
│   └── ignore_folders.py
└── utils/
    ├── __init__.py
    ├── logger.py
    └── singleton.py
```

## Usage

### Running the Flask App

To run the Flask app, use the following command:

```sh
flask run
```

### Using the Terminal

To collect data for specific project directories via terminal, you can run the following script:

```sh
python singleton_collector.py
```

### API Endpoints

#### Collect Data

- **Endpoint**: `/collect`
- **Method**: POST
- **Request Body**: JSON object with an array of project paths

Example:

```sh
curl -X POST http://localhost:5000/collect -H "Content-Type: application/json" -d '{"project_paths": ["/path/to/project1", "/path/to/project2"]}'
```

## Logging

Logs are written to both the terminal and a log file located at `logs/app.log`. The log file is rotated to ensure it does not exceed 5 MB and maintains up to 5 backup files.

## Extending the Application

To add a new data collection module, follow these steps:

1. Create a new Python file in the `modules/` directory.
2. Implement a class that inherits from `BaseModule` and implements the `collect_data` method.
3. Update `config.json` to include the new module for the relevant data section.

## License

This project is licensed under the MIT License.
```

This setup ensures a modular, maintainable, and production-ready application for collecting project data. Each module adheres to a common interface, supports logging, and integrates with a Flask app for triggering data collection.



# Project Data Collector

## Overview

The Project Data Collector is a modular Python application designed to scan project directories and collect various pieces of information such as project metadata, dependencies, environment variables, documentation, and more. This data is collected using various modules that adhere to a common interface and can be easily extended or modified.

## Features

- Modular architecture for easy extension and maintenance
- Collects project information, dependencies, environment variables, documentation, and more
- Uses Git to collect commit and contributor information
- Supports both Flask endpoints and terminal execution for data collection
- Comprehensive logging to both terminal and file

### Data to collect from each project

```sh
1. Project Information (project_info.py)
    - name: Extracted from `package.json` (Node.js), `setup.py` (Python), or similar project file.
    - description: Extracted from `package.json` (Node.js), `setup.py` (Python), or similar project file.
    - version: Extracted from `package.json` (Node.js), `setup.py` (Python), or similar project file.
    - author: Extracted from `package.json` (Node.js), `setup.py` (Python), or similar project file.
    - license: Extracted from `package.json` (Node.js), `setup.py` (Python), or similar project file.
    - repository: Extracted from `package.json` (Node.js), `setup.py` (Python), or similar project file.

2. Dependencies (dependencies.py)
    - python: Extracted from `requirements.txt`.
    - php: Extracted from `composer.json`.
    - node: Extracted from `package.json` (dependencies and devDependencies).

3. Scripts (scripts.py)
    - start: Extracted from `package.json`.
    - test: Extracted from `package.json`.

4. Build Information (build_info.py)
    - tool: Inferred from the presence of files like `webpack.config.js`.
    - config_file: Inferred from the presence of files like `webpack.config.js`.

5. Environment Variables (environment.py)
    - variables: Extracted from `.env`.

6. Documentation (documentation.py)
    - readme: Detected by the presence of `README.md`.
    - changelog: Detected by the presence of `CHANGELOG.md`.
    - contributing: Detected by the presence of `CONTRIBUTING.md`.

7. Metadata (metadata.py)
    - created_at: Extracted using `os.stat` to get file creation time.
    - updated_at: Extracted using `os.stat` to get file modification time.

8. Project Type (project_type.py)
    - project_type: Inferred from the presence of `package.json` (Node.js), `requirements.txt` (Python), `composer.json` (PHP).
    - framework: Inferred from dependencies in `package.json` (e.g., presence of `express` for Express.js).
    - entry_point: Inferred from common entry point files like `src/index.js`.

9. Deployment Information (deployment.py)
    - platform: Inferred from the presence of deployment files like `Procfile`.
    - config_file: Inferred from the presence of deployment files like `Procfile`.

10. Files (files.py)
    - counts: Total file counts excluding and including ignored folders, using `os.walk`.
    - extensions: Count of files by extension, using `os.walk`.
    - last_updated_file: Last updated file information using `git log`.
    - last_created_file: Last created file information using `git log`.
    - last_deleted_file: Last deleted file information using `git log`.
    - lines_of_code: Counted using `cloc`.

11. Git Information (git_info.py)
    - last_commit_message: Extracted using `git log`.
    - last_commit_author: Extracted using `git log`.
    - contributors: Extracted using `git shortlog -sn`.

12. Repository Information (repo_info.py)
    - open_issues: Placeholder, ideally extracted using GitHub/GitLab API.
    - closed_issues: Placeholder, ideally extracted using GitHub/GitLab API.
    - pull_requests: Placeholder, ideally extracted using GitHub/GitLab API.
        - open: Placeholder.
        - closed: Placeholder.
        - merged: Placeholder.

13. CI/CD Information (ci_cd.py)
    - enabled: Placeholder, typically extracted from CI/CD configuration files.
    - tool: Placeholder, typically inferred from CI/CD configuration files.
    - status: Placeholder, typically extracted from CI/CD service API.

14. Test Coverage (test_coverage.py)
    - percentage: Placeholder, typically extracted from test coverage reports.
    - tool: Placeholder, inferred from the testing tool used.

15. Code Quality (code_quality.py)
    - score: Placeholder, typically extracted from code quality reports.
    - tool: Placeholder, inferred from the code quality tool used.

16. Security Vulnerabilities (security.py)
    - count: Placeholder, typically extracted from security scanning tools.
    - last_scanned: Placeholder, typically extracted from security scanning tools.
    - tool: Placeholder, inferred from the security scanning tool used.

17. Ignore Folders (ignore_folders.py)
    - default_ignore: Default ignored folders (`node_modules`, `dist`, `.git`, `vendor`).
    - custom_ignore: Custom ignored folders (`logs`, `temp`).
    - custom_include: Custom included folders (`src/config`, `tests/e2e`).
```

## Prerequisites

- Conda
- Git
- Python 3.8+
- Flask
- Cloc
- Python-dotenv

## Installation

### Step 1: Clone the Repository

```sh
git clone git@github.com:charlpcronje/Project-Data-Collector.git
cd project_data_collector
```

### Step 2: Create and Activate Conda Environment

```sh
conda create -n project_data_collector_env python=3.8
conda activate project_data_collector_env
```

### Step 3: Install Required Packages

```sh
pip install flask python-dotenv cloc
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the project root with the following content:

```conf
FLASK_APP=app.py
FLASK_ENV=production
HOST=0.0.0.0
PORT=5000
LOG_FILE_PATH=logs/app.log
```

### Step 5: Set Up Project Structure

Ensure the project directory has the following structure:

```sh
project_data_collector/
├── .env
├── README.md
├── app.py
├── config.json
├── logs/
│   └── app.log
├── modules/
│   ├── __init__.py
│   ├── base_module.py
│   ├── project_info.py
│   ├── dependencies.py
│   ├── scripts.py
│   ├── build_info.py
│   ├── environment.py
│   ├── documentation.py
│   ├── metadata.py
│   ├── project_type.py
│   ├── deployment.py
│   ├── files.py
│   ├── git_info.py
│   ├── repo_info.py
│   ├── ci_cd.py
│   ├── test_coverage.py
│   ├── code_quality.py
│   ├── security.py
│   └── ignore_folders.py
└── utils/
    ├── __init__.py
    ├── logger.py
    └── singleton.py
```

## Usage

### Running the Flask App

To run the Flask app, use the following command:

```sh
flask run
```

### Using the Terminal

To collect data for specific project directories via terminal, you can run the following script:

```sh
python singleton_collector.py
```

### API Endpoints

#### Collect Data

- **Endpoint**: `/collect`
- **Method**: POST
- **Request Body**: JSON object with an array of project paths

Example:

```sh
curl -X POST http://localhost:5000/collect -H "Content-Type: application/json" -d '{"project_paths": ["/path/to/project1", "/path/to/project2"]}'
```

## Logging

Logs are written to both the terminal and a log file located at `logs/app.log`. The log file is rotated to ensure it does not exceed 5 MB and maintains up to 5 backup files.

## Extending the Application

To add a new data collection module, follow these steps:

1. Create a new Python file in the `modules/` directory.
2. Implement a class that inherits from `BaseModule` and implements the `collect_data` method.
3. Update `config.json` to include the new module for the relevant data section.

## License

This project is licensed under the MIT License.