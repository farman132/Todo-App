"""
Main entry point for the Todo In-Memory Python Console App with Intermediate Level Features.

This module implements the main CLI menu loop that allows users to interact
with all task management features including priorities, tags, search, filter, and sort.
"""
import sys
import os
# Add the project root directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.services.task_service import TaskService
from src.services.search_service import SearchService
from src.services.sort_service import SortService
from src.services.recurrence_service import RecurrenceService
from src.services.date_service import DateService
from src.cli.cli_interface import CLIInterface


def main():
    """
    Main function that runs the CLI menu loop for the todo app with all features.
    """
    print("Welcome to the Todo In-Memory Python Console App with Advanced Intelligent Features!")
    print("Manage your tasks efficiently with priorities, tags, search, filter, sort, recurring tasks, and due date management.\n")

    # Initialize all services
    task_service = TaskService()
    search_service = SearchService(task_service)
    sort_service = SortService(task_service)
    recurrence_service = RecurrenceService(task_service)
    date_service = DateService(task_service)
    cli_interface = CLIInterface(task_service)

    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark task as complete/incomplete")
        print("6. Search tasks")
        print("7. Filter tasks")
        print("8. Sort tasks")
        print("9. Exit")
        print()

        try:
            choice = input("Please select an option (1-9): ").strip()

            if choice == "1":
                cli_interface.add_task()
            elif choice == "2":
                cli_interface.view_all_tasks()
            elif choice == "3":
                cli_interface.update_task()
            elif choice == "4":
                cli_interface.delete_task()
            elif choice == "5":
                cli_interface.mark_task_status()
            elif choice == "6":
                cli_interface.search_tasks()
            elif choice == "7":
                cli_interface.filter_tasks()
            elif choice == "8":
                cli_interface.sort_tasks()
            elif choice == "9":
                print("Thank you for using the Todo In-Memory Python Console App. Goodbye!")
                break
            else:
                print("Invalid option. Please select a number between 1 and 9.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Goodbye!")
            break
        except EOFError:
            print("\n\nGoodbye!")
            break


if __name__ == "__main__":
    main()