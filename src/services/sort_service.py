"""
Sorting service for the Todo In-Memory Python Console App with Intermediate Level Features.

This module provides functionality for sorting tasks.
"""
from typing import List
from ..models.task import Task
from ..lib.validators import validate_sort_field, validate_sort_order
from datetime import datetime


class SortService:
    """
    Service class for sorting tasks.

    This service provides methods for sorting tasks by various criteria.
    """

    def __init__(self, task_service):
        """
        Initialize the sort service with a task service reference.

        Args:
            task_service: The task service to sort tasks from
        """
        self.task_service = task_service

    def sort_tasks_by_field(self, field: str, order: str = "asc") -> List[Task]:
        """
        Sort tasks by a specified field.

        Args:
            field (str): The field to sort by ('due_date', 'priority', 'title', 'created_at')
            order (str): The sort order ('asc' for ascending, 'desc' for descending)

        Returns:
            List[Task]: List of tasks sorted by the specified field and order
        """
        if not validate_sort_field(field):
            raise ValueError(f"Invalid sort field: {field}")

        if not validate_sort_order(order):
            raise ValueError(f"Invalid sort order: {order}")

        all_tasks = self.task_service.get_all_tasks()

        # Define sorting key based on field
        if field == "title":
            key_func = lambda task: task.title.lower()
        elif field == "priority":
            # Map priorities to numeric values for proper sorting (high, medium, low)
            priority_map = {"high": 0, "medium": 1, "low": 2}
            key_func = lambda task: priority_map[task.priority]
        elif field == "due_date":
            # Sort by due date, with None values last
            key_func = lambda task: (task.due_date is None, task.due_date)
        elif field == "created_at":
            key_func = lambda task: task.created_at
        else:
            # Default to title
            key_func = lambda task: task.title.lower()

        # Sort the tasks
        sorted_tasks = sorted(all_tasks, key=key_func, reverse=(order == "desc"))

        return sorted_tasks

    def sort_tasks_by_due_date(self, order: str = "asc") -> List[Task]:
        """
        Sort tasks by due date.

        Args:
            order (str): The sort order ('asc' for ascending, 'desc' for descending)

        Returns:
            List[Task]: List of tasks sorted by due date
        """
        return self.sort_tasks_by_field("due_date", order)

    def sort_tasks_by_priority(self, order: str = "asc") -> List[Task]:
        """
        Sort tasks by priority.

        Args:
            order (str): The sort order ('asc' for ascending, 'desc' for descending)

        Returns:
            List[Task]: List of tasks sorted by priority
        """
        return self.sort_tasks_by_field("priority", order)

    def sort_tasks_by_title(self, order: str = "asc") -> List[Task]:
        """
        Sort tasks alphabetically by title.

        Args:
            order (str): The sort order ('asc' for ascending, 'desc' for descending)

        Returns:
            List[Task]: List of tasks sorted by title
        """
        return self.sort_tasks_by_field("title", order)

    def sort_tasks_by_created_at(self, order: str = "asc") -> List[Task]:
        """
        Sort tasks by creation date.

        Args:
            order (str): The sort order ('asc' for ascending, 'desc' for descending)

        Returns:
            List[Task]: List of tasks sorted by creation date
        """
        return self.sort_tasks_by_field("created_at", order)