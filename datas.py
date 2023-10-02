from pathlib import Path
import json


DIR_JSON = Path.cwd() / "data" / "data.json"


def save_task_in_json(task):
    with open(DIR_JSON, "r") as f:
        json_data = json.load(f)

    json_data.append(task)

    with open(DIR_JSON, "w") as f:
        json.dump(json_data, f, indent=4)


def delete_task_from_json(task):
    with open(DIR_JSON, "r") as f:
        json_data = json.load(f)
    json_data.remove(task)
    with open(DIR_JSON, "w") as f:
        json.dump(json_data, f, indent=4)


def clear_json_list():
    with open(DIR_JSON, "r") as f:
        json_data = json.load(f)
    json_data.clear()
    with open(DIR_JSON, "w") as f:
        json.dump(json_data, f, indent=4)


def get_tasks_from_json():
    with open(DIR_JSON, "r") as f:
        json_data = json.load(f)

    return json_data