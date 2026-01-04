"""
CLI interface for the Todo In-Memory Python Console App with Intermediate Level Features.

This module provides the command-line interface for interacting with tasks.
"""
from typing import Optional
from src.services.task_service import TaskService


class CLIInterface:
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

            # Get priority
            priority = input("Enter priority (high/medium/low, default: medium): ").strip().lower()
            if priority not in ["high", "medium", "low", ""]:
                print("Error: Priority must be 'high', 'medium', or 'low'. Using default 'medium'.")
                priority = "medium"
            elif priority == "":
                priority = "medium"

            # Get tags
            tags_input = input("Enter tags (comma-separated, optional): ").strip()
            tags = []
            if tags_input:
                tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
                # Validate tags
                from src.lib.validators import validate_tags
                if not validate_tags(tags):
                    print("Warning: Some tags have invalid format. Tags should be 1-50 characters with only alphanumeric, hyphens, and underscores.")
                    # Continue anyway but warn user

            # Get due date
            due_date = input("Enter due date (YYYY-MM-DD, optional): ").strip()
            if due_date == "":
                due_date = None
            elif due_date:
                from src.lib.validators import validate_due_date
                if not validate_due_date(due_date):
                    print("Warning: Invalid date format. Please use YYYY-MM-DD format.")
                    due_date = None

            # Get recurrence pattern
            recurrence_pattern = input("Enter recurrence pattern (daily/weekly/monthly, optional): ").strip().lower()
            if recurrence_pattern == "":
                recurrence_pattern = None
            elif recurrence_pattern not in ["daily", "weekly", "monthly"]:
                print("Warning: Invalid recurrence pattern. Please use 'daily', 'weekly', or 'monthly'.")
                recurrence_pattern = None

            # Get next occurrence if recurrence is set
            next_occurrence = None
            if recurrence_pattern:
                next_occurrence_input = input("Enter next occurrence date (YYYY-MM-DD, optional, defaults to tomorrow): ").strip()
                if next_occurrence_input == "":
                    from datetime import datetime, timedelta
                    next_occurrence = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
                elif next_occurrence_input:
                    from src.lib.validators import validate_due_date
                    if validate_due_date(next_occurrence_input):
                        next_occurrence = next_occurrence_input
                    else:
                        print("Warning: Invalid date format. Using default (tomorrow).")
                        from datetime import datetime, timedelta
                        next_occurrence = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

            task = self.task_service.add_task(title, description, priority, tags, due_date, recurrence_pattern, next_occurrence)
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
            priority_indicator = task.priority_indicator
            print(f"ID: {task.id} | {status_indicator} | {priority_indicator} | {task.priority.upper()} | {task.title}")
            if task.description:
                print(f"  Description: {task.description}")

            if task.tags:
                print(f"  Tags: {', '.join(task.tags)}")

            if task.due_date:
                print(f"  Due Date: {task.due_date}")
                if task.is_overdue:
                    print(f"  Status: OVERDUE!")
                elif task.is_due_soon:
                    print(f"  Status: DUE SOON!")

            if task.recurrence_pattern:
                print(f"  Recurrence: {task.recurrence_pattern}")
                if task.next_occurrence:
                    print(f"  Next Occurrence: {task.next_occurrence}")

            print(f"  Created: {task.created_at}")
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
            print(f"Current priority: {task.priority}")
            if task.tags:
                print(f"Current tags: {', '.join(task.tags)}")
            if task.due_date:
                print(f"Current due date: {task.due_date}")

            new_title = input("Enter new title (or press Enter to keep current): ").strip()
            new_description = input("Enter new description (or press Enter to keep current): ").strip()

            # Get new priority
            new_priority = input("Enter new priority (high/medium/low, or press Enter to keep current): ").strip().lower()
            if new_priority and new_priority not in ["high", "medium", "low"]:
                print("Error: Priority must be 'high', 'medium', or 'low'. Keeping current priority.")
                new_priority = None

            # Get new tags
            new_tags_input = input("Enter new tags (comma-separated, or press Enter to keep current): ").strip()
            new_tags = None
            if new_tags_input:
                new_tags = [tag.strip() for tag in new_tags_input.split(",") if tag.strip()]
            elif new_tags_input == "":
                new_tags = []  # Empty list to clear tags

            # Get new due date
            new_due_date = input("Enter new due date (YYYY-MM-DD, or press Enter to keep current): ").strip()
            if new_due_date == "":
                new_due_date = None  # Keep current due date

            # Get new recurrence pattern
            new_recurrence_input = input("Enter new recurrence pattern (daily/weekly/monthly, or press Enter to keep current): ").strip().lower()
            new_recurrence_pattern = None
            if new_recurrence_input:
                if new_recurrence_input in ["daily", "weekly", "monthly"]:
                    new_recurrence_pattern = new_recurrence_input
                elif new_recurrence_input in ["none", "clear", "remove"]:
                    new_recurrence_pattern = None  # Clear the recurrence
                else:
                    print("Invalid recurrence pattern. Valid options are 'daily', 'weekly', 'monthly', 'none', 'clear', 'remove'. Keeping current value.")
                    new_recurrence_pattern = None  # Don't update if invalid

            # Get new next occurrence
            new_next_occurrence = None
            if new_recurrence_pattern:
                new_occurrence_input = input("Enter new next occurrence date (YYYY-MM-DD, or press Enter to keep current): ").strip()
                if new_occurrence_input:
                    from src.lib.validators import validate_due_date
                    if validate_due_date(new_occurrence_input):
                        new_next_occurrence = new_occurrence_input
                    else:
                        print("Invalid date format. Keeping current value.")
                        new_next_occurrence = None  # Don't update if invalid
                elif new_occurrence_input == "":
                    new_next_occurrence = None  # Keep current value

            # Prepare update parameters
            title_update = new_title if new_title else None
            description_update = new_description if new_description else None
            priority_update = new_priority if new_priority else None
            tags_update = new_tags if new_tags is not None else None
            due_date_update = new_due_date if new_due_date else None
            recurrence_pattern_update = new_recurrence_pattern
            next_occurrence_update = new_next_occurrence

            updated = self.task_service.update_task(
                task_id,
                title=title_update,
                description=description_update,
                priority=priority_update,
                tags=tags_update,
                due_date=due_date_update,
                recurrence_pattern=recurrence_pattern_update,
                next_occurrence=next_occurrence_update
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

    def search_tasks(self) -> None:
        """
        Search tasks by keyword through CLI prompts.
        """
        print("\n--- Search Tasks ---")
        try:
            keyword = input("Enter keyword to search (in title or description): ").strip()

            if not keyword:
                print("Error: Search keyword cannot be empty.")
                return

            # Import SearchService here to avoid circular imports
            from src.services.search_service import SearchService
            search_service = SearchService(self.task_service)

            matching_tasks = search_service.search_tasks_by_keyword(keyword)

            if not matching_tasks:
                print("No tasks found matching your search.")
                return

            print(f"\n--- Search Results for '{keyword}' ---")
            for task in matching_tasks:
                status_indicator = task.status_indicator
                priority_indicator = task.priority_indicator
                print(f"ID: {task.id} | {status_indicator} | {priority_indicator} | {task.priority.upper()} | {task.title}")
                if task.description:
                    print(f"  Description: {task.description}")

                if task.tags:
                    print(f"  Tags: {', '.join(task.tags)}")

                if task.due_date:
                    print(f"  Due Date: {task.due_date}")

                print(f"  Created: {task.created_at}")
                print()
        except Exception as e:
            print(f"An unexpected error occurred during search: {e}")

    def filter_tasks(self) -> None:
        """
        Filter tasks by various criteria through CLI prompts.
        """
        print("\n--- Filter Tasks ---")
        try:
            print("Select filter criteria (press Enter to skip a filter):")

            status = input("Filter by status (complete/incomplete): ").strip().lower()
            if status and status not in ["complete", "incomplete"]:
                print("Invalid status. Valid options are 'complete' or 'incomplete'.")
                return

            priority = input("Filter by priority (high/medium/low): ").strip().lower()
            if priority and priority not in ["high", "medium", "low"]:
                print("Invalid priority. Valid options are 'high', 'medium', or 'low'.")
                return

            tag = input("Filter by tag: ").strip()

            due_date = input("Filter by due date (YYYY-MM-DD): ").strip()
            if due_date:
                from src.lib.validators import validate_due_date
                if not validate_due_date(due_date):
                    print("Invalid date format. Please use YYYY-MM-DD format.")
                    return

            # Import SearchService here to avoid circular imports
            from src.services.search_service import SearchService
            search_service = SearchService(self.task_service)

            matching_tasks = search_service.filter_tasks(
                status=status if status else None,
                priority=priority if priority else None,
                tag=tag if tag else None,
                due_date=due_date if due_date else None
            )

            if not matching_tasks:
                print("No tasks found matching your filter criteria.")
                return

            print("\n--- Filter Results ---")
            for task in matching_tasks:
                status_indicator = task.status_indicator
                priority_indicator = task.priority_indicator
                print(f"ID: {task.id} | {status_indicator} | {priority_indicator} | {task.priority.upper()} | {task.title}")
                if task.description:
                    print(f"  Description: {task.description}")

                if task.tags:
                    print(f"  Tags: {', '.join(task.tags)}")

                if task.due_date:
                    print(f"  Due Date: {task.due_date}")

                print(f"  Created: {task.created_at}")
                print()
        except Exception as e:
            print(f"An unexpected error occurred during filtering: {e}")

    def sort_tasks(self) -> None:
        """
        Sort tasks by various criteria through CLI prompts.
        """
        print("\n--- Sort Tasks ---")
        try:
            print("Select sort field:")
            print("1. Title (alphabetically)")
            print("2. Priority (high to low)")
            print("3. Due Date")
            print("4. Creation Date")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                field = "title"
                field_name = "Title"
            elif choice == "2":
                field = "priority"
                field_name = "Priority"
            elif choice == "3":
                field = "due_date"
                field_name = "Due Date"
            elif choice == "4":
                field = "created_at"
                field_name = "Creation Date"
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
                return

            order_input = input("Sort order (asc/desc, default: asc): ").strip().lower()
            if order_input in ["", "asc", "ascending"]:
                order = "asc"
            elif order_input in ["desc", "descending"]:
                order = "desc"
            else:
                print("Invalid sort order. Using ascending order.")
                order = "asc"

            # Import SortService here to avoid circular imports
            from src.services.sort_service import SortService
            sort_service = SortService(self.task_service)

            sorted_tasks = sort_service.sort_tasks_by_field(field, order)

            if not sorted_tasks:
                print("No tasks to sort.")
                return

            print(f"\n--- Tasks Sorted by {field_name} ({'Ascending' if order == 'asc' else 'Descending'}) ---")
            for task in sorted_tasks:
                status_indicator = task.status_indicator
                priority_indicator = task.priority_indicator
                print(f"ID: {task.id} | {status_indicator} | {priority_indicator} | {task.priority.upper()} | {task.title}")
                if task.description:
                    print(f"  Description: {task.description}")

                if task.tags:
                    print(f"  Tags: {', '.join(task.tags)}")

                if task.due_date:
                    print(f"  Due Date: {task.due_date}")

                print(f"  Created: {task.created_at}")
                print()
        except Exception as e:
            print(f"An unexpected error occurred during sorting: {e}")