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
    empl_id = sys.argv[1]
    employee = requests.get((url + "{}").format(empl_id)).json()
    user_name = employee.get("username")
    todos = requests.get((url + "{}/todos").format(empl_id)).json()

    data = {empl_id: [{
                "task": ts.get("title"),
                "completed": ts.get("completed"),
                "username": user_name
            } for ts in todos]}
    with open("{}.json".format(empl_id), "w", newline="") as jsonfile:
        json.dump(data, jsonfile)
