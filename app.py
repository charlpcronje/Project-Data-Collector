# app.py
# Version: 1.0.1

from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
from singleton_collector import ProjectDataCollector

load_dotenv()

app = Flask(__name__)
collector = ProjectDataCollector('config.json')


@app.route('/collect', methods=['POST'])
def collect_data():
    """Endpoint to collect data for specified project paths"""
    project_paths = request.json.get(
        'project_paths', []) if request.json else []
    collector.collect_data_for_all_projects(project_paths)
    return jsonify(collector.projects)


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=int(os.getenv('PORT', 5000)))
