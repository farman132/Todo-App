"""
Task model for the Advanced Intelligent Features of the Todo In-Memory Python Console App.

This module defines the Task data structure with ID, title, description, status,
priority, tags, due date, recurrence pattern, and next occurrence.
"""
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime, date


@dataclass
class Task:
    """
    Represents a single todo task with ID, title, description, status, priority, tags, due date,
    recurrence pattern, and next occurrence.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Title of the task
        description (str): Detailed description of the task
        status (str): Completion status of the task ('incomplete' or 'complete')
        priority (str): Priority level of the task ('high', 'medium', 'low')
        tags (List[str]): List of tags associated with the task
        due_date (Optional[str]): Due date of the task in ISO 8601 format (YYYY-MM-DD)
        created_at (str): Creation timestamp in ISO 8601 format (YYYY-MM-DDTHH:MM:SS)
        recurrence_pattern (Optional[str]): Recurrence pattern ('daily', 'weekly', 'monthly', None)
        next_occurrence (Optional[str]): Next occurrence date in ISO 8601 format (YYYY-MM-DD)
    """

    id: int
    title: str
    description: str
    status: str = "incomplete"
    priority: str = "medium"
    tags: List[str] = None
    due_date: Optional[str] = None
    created_at: str = None
    recurrence_pattern: Optional[str] = None
    next_occurrence: Optional[str] = None

    def __post_init__(self):
        """Validate the task after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Task ID must be a positive integer")

        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")

        if self.status not in ["incomplete", "complete"]:
            raise ValueError("Task status must be 'incomplete' or 'complete'")

        if self.priority not in ["high", "medium", "low"]:
            raise ValueError("Task priority must be 'high', 'medium', or 'low'")

        if self.tags is None:
            self.tags = []

        if self.recurrence_pattern is not None and self.recurrence_pattern not in ["daily", "weekly", "monthly"]:
            raise ValueError("Recurrence pattern must be 'daily', 'weekly', 'monthly', or None")

        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

        # Validate due date format if provided
        if self.due_date:
            try:
                datetime.strptime(self.due_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Due date must be in YYYY-MM-DD format")

        # Validate next occurrence format if provided
        if self.next_occurrence:
            try:
                datetime.strptime(self.next_occurrence, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Next occurrence must be in YYYY-MM-DD format")

    @property
    def status_indicator(self) -> str:
        """Return the status indicator for display (✔ for complete, ✖ for incomplete)."""
        return "✔" if self.status == "complete" else "✖"

    @property
    def priority_indicator(self) -> str:
        """Return the priority indicator for display."""
        if self.priority == "high":
            return "🔴"
        elif self.priority == "medium":
            return "🟡"
        else:  # low
            return "🟢"

    @property
    def is_overdue(self) -> bool:
        """Check if the task is overdue."""
        if not self.due_date or self.status == "complete":
            return False

        due_date_obj = datetime.strptime(self.due_date, "%Y-%m-%d").date()
        current_date = date.today()
        return due_date_obj < current_date

    @property
    def is_due_soon(self) -> bool:
        """Check if the task is due soon (within 3 days)."""
        if not self.due_date or self.status == "complete":
            return False

        due_date_obj = datetime.strptime(self.due_date, "%Y-%m-%d").date()
        current_date = date.today()
        days_until_due = (due_date_obj - current_date).days
        return 0 <= days_until_due <= 3

    @property
    def due_status(self) -> str:
        """Get the due status of the task."""
        if self.is_overdue:
            return "overdue"
        elif self.is_due_soon:
            return "due_soon"
        elif self.due_date:
            return "not_due"
        else:
            return "no_due_date"

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