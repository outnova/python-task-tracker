from datetime import datetime, timezone
from . import data_manager

def get_next_id(data):
    if not data:
        return 1
    
    existing_ids = set()

    for item in data:
        if "id" in item:
            try:
                existing_ids.add(int(item["id"]))
            except (ValueError, TypeError) as e:
                continue

    if not existing_ids:
        return 1
    
    max_id = max(existing_ids)

    for i in range(1, max_id + 1):
        if i not in existing_ids:
            return i
        
    return max_id + 1

def update_task(task_id, new_taskname):
    data = data_manager.get_json_data()
    utc_timestamp = datetime.now(timezone.utc).timestamp()
    found = False

    for item in data:
        if "id" in item and item["id"] == task_id:
            item["description"] = new_taskname
            item["updatedAt"] = utc_timestamp
            found = True
            break

    if found:   
        data_manager.store_json_data(data)
        print(f"Task with ID {task_id} updated successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def update_task_status(task_id, new_status):
    data = data_manager.get_json_data()
    utc_timestamp = datetime.now(timezone.utc).timestamp()
    found = False

    for item in data:
        if "id" in item and item["id"] == task_id:
            item["status"] = new_status
            item["updatedAt"] = utc_timestamp
            found = True
            break

    if found:   
        data_manager.store_json_data(data)
        print(f"Status of Task with ID {task_id} updated successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def delete_task(task_id):
    data = data_manager.get_json_data()
    found = False
    for item in data:
        if "id" in item and item["id"] == task_id:
            found = True
            break

    if found:   
        del data[task_id - 1]
        data_manager.store_json_data(data)
        print(f"Task with ID {task_id} deleted successfully.")
    else:
        print(f"Error: Task with ID {task_id} not found.")

def tasks_by_status(status):
    data = data_manager.get_json_data()
    new_list = []
    count = 0
    for item in data:
        if "id" in item and item["status"] == status:
            count += 1
            new_list.append(item)

    if count:
        return new_list