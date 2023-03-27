import requests
import json
from pytest import fixture

@fixture
def get_task():
    ENPOINT = "http://todo.pixegami.io/"
    response = requests.get(ENPOINT)
    return response.json()

ENPOINT = "http://todo.pixegami.io/"

# This script is used to get the current status of the server   

response = requests.get(ENPOINT)
print(response.json())

payload= {
    "content": "My first todo",
    "user_id": 1,
    "task_id":28,
    "is_done": True

}

response = requests.put(ENPOINT+ "/create-task", json=payload)
data= response.json()
task_id = data.get("task").get("task_id")

get_task_response = requests.get(ENPOINT + "/get-task/" + str(task_id))
print(get_task_response.json())

