"""
Recurrence service for the Advanced Intelligent Features of the Todo In-Memory Python Console App.

This module provides functionality for managing recurring tasks.
"""
from typing import List, Optional
from datetime import datetime, timedelta
import calendar
from ..models.task import Task
from ..models.recurrence import Recurrence


class RecurrenceService:
    """
    Service class for managing recurring tasks.

    This service provides methods for creating, processing, and managing recurring tasks.
    """

    def __init__(self, task_service):
        """
        Initialize the recurrence service with a task service reference.

        Args:
            task_service: The task service to use for task operations
        """
        self.task_service = task_service

    def process_completed_recurring_task(self, task: Task) -> Optional[Task]:
        """
        Process a completed recurring task and create the next occurrence if applicable.

        Args:
            task (Task): The completed recurring task

        Returns:
            Optional[Task]: The new task instance created based on recurrence pattern, or None if not recurring
        """
        if not task.recurrence_pattern:
            return None

        # Calculate next occurrence date
        current_date = datetime.now().strftime("%Y-%m-%d")
        if task.next_occurrence:
            # If next_occurrence is already set, use that date
            next_occurrence_date = task.next_occurrence
        else:
            # Otherwise, calculate based on the recurrence pattern
            recurrence = Recurrence(task.recurrence_pattern, task.id)
            next_occurrence_date = recurrence.calculate_next_occurrence(current_date)

        # Create a new task based on the original task
        new_task = self.task_service.add_task(
            title=task.title,
            description=task.description,
            priority=task.priority,
            tags=task.tags.copy(),
            due_date=self._calculate_next_due_date(task, next_occurrence_date),
            recurrence_pattern=task.recurrence_pattern,
            next_occurrence=next_occurrence_date
        )

        return new_task

    def _calculate_next_due_date(self, original_task: Task, next_occurrence_date: str) -> Optional[str]:
        """
        Calculate the next due date based on the original task's due date pattern.

        Args:
            original_task (Task): The original task
            next_occurrence_date (str): The next occurrence date

        Returns:
            Optional[str]: The calculated next due date, or None if original task had no due date
        """
        if not original_task.due_date:
            return None

        # If the original task had a due date, calculate the new due date based on the recurrence pattern
        try:
            original_due_date = datetime.strptime(original_task.due_date, "%Y-%m-%d")

            # Calculate the next due date based on the recurrence pattern
            if original_task.recurrence_pattern == "daily":
                # For daily recurrence, add 1 day to the original due date
                next_due_date = original_due_date + timedelta(days=1)
            elif original_task.recurrence_pattern == "weekly":
                # For weekly recurrence, add 7 days to the original due date
                next_due_date = original_due_date + timedelta(weeks=1)
            elif original_task.recurrence_pattern == "monthly":
                # For monthly recurrence, add 1 month to the original due date
                # Calculate next month - handle month overflow
                year = original_due_date.year
                month = original_due_date.month + 1
                day = original_due_date.day

                # Handle year overflow
                if month > 12:
                    year += 1
                    month = 1

                # Handle day overflow for months with fewer days (e.g., Jan 31 -> Feb 28/29)
                try:
                    next_due_date = original_due_date.replace(year=year, month=month, day=day)
                except ValueError:
                    # If the day doesn't exist in the next month, use the last day of that month
                    import calendar
                    max_day = calendar.monthrange(year, month)[1]
                    next_due_date = original_due_date.replace(year=year, month=month, day=max_day)
            else:
                # If no recurrence pattern, just return the original due date
                next_due_date = original_due_date

            return next_due_date.strftime("%Y-%m-%d")
        except ValueError:
            # If calculation fails, return None
            return None

    def create_recurring_task(self, title: str, description: str = "", priority: str = "medium",
                              tags: List[str] = None, due_date: Optional[str] = None,
                              recurrence_pattern: str = None, next_occurrence: Optional[str] = None) -> Task:
        """
        Create a recurring task with the specified parameters.

        Args:
            title (str): Title of the task
            description (str): Description of the task
            priority (str): Priority level ('high', 'medium', 'low')
            tags (List[str]): List of tags associated with the task
            due_date (Optional[str]): Due date in YYYY-MM-DD format
            recurrence_pattern (str): Recurrence pattern ('daily', 'weekly', 'monthly')
            next_occurrence (Optional[str]): Next occurrence date in YYYY-MM-DD format

        Returns:
            Task: The created recurring task
        """
        if recurrence_pattern and next_occurrence is None:
            # Calculate next occurrence if not provided
            if recurrence_pattern == "daily":
                next_occurrence = self._add_days_to_date(datetime.now().strftime("%Y-%m-%d"), 1)
            elif recurrence_pattern == "weekly":
                next_occurrence = self._add_days_to_date(datetime.now().strftime("%Y-%m-%d"), 7)
            elif recurrence_pattern == "monthly":
                next_occurrence = self._add_months_to_date(datetime.now().strftime("%Y-%m-%d"), 1)

        return self.task_service.add_task(
            title=title,
            description=description,
            priority=priority,
            tags=tags or [],
            due_date=due_date,
            recurrence_pattern=recurrence_pattern,
            next_occurrence=next_occurrence
        )

    def _add_days_to_date(self, date_str: str, days: int) -> str:
        """
        Add days to a date string.

        Args:
            date_str (str): Date in YYYY-MM-DD format
            days (int): Number of days to add

        Returns:
            str: New date in YYYY-MM-DD format
        """
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        new_date = date_obj + timedelta(days=days)
        return new_date.strftime("%Y-%m-%d")

    def _add_months_to_date(self, date_str: str, months: int) -> str:
        """
        Add months to a date string, handling month/year overflow.

        Args:
            date_str (str): Date in YYYY-MM-DD format
            months (int): Number of months to add

        Returns:
            str: New date in YYYY-MM-DD format
        """
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        year = date_obj.year
        month = date_obj.month + months
        day = date_obj.day

        # Handle year overflow
        while month > 12:
            year += 1
            month -= 12

        # Handle day overflow for months with fewer days (e.g., Jan 31 -> Feb 28/29)
        try:
            new_date = date_obj.replace(year=year, month=month, day=day)
        except ValueError:
            # If the day doesn't exist in the target month, use the last day of that month
            max_day = calendar.monthrange(year, month)[1]
            new_date = date_obj.replace(year=year, month=month, day=max_day)

        return new_date.strftime("%Y-%m-%d")

    def get_recurring_tasks(self) -> List[Task]:
        """
        Get all recurring tasks.

        Returns:
            List[Task]: List of all recurring tasks
        """
        all_tasks = self.task_service.get_all_tasks()
        return [task for task in all_tasks if task.recurrence_pattern is not None]