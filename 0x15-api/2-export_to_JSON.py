#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
exports data in JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)).json()

    data = {employee_id: []}
    for task in todos:
        data[employee_id].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": user.get("username")
        })

    with open('{}.json'.format(employee_id), mode='w') as file:
        json.dump(data, file)

