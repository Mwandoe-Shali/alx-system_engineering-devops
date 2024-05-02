#!/usr/bin/python3
"""
A Script that, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    full_url = base_url + "/" + employee_id

    response = requests.get(full_url)
    employee_name = response.json().get('name')

    todo_url = full_url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done_no = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done_no += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_no, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
