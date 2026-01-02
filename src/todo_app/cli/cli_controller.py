"""
CLI controller for the Todo In-Memory Python Console App.

This module provides the command-line interface for interacting with tasks.
"""

from typing import Optional
from src.todo_app.services.task_service import TaskService


class CLIController:
    """
    Controller class for handling CLI interactions with tasks.

    This controller provides methods for adding, viewing, updating, deleting,
    and toggling the status of tasks through the command line interface.
    """

    def __init__(self, task_service: TaskService):
        """
        Initialize the CLI controller with a task service.

        Args:
            task_service (TaskService): The service to use for task operations
        """
        self.task_service = task_service

    def add_task(self) -> None:
        """
        Add a new task through CLI prompts.
        """
        print("\n--- Add New Task ---")
        try:
            title = input("Enter task title: ").strip()
            if not title:
                print("Error: Task title cannot be empty.")
                return

            description = input("Enter task description (optional): ").strip()

            task = self.task_service.add_task(title, description)
            print(f"Task added successfully! ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def view_all_tasks(self) -> None:
        """
        Display all tasks through CLI.
        """
        print("\n--- All Tasks ---")
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            status_indicator = task.status_indicator
            print(f"ID: {task.id} | {status_indicator} | {task.title}")
            if task.description:
                print(f"  Description: {task.description}")
            print()

    def update_task(self) -> None:
        """
        Update a task through CLI prompts.
        """
        print("\n--- Update Task ---")
        try:
            task_id_input = input("Enter task ID to update: ").strip()
            if not task_id_input.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_input)
            task = self.task_service.get_task_by_id(task_id)
            if task is None:
                print(f"Error: Task with ID {task_id} not found.")
                return

            print(f"Current task: {task.title}")
            if task.description:
                print(f"Current description: {task.description}")

            new_title = input("Enter new title (or press Enter to keep current): ").strip()
            new_description = input("Enter new description (or press Enter to keep current): ").strip()

            # Use None if user pressed Enter without typing anything, otherwise use the input
            title_update = new_title if new_title else None
            description_update = new_description if new_description else None

            # If user wants to keep the current value, don't update that field
            if title_update == "":
                title_update = task.title
            if description_update == "":
                description_update = task.description

            updated = self.task_service.update_task(
                task_id,
                title=title_update if title_update != task.title else None,
                description=description_update if description_update != task.description else None
            )

            if updated:
                print("Task updated successfully!")
            else:
                print("Failed to update task.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def delete_task(self) -> None:
        """
        Delete a task through CLI prompts.
        """
        print("\n--- Delete Task ---")
        try:
            task_id_input = input("Enter task ID to delete: ").strip()
            if not task_id_input.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_input)
            task = self.task_service.get_task_by_id(task_id)
            if task is None:
                print(f"Error: Task with ID {task_id} not found.")
                return

            confirm = input(f"Are you sure you want to delete task '{task.title}'? (y/N): ").strip().lower()
            if confirm in ['y', 'yes']:
                deleted = self.task_service.delete_task(task_id)
                if deleted:
                    print("Task deleted successfully!")
                else:
                    print("Failed to delete task.")
            else:
                print("Deletion cancelled.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def mark_task_status(self) -> None:
        """
        Toggle a task's completion status through CLI prompts.
        """
        print("\n--- Mark Task Status ---")
        try:
            task_id_input = input("Enter task ID to toggle status: ").strip()
            if not task_id_input.isdigit():
                print("Error: Task ID must be a number.")
                return

            task_id = int(task_id_input)
            task = self.task_service.get_task_by_id(task_id)
            if task is None:
                print(f"Error: Task with ID {task_id} not found.")
                return

            current_status = "Complete" if task.status == "complete" else "Incomplete"
            print(f"Current status for '{task.title}': {current_status}")

            toggled = self.task_service.toggle_task_status(task_id)
            if toggled:
                new_status = "Complete" if task.status == "complete" else "Incomplete"
                print(f"Task status updated to: {new_status}")
            else:
                print("Failed to update task status.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")