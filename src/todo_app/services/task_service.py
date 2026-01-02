"""
Task service for the Todo In-Memory Python Console App.

This module provides business logic for managing tasks in memory.
"""

from typing import List, Optional
from src.todo_app.models.task import Task


class TaskService:
    """
    Service class for managing tasks in memory.

    This service provides methods for adding, retrieving, updating, deleting,
    and toggling the status of tasks.
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

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the in-memory storage.

        Args:
            title (str): Title of the task
            description (str): Description of the task

        Returns:
            Task: The created task with a unique ID

        Raises:
            ValueError: If title is empty or invalid
        """
        # Validate inputs
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        # Create a new task with a unique ID
        task_id = self._generate_next_id()
        task = Task(id=task_id, title=title.strip(), description=description.strip())
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

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update a task's title or description by its ID.

        Args:
            task_id (int): ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task

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

        Args:
            task_id (int): ID of the task to toggle

        Returns:
            bool: True if the task status was toggled, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False

        task.toggle_status()
        return True

    def get_next_id(self) -> int:
        """
        Get the next available ID without adding a task.

        Returns:
            int: The next available task ID
        """
        return self._generate_next_id()