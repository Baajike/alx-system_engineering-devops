#!/usr/bin/python3
"""
Script to export data in JSON format for all tasks from all employees.
"""

import json
import requests
from sys import argv


def fetch_user_tasks(user_id):
    """
    Fetches the tasks for a specific user ID
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url, params={'userId': user_id})
    return response.json()


def export_all_tasks():
    """
    Export all tasks for all employees to a JSON file
    """
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = response.json()
    all_tasks = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks = fetch_user_tasks(user_id)
        formatted_tasks = [
            {"username": username, "task": task.get('title'), "completed": task.get('completed')}
            for task in tasks
        ]
        all_tasks[str(user_id)] = formatted_tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    export_all_tasks()
