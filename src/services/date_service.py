"""
Date service for the Advanced Intelligent Features of the Todo In-Memory Python Console App.

This module provides functionality for managing due dates and detecting overdue tasks.
"""
from typing import List
from datetime import datetime, date
from ..models.task import Task


class DateService:
    """
    Service class for managing due dates and overdue status.

    This service provides methods for checking due dates, identifying overdue tasks,
    and calculating time-based status for tasks.
    """

    def __init__(self, task_service):
        """
        Initialize the date service with a task service reference.

        Args:
            task_service: The task service to use for task operations
        """
        self.task_service = task_service

    def get_overdue_tasks(self) -> List[Task]:
        """
        Get all overdue tasks.

        Returns:
            List[Task]: List of tasks that are overdue
        """
        all_tasks = self.task_service.get_all_tasks()
        return [task for task in all_tasks if task.is_overdue]

    def get_due_soon_tasks(self) -> List[Task]:
        """
        Get all tasks that are due soon (within 3 days).

        Returns:
            List[Task]: List of tasks that are due soon
        """
        all_tasks = self.task_service.get_all_tasks()
        return [task for task in all_tasks if task.is_due_soon and not task.is_overdue]

    def get_tasks_by_due_status(self, status: str) -> List[Task]:
        """
        Get tasks by due status.

        Args:
            status (str): The due status to filter by ('overdue', 'due_soon', 'not_due', 'no_due_date')

        Returns:
            List[Task]: List of tasks with the specified due status
        """
        all_tasks = self.task_service.get_all_tasks()
        return [task for task in all_tasks if task.due_status == status]

    def check_overdue_status(self, task: Task) -> bool:
        """
        Check if a task is overdue.

        Args:
            task (Task): The task to check

        Returns:
            bool: True if the task is overdue, False otherwise
        """
        return task.is_overdue

    def calculate_days_until_due(self, task: Task) -> int:
        """
        Calculate the number of days until the task is due.

        Args:
            task (Task): The task to calculate for

        Returns:
            int: Number of days until due (negative if overdue, positive if in future, 0 if due today)
        """
        if not task.due_date:
            return float('inf')  # No due date, so it's effectively never due

        due_date_obj = datetime.strptime(task.due_date, "%Y-%m-%d").date()
        current_date = date.today()
        days_difference = (due_date_obj - current_date).days

        return days_difference

    def get_upcoming_deadlines(self, days_ahead: int = 7) -> List[Task]:
        """
        Get tasks with due dates within the specified number of days.

        Args:
            days_ahead (int): Number of days ahead to check for due dates (default: 7)

        Returns:
            List[Task]: List of tasks due within the specified number of days
        """
        all_tasks = self.task_service.get_all_tasks()
        current_date = date.today()
        upcoming_tasks = []

        for task in all_tasks:
            if task.due_date and not task.is_overdue:
                due_date_obj = datetime.strptime(task.due_date, "%Y-%m-%d").date()
                days_until_due = (due_date_obj - current_date).days

                if 0 <= days_until_due <= days_ahead:
                    upcoming_tasks.append(task)

        return upcoming_tasks

    def validate_due_date_format(self, due_date: str) -> bool:
        """
        Validate that the due date is in the correct format.

        Args:
            due_date (str): The due date string to validate

        Returns:
            bool: True if valid, False otherwise
        """
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def get_due_date_summary(self) -> dict:
        """
        Get a summary of due date statistics.

        Returns:
            dict: Dictionary with counts of overdue, due soon, not due, and no due date tasks
        """
        all_tasks = self.task_service.get_all_tasks()

        overdue_count = 0
        due_soon_count = 0
        not_due_count = 0
        no_due_date_count = 0

        for task in all_tasks:
            if task.due_status == "overdue":
                overdue_count += 1
            elif task.due_status == "due_soon":
                due_soon_count += 1
            elif task.due_status == "not_due":
                not_due_count += 1
            else:  # no_due_date
                no_due_date_count += 1

        return {
            "overdue": overdue_count,
            "due_soon": due_soon_count,
            "not_due": not_due_count,
            "no_due_date": no_due_date_count,
            "total": len(all_tasks)
        }