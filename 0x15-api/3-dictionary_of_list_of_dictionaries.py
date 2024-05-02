#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
and export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == '__main__':
    full_url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(full_url)
    users = response.json()

    dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        full_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        full_url = full_url + '/todos/'
        response = requests.get(full_url)
        tasks = response.json()
        dict[user_id] = []
        for task in tasks:
            dict[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dict, file)
