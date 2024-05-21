#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using a REST API and exports it to a JSON file.
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve employee's TODO list progress based on the employee ID
    and export it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Base URL of the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Endpoint for fetching user details
    user_endpoint = f"{base_url}/users/{employee_id}"

    # Endpoint for fetching user's TODO list
    todo_endpoint = f"{base_url}/todos?userId={employee_id}"

    # Fetching user details
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()

    # Fetching user's TODO list
    todo_response = requests.get(todo_endpoint)
    todo_data = todo_response.json()

    # JSON filename
    json_filename = f"{employee_id}.json"

    # Collecting data for JSON
    json_data = {"USER_ID": []}
    for task in todo_data:
        json_data["USER_ID"].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": user_data['username']
        })

    # Writing data to JSON file
    with open(json_filename, 'w') as file:
        json.dump(json_data, file, indent=4)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

