#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    empl_id = sys.argv[1]
    employee = requests.get((url + "{}").format(empl_id)).json()
    user_name = employee.get("username")
    todos = requests.get((url + "{}/todos").format(empl_id)).json()

    with open("{}.csv".format(empl_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for ts in todos:
            writer.writerow([empl_id, user_name,
                             ts.get("completed"), ts.get("title")])
