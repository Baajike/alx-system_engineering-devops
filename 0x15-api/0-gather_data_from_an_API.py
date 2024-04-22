#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
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

    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    completed_tasks_count = len(completed_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), completed_tasks_count, total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))

