# Todo In-Memory Python Console App

A simple command-line todo application with in-memory storage, built with Python 3.13+.

## Features

- Add new tasks with title and description
- View all tasks with status indicators (✔ for complete, ✖ for incomplete)
- Update task details by ID
- Delete tasks by ID
- Mark tasks as complete/incomplete
- In-memory storage (no persistent storage)
- Clean, intuitive CLI interface

## Prerequisites

- Python 3.13 or higher

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Make sure you have Python 3.13+ installed

## Usage

To run the application:

```bash
python -m src.todo_app.main
```

## How to Use

1. The application will display a menu with options:
   - Add a new task
   - View all tasks
   - Update a task
   - Delete a task
   - Mark task as complete/incomplete
   - Exit

2. Follow the on-screen prompts to select an option
3. Enter required information when prompted
4. The application will provide feedback for each operation

## Example Workflow

1. Start the application
2. Select "Add a new task"
3. Enter a title and description for your task
4. Select "View all tasks" to see your task with status indicator
5. Use other options to manage your tasks as needed

## Architecture

The application follows a clean architecture pattern:

- **Models**: Task data structure
- **Services**: Business logic for task management
- **CLI**: Command-line interface components
- **Main**: Entry point and menu loop

## License

This project is licensed under the MIT License.