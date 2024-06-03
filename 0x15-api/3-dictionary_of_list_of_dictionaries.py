#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(url).json()

    data = {
            user.get("id"): [{
                "task": ts.get("title"),
                "completed": ts.get("completed"),
                "username": user.get("username")
            } for ts in requests.get((url +
                                     "{}/todos")
                                     .format(user.get("id"))).json()]
            for user in users}

    with open("todo_all_employees.json", "w", newline="") as jsonfile:
        json.dump(data, jsonfile)
