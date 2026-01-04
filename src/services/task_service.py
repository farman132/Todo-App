"""
Task service for the Todo In-Memory Python Console App with Intermediate Level Features.

This module provides business logic for managing tasks in memory with priorities and tags.
"""
from typing import List, Optional
from src.models.task import Task


class TaskService:
    """
    Service class for managing tasks in memory with priorities and tags.

    This service provides methods for adding, retrieving, updating, deleting,
    and toggling the status of tasks with additional priority and tag functionality.
    """

    def __init__(self):
        """Initialize the task service with an empty in-memory storage."""
        self._tasks: List[Task] = []
        self._next_id = 1

    def _generate_next_id(self) -> int:
        """Generate the next unique ID for a task."""
        while any(task.id == self._next_id for task in self._tasks):
            self._next_id += 1
        return self._next_id

    def add_task(self, title: str, description: str = "", priority: str = "medium", tags: List[str] = None,
                 due_date: Optional[str] = None, recurrence_pattern: Optional[str] = None,
                 next_occurrence: Optional[str] = None) -> Task:
        """
        Add a new task to the in-memory storage.

        Args:
            title (str): Title of the task
            description (str): Description of the task
            priority (str): Priority level ('high', 'medium', 'low')
            tags (List[str]): List of tags associated with the task
            due_date (Optional[str]): Due date in YYYY-MM-DD format
            recurrence_pattern (Optional[str]): Recurrence pattern ('daily', 'weekly', 'monthly', None)
            next_occurrence (Optional[str]): Next occurrence date in YYYY-MM-DD format

        Returns:
            Task: The created task with a unique ID

        Raises:
            ValueError: If title is empty or invalid
        """
        # Validate inputs
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        if priority not in ["high", "medium", "low"]:
            raise ValueError("Priority must be 'high', 'medium', or 'low'")

        if recurrence_pattern is not None and recurrence_pattern not in ["daily", "weekly", "monthly"]:
            raise ValueError("Recurrence pattern must be 'daily', 'weekly', 'monthly', or None")

        if tags is None:
            tags = []

        # Create a new task with a unique ID
        task_id = self._generate_next_id()
        task = Task(
            id=task_id,
            title=title.strip(),
            description=description.strip(),
            priority=priority,
            tags=tags.copy(),
            due_date=due_date,
            recurrence_pattern=recurrence_pattern,
            next_occurrence=next_occurrence
        )
        self._tasks.append(task)

        # Increment the next ID counter
        self._next_id = task_id + 1

        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks from in-memory storage.

        Returns:
            List[Task]: List of all tasks
        """
        return self._tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID from in-memory storage.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Task: The task with the given ID, or None if not found
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                    priority: Optional[str] = None, tags: Optional[List[str]] = None,
                    due_date: Optional[str] = None, recurrence_pattern: Optional[str] = None,
                    next_occurrence: Optional[str] = None) -> bool:
        """
        Update a task's title, description, priority, tags, due date, recurrence pattern, or next occurrence by its ID.

        Args:
            task_id (int): ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task
            priority (str, optional): New priority for the task
            tags (List[str], optional): New tags for the task
            due_date (str, optional): New due date for the task
            recurrence_pattern (str, optional): New recurrence pattern for the task
            next_occurrence (str, optional): New next occurrence date for the task

        Returns:
            bool: True if the task was updated, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        if title is not None:
            if not title or not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()

        if description is not None:
            task.description = description.strip()

        if priority is not None:
            if priority not in ["high", "medium", "low"]:
                raise ValueError("Priority must be 'high', 'medium', or 'low'")
            task.priority = priority

        if tags is not None:
            task.tags = tags.copy()

        if due_date is not None:
            task.due_date = due_date

        if recurrence_pattern is not None:
            if recurrence_pattern not in ["daily", "weekly", "monthly"]:
                raise ValueError("Recurrence pattern must be 'daily', 'weekly', 'monthly', or None")
            task.recurrence_pattern = recurrence_pattern

        if next_occurrence is not None:
            task.next_occurrence = next_occurrence

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID from in-memory storage.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        self._tasks.remove(task)
        return True

    def toggle_task_status(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task by its ID.
        If the task is recurring and being marked complete, process the recurring task logic.

        Args:
            task_id (int): ID of the task to toggle

        Returns:
            bool: True if the task status was toggled, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        # Check if the task is being marked as complete
        is_becoming_complete = (task.status == "incomplete")

        # Toggle the status
        task.toggle_status()

        # If the task is recurring and is being marked complete, process the recurrence
        if is_becoming_complete and task.recurrence_pattern:
            # Create a new task based on the recurrence pattern
            from ..services.recurrence_service import RecurrenceService
            # For now, we'll just create the recurrence service to handle this
            # In a real implementation, we'd call the service to create the next instance
            recurrence_service = RecurrenceService(self)
            recurrence_service.process_completed_recurring_task(task)

        return True

    def get_next_id(self) -> int:
        """
        Get the next available ID without adding a task.

        Returns:
            int: The next available task ID
        """
        return self._generate_next_id()