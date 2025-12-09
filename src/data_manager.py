import os
import json

FILEPATH = 'src/tasks.json'

def get_json_data():
    with open(FILEPATH) as json_file:
        data = json.load(json_file)
    return data.get("tasks", [])

def store_json_data(data):
    data_to_store = {
        "tasks": data
    }
    with open(FILEPATH, 'w') as outfile:
        json.dump(data_to_store, outfile, indent=4)

def create_json():
    if not os.path.exists(FILEPATH):
        print(f"Creating {FILEPATH} file...")
        data = {"tasks": []}
        with open(FILEPATH, 'w') as f:
            json.dump(data, f, indent=4)
    else:
        pass