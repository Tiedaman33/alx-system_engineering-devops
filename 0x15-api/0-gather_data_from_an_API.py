#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using a REST API.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve employee's TODO list progress based on the employee ID.

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

    # Count completed tasks
    completed_tasks = [task for task in todo_data if task.get('completed')]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    # Display employee's TODO list progress
    print(f"Employee {user_data['name']} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

