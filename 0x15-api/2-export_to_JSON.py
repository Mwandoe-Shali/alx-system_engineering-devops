#!/usr/bin/python3
"""
A sript that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in the JSON format.
"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    full_url = base_url + "/" + employee_id

    response = requests.get(full_url)
    username = response.json().get('username')

    todo_url = full_url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    dict = {employee_id: []}
    for task in tasks:
        dict[employee_id].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        })
    with open('{}.json'.format(employee_id), 'w') as filename:
        json.dump(dict, filename)
