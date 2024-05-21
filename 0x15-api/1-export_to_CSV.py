#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using a REST API and exports it to a CSV file.
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieve employee's TODO list progress based on the employee ID
    and export it to a CSV file.

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

    # CSV filename
    csv_filename = f"{employee_id}.csv"

    # Writing data to CSV file
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            writer.writerow([user_data['id'], user_data['username'], task['completed'], task['title']])

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

