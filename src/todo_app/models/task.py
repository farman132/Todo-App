"""
Task model for the Todo In-Memory Python Console App.

This module defines the Task data structure with ID, title, description, and status.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo task with ID, title, description, and completion status.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Title of the task
        description (str): Detailed description of the task
        status (str): Completion status of the task ('incomplete' or 'complete')
    """

    id: int
    title: str
    description: str
    status: str = "incomplete"

    def __post_init__(self):
        """Validate the task after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")

        if self.status not in ["incomplete", "complete"]:
            raise ValueError("Task status must be 'incomplete' or 'complete'")

    @property
    def status_indicator(self) -> str:
        """Return the status indicator for display (✔ for complete, ✖ for incomplete)."""
        return "✔" if self.status == "complete" else "✖"

    def mark_complete(self):
        """Mark the task as complete."""
        self.status = "complete"

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.status = "incomplete"

    def toggle_status(self):
        """Toggle the task status between complete and incomplete."""
        if self.status == "complete":
            self.status = "incomplete"
        else:
            self.status = "complete"