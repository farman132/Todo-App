"""
Unit tests for the SearchService with Intermediate Level Features.
"""
import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.task_service import TaskService
from src.services.search_service import SearchService


class TestSearchService(unittest.TestCase):
    """
    Unit tests for SearchService functionality.
    """

    def setUp(self):
        """
        Set up a fresh TaskService and SearchService instance for each test.
        """
        self.task_service = TaskService()
        self.search_service = SearchService(self.task_service)

    def test_search_by_keyword_in_title(self):
        """
        Test searching for tasks by keyword in title.
        """
        # Add tasks
        self.task_service.add_task("Complete project", "Finish the project", "high", ["work"])
        self.task_service.add_task("Buy groceries", "Milk and bread", "medium", ["personal"])

        # Search for "project"
        results = self.search_service.search_tasks_by_keyword("project")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Complete project")

    def test_search_by_keyword_in_description(self):
        """
        Test searching for tasks by keyword in description.
        """
        # Add tasks
        self.task_service.add_task("Task 1", "This is important", "high", ["work"])
        self.task_service.add_task("Task 2", "This is not important", "low", ["personal"])

        # Search for "important"
        results = self.search_service.search_tasks_by_keyword("important")
        self.assertEqual(len(results), 2)

    def test_filter_by_status(self):
        """
        Test filtering tasks by status.
        """
        # Add tasks
        task1 = self.task_service.add_task("Task 1", "Description", "high", ["work"])
        task2 = self.task_service.add_task("Task 2", "Description", "low", ["personal"])
        self.task_service.toggle_task_status(task1.id)  # Mark task1 as complete

        # Filter by complete status
        results = self.search_service.filter_tasks_by_status("complete")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, task1.id)

    def test_filter_by_priority(self):
        """
        Test filtering tasks by priority.
        """
        # Add tasks
        self.task_service.add_task("Task 1", "Description", "high", ["work"])
        self.task_service.add_task("Task 2", "Description", "low", ["personal"])
        self.task_service.add_task("Task 3", "Description", "high", ["urgent"])

        # Filter by high priority
        results = self.search_service.filter_tasks_by_priority("high")
        self.assertEqual(len(results), 2)

    def test_filter_by_tag(self):
        """
        Test filtering tasks by tag.
        """
        # Add tasks
        self.task_service.add_task("Task 1", "Description", "high", ["work", "urgent"])
        self.task_service.add_task("Task 2", "Description", "low", ["personal"])
        self.task_service.add_task("Task 3", "Description", "medium", ["work"])

        # Filter by "work" tag
        results = self.search_service.filter_tasks_by_tag("work")
        self.assertEqual(len(results), 2)

    def test_filter_by_multiple_criteria(self):
        """
        Test filtering tasks by multiple criteria.
        """
        # Add tasks
        self.task_service.add_task("Task 1", "Description", "high", ["work"])
        self.task_service.add_task("Task 2", "Important task", "high", ["work"])
        self.task_service.add_task("Task 3", "Description", "low", ["personal"])

        # Filter by high priority
        results = self.search_service.filter_tasks(priority="high")
        self.assertEqual(len(results), 2)

        # Filter by work tag
        results = self.search_service.filter_tasks(tag="work")
        self.assertEqual(len(results), 2)

        # Filter by both high priority and work tag
        results = self.search_service.filter_tasks(priority="high", tag="work")
        self.assertEqual(len(results), 2)


if __name__ == '__main__':
    unittest.main()