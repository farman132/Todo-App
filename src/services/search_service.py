"""
Search and filter service for the Todo In-Memory Python Console App with Intermediate Level Features.

This module provides functionality for searching and filtering tasks.
"""
from typing import List, Optional
from ..models.task import Task
from ..lib.validators import validate_search_keyword


class SearchService:
    """
    Service class for searching and filtering tasks.

    This service provides methods for searching tasks by keyword and filtering by various criteria.
    """

    def __init__(self, task_service):
        """
        Initialize the search service with a task service reference.

        Args:
            task_service: The task service to search within
        """
        self.task_service = task_service

    def search_tasks_by_keyword(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in title or description.

        Args:
            keyword (str): The keyword to search for

        Returns:
            List[Task]: List of tasks that match the keyword
        """
        if not validate_search_keyword(keyword):
            return []

        keyword_lower = keyword.lower().strip()
        matching_tasks = []

        all_tasks = self.task_service.get_all_tasks()
        for task in all_tasks:
            # Check if keyword appears in title or description (case-insensitive)
            if keyword_lower in task.title.lower() or (task.description and keyword_lower in task.description.lower()):
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks_by_status(self, status: str) -> List[Task]:
        """
        Filter tasks by completion status.

        Args:
            status (str): The status to filter by ('complete' or 'incomplete')

        Returns:
            List[Task]: List of tasks with the specified status
        """
        if status not in ["complete", "incomplete"]:
            return []

        matching_tasks = []
        all_tasks = self.task_service.get_all_tasks()
        for task in all_tasks:
            if task.status == status:
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks_by_priority(self, priority: str) -> List[Task]:
        """
        Filter tasks by priority level.

        Args:
            priority (str): The priority to filter by ('high', 'medium', 'low')

        Returns:
            List[Task]: List of tasks with the specified priority
        """
        if priority not in ["high", "medium", "low"]:
            return []

        matching_tasks = []
        all_tasks = self.task_service.get_all_tasks()
        for task in all_tasks:
            if task.priority == priority:
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks_by_tag(self, tag: str) -> List[Task]:
        """
        Filter tasks by a specific tag.

        Args:
            tag (str): The tag to filter by

        Returns:
            List[Task]: List of tasks that have the specified tag
        """
        if not tag or not tag.strip():
            return []

        tag_lower = tag.lower().strip()
        matching_tasks = []
        all_tasks = self.task_service.get_all_tasks()
        for task in all_tasks:
            # Check if the tag exists in the task's tags (case-insensitive)
            for task_tag in task.tags:
                if tag_lower == task_tag.lower():
                    matching_tasks.append(task)
                    break  # Found the tag, no need to check other tags

        return matching_tasks

    def filter_tasks_by_due_date(self, due_date: str) -> List[Task]:
        """
        Filter tasks by due date.

        Args:
            due_date (str): The due date to filter by (YYYY-MM-DD format)

        Returns:
            List[Task]: List of tasks with the specified due date
        """
        from src.lib.validators import validate_due_date
        if not validate_due_date(due_date):
            return []

        matching_tasks = []
        all_tasks = self.task_service.get_all_tasks()
        for task in all_tasks:
            if task.due_date == due_date:
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks(self, status: Optional[str] = None, priority: Optional[str] = None,
                     tag: Optional[str] = None, due_date: Optional[str] = None) -> List[Task]:
        """
        Filter tasks by multiple criteria.

        Args:
            status (str, optional): Status to filter by
            priority (str, optional): Priority to filter by
            tag (str, optional): Tag to filter by
            due_date (str, optional): Due date to filter by

        Returns:
            List[Task]: List of tasks that match all specified criteria
        """
        matching_tasks = self.task_service.get_all_tasks()

        # Apply filters sequentially
        if status:
            matching_tasks = [task for task in matching_tasks if task.status == status]

        if priority:
            matching_tasks = [task for task in matching_tasks if task.priority == priority]

        if tag:
            matching_tasks = [task for task in matching_tasks if tag.lower() in [t.lower() for t in task.tags]]

        if due_date:
            matching_tasks = [task for task in matching_tasks if task.due_date == due_date]

        return matching_tasks