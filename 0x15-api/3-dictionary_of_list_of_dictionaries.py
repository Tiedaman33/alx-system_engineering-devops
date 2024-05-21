#!/usr/bin/python3

"""
This script retrieves information about all employees' TODO list progress
using a REST API and exports it to a JSON file.
"""

import json
import requests
import sys


def get_all_employees_todo_progress():
    """
    Retrieve all employees' TODO list progress and export it to a JSON file.

    Returns:
        None
    """
    # Base URL of the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Endpoint for fetching all users
    users_endpoint = f"{base_url}/users"

    # Fetching all users
    users_response = requests.get(users_endpoint)
    users_data = users_response.json()

    # JSON data
    json_data = {}

    for user in users_data:
        # Endpoint for fetching user's TODO list
        todo_endpoint = f"{base_url}/todos?userId={user['id']}"

        # Fetching user's TODO list
        todo_response = requests.get(todo_endpoint)
        todo_data = todo_response.json()

        # Collecting tasks for the user
        user_tasks = []
        for task in todo_data:
            user_tasks.append({
                "username": user['username'],
                "task": task['title'],
                "completed": task['completed']
            })

        # Storing tasks in JSON data
        json_data[user['id']] = user_tasks

    # JSON filename
    json_filename = "todo_all_employees.json"

    # Writing data to JSON file
    with open(json_filename, 'w') as file:
        json.dump(json_data, file, indent=4)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    get_all_employees_todo_progress()

