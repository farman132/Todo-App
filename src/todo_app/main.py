"""
Main entry point for the Todo In-Memory Python Console App.

This module implements the main CLI menu loop that allows users to interact
with the task management system.
"""

from src.todo_app.services.task_service import TaskService
from src.todo_app.cli.cli_controller import CLIController


def main():
    """
    Main function that runs the CLI menu loop for the todo app.
    """
    print("Welcome to the Todo In-Memory Python Console App!")
    print("Manage your tasks efficiently with this simple CLI tool.\n")

    # Initialize the task service and CLI controller
    task_service = TaskService()
    cli_controller = CLIController(task_service)

    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as complete/incomplete")
        print("6. Exit")
        print()

        try:
            choice = input("Please select an option (1-6): ").strip()

            if choice == "1":
                cli_controller.add_task()
            elif choice == "2":
                cli_controller.view_all_tasks()
            elif choice == "3":
                cli_controller.update_task()
            elif choice == "4":
                cli_controller.delete_task()
            elif choice == "5":
                cli_controller.mark_task_status()
            elif choice == "6":
                print("Thank you for using the Todo In-Memory Python Console App. Goodbye!")
                break
            else:
                print("Invalid option. Please select a number between 1 and 6.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Goodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()