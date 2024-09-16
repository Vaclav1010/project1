ukoly = []

def add_task(name):
    new_task = {
        "name": name,
        "status": False
    }            
    ukoly.append(new_task)
    print(f"Task '{name}' has been added to register.")


def show_task():
    if len(ukoly) == 0:
        print("Your task register is empty.")
    else:
        print("Task register: ")
        for index, task in enumerate(ukoly, start = 1):
            status = "Complete" if task["status"] else "Not finished"
            print(f"{index}. {task["name"]} - {status}")

def mark_as_done(index):
    if index <= 0 or index > len(ukoly):
        print("Invalid index!")
    else:
        ukoly[index - 1]["status"] = True
        print(f"Task {ukoly[index - 1]["name"]} has been marked as done.")

def delete_task(index):
    if index <= 0 or index > len(ukoly):
        print("Invalid index!")
    else:
        deleted_task = ukoly.pop(index -1)
        print(f"Task {deleted_task["name"]} has been deleted.")
