# TaskMaster CLI

A lightweight command-line tool to track daily tasks locally.

## Core Features Needed:
1. **Add a task:** e.g., `python task_cli.py add "Buy groceries"`
2. **List tasks:** e.g., `python task_cli.py list` (should show pending and completed tasks)
3. **Complete a task:** e.g., `python task_cli.py done 1` (marks task ID 1 as complete)

## Technical Requirements:
- The app must save data locally to a `tasks.json` file so tasks persist between commands.
- If `tasks.json` doesn't exist yet, the script should create it automatically.
