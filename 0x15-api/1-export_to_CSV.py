#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID,
exports data in CSV format.
"""
import csv
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

    with open('{}.csv'.format(employee_id), mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, user.get("username"), task.get(
                "completed"), task.get("title")])

