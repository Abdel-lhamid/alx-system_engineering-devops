#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    empl_id = sys.argv[1]
    employee = requests.get((url + "{}").format(empl_id)).json()
    todos = requests.get((url + "{}/todos").format(empl_id)).json()
    compl_tasks = []
    for ts in todos:
        if ts.get("completed") is True:
            compl_tasks.append(ts.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(compl_tasks), len(todos)))
    for t in compl_tasks:
        print("\t {}".format(t))
