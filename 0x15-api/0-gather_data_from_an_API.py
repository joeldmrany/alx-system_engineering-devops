#!/usr/bin/python3
"""
REST API
"""

import requests
import sys


if __name__ == '__main__':
    E_Id = sys.argv[1]
    Ba_url = "https://jsonplaceholder.typicode.com/users"
    link = Ba_url + "/" + E_Id

    answer = requests.get(link)
    E_Name = answer.json().get('name')

    todoUrl = link + "/todos"
    answer = requests.get(todoUrl)
    tasks = answer.json()
    completed = 0
    completed_tasks = []

    for work in tasks:
        if work.get('completed'):
            completed_tasks.append(work)
            completed += 1

    print("Employee {} is completed with tasks({}/{}):"
          .format(E_Name, completed, len(tasks)))

    for work in completed_tasks:
        print("\t {}".format(work.get('title')))
