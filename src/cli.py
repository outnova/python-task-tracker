import cmd
from datetime import datetime, timezone
from . import data_manager
from . import task_logic

class TaskTrackerCLI(cmd.Cmd):
    data_manager.create_json()
    prompt = ">> "
    intro = "Welcome to the Python Task Tracker!\nUse 'help' or 'exit'"

    def do_add(self, taskname):
        try:
            if len(taskname) == 0:
                print("Usage: add <description>")
                return

            data = data_manager.get_json_data()
            next_id = task_logic.get_next_id(data)
            utc_timestamp = datetime.now(timezone.utc).timestamp()

            new_task = {
                "id": next_id,
                "description": taskname,
                "status": "todo",
                "createdAt": utc_timestamp,
                "updatedAt": None,
            }

            data.append(new_task)

            data_manager.store_json_data(data)
            print(f"Task added successfully (ID: {next_id})")
        except:
            print("Error: Couldn't add the task.")

    def do_update(self, line):
        try:
            args = line.split()

            if len(args) < 2:
                print("Usage: update <ID> <new_description>")
                return
            
            taskid = args[0]
            taskname = " ".join(args[1:])

            try:
                taskid = int(taskid)
            except ValueError:
                print("Error: ID must be a integer.")
                return
            
            task_logic.update_task(taskid, taskname)
        except:
            print("Error: Couldn't update the task.")
        
    def do_delete(self, task):
        try:
            try:
                taskid = int(task)
            except ValueError:
                print("Error: ID must be a integer.")
                return
            
            task_logic.delete_task(taskid)
            
        except:
            print("Error: Couldn't delete the task.")

    def do_mark_in_progress(self, task):
        try:
            try:
                taskid = int(task)
            except ValueError:
                print("Error: ID must be a integer.")
                return
            
            task_logic.update_task_status(taskid, "in-progress")

        except:
            print("Error: Couldn't update the task status.")

    def do_mark_done(self, task):
        try:
            try:
                taskid = int(task)
            except ValueError:
                print("Error: ID must be a integer.")
                return
            
            task_logic.update_task_status(taskid, "done")

        except:
            print("Error: Couldn't update the task status.")

    def do_list(self, status):
        if status == '':
            data = data_manager.get_json_data()
            count = 0
            for item in data:
                if "id" in item and item["id"]:
                    count += 1
                    if(count == 1): print("List of Tasks:")
                    print(f"ID: {item["id"]}, Task: {item["description"]}, Progress: {item["status"]}")

            if count == 0:
                print("No hay tareas.")
        else:
            if status != 'done' and status != 'todo' and status != 'in-progress':
                print("Available options: done, todo, in-progress")
                return
            
            task_list = []
            task_list = task_logic.tasks_by_status(status)
            count = 0

            if task_list:
                for item in task_list:
                    if "id" in item and item["id"]:
                        count += 1
                        if(count == 1): print(f"List of Tasks ({status}):")
                        print(f"ID: {item["id"]}, Task: {item["description"]}")
            else:
                print("There isn't tasks with that status.")

    def do_exit(self, line):
        return True
    
    def do_help(self, line):
        print("Available commands:")
        print("add [description]")
        print("update [id] [description]")
        print("delete [id]")
        print("list")
        print("mark_in_progress [id]")
        print("mark_done [id]")
        print("list done")
        print("list todo")
        print("list in-progress")

def main():
    TaskTrackerCLI().cmdloop()