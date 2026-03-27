import json
import sys
import argparse

tasks = []
tasks_file = 'tasks.json'

def load_tasks():
    try:
        with open(tasks_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks():
    with open(tasks_file, 'w') as file:
        json.dump(tasks, file)

def add_task(task):
    tasks.append({'task': task, 'done': False})
    save_tasks()

def list_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task['done'] else "Pending"
        print(f"{i}. {task['task']} - {status}")

def complete_task(task_id):
    try:
        task_id = int(task_id) - 1
        if task_id < 0:
            print("Invalid task ID")
            return
        tasks[task_id]['done'] = True
        save_tasks()
    except IndexError:
        print("Task not found")

def delete_task(task_id):
    try:
        task_id = int(task_id) - 1
        if task_id < 0:
            print("Invalid task ID")
            return
        del tasks[task_id]
        save_tasks()
    except IndexError:
        print("Task not found")

def clear_tasks():
    confirm = input("Are you sure you want to clear all tasks? (y/n): ")
    if confirm.lower() == 'y':
        global tasks
        tasks = []
        save_tasks()
        print("All tasks cleared")
    else:
        print("Clearing tasks cancelled")

def main():
    parser = argparse.ArgumentParser(description='TaskMaster CLI')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('task', help='Task description')

    list_parser = subparsers.add_parser('list', help='List all tasks')

    done_parser = subparsers.add_parser('done', help='Mark a task as done')
    done_parser.add_argument('task_id', help='ID of the task to mark as done', type=int)

    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('task_id', help='ID of the task to delete', type=int)

    clear_parser = subparsers.add_parser('clear', help='Clear all tasks')

    args = parser.parse_args()
    global tasks
    tasks = load_tasks()

    if args.command == 'add':
        add_task(args.task)
    elif args.command == 'list':
        list_tasks()
    elif args.command == 'done':
        complete_task(args.task_id)
    elif args.command == 'delete':
        delete_task(args.task_id)
    elif args.command == 'clear':
        clear_tasks()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
