"""
Unit tests for the SortService with Intermediate Level Features.
"""
import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.services.task_service import TaskService
from src.services.sort_service import SortService


class TestSortService(unittest.TestCase):
    """
    Unit tests for SortService functionality.
    """

    def setUp(self):
        """
        Set up a fresh TaskService and SortService instance for each test.
        """
        self.task_service = TaskService()
        self.sort_service = SortService(self.task_service)

    def test_sort_by_title_ascending(self):
        """
        Test sorting tasks by title in ascending order.
        """
        # Add tasks in random order
        self.task_service.add_task("Zebra Task", "Description", "low")
        self.task_service.add_task("Alpha Task", "Description", "high")
        self.task_service.add_task("Mango Task", "Description", "medium")

        # Sort by title (ascending)
        sorted_tasks = self.sort_service.sort_tasks_by_field("title", "asc")
        titles = [task.title for task in sorted_tasks]

        self.assertEqual(titles, ["Alpha Task", "Mango Task", "Zebra Task"])

    def test_sort_by_title_descending(self):
        """
        Test sorting tasks by title in descending order.
        """
        # Add tasks in random order
        self.task_service.add_task("Alpha Task", "Description", "low")
        self.task_service.add_task("Mango Task", "Description", "high")
        self.task_service.add_task("Zebra Task", "Description", "medium")

        # Sort by title (descending)
        sorted_tasks = self.sort_service.sort_tasks_by_field("title", "desc")
        titles = [task.title for task in sorted_tasks]

        self.assertEqual(titles, ["Zebra Task", "Mango Task", "Alpha Task"])

    def test_sort_by_priority(self):
        """
        Test sorting tasks by priority.
        """
        # Add tasks with different priorities
        self.task_service.add_task("Low Priority", "Description", "low")
        self.task_service.add_task("High Priority", "Description", "high")
        self.task_service.add_task("Medium Priority", "Description", "medium")

        # Sort by priority (high to low)
        sorted_tasks = self.sort_service.sort_tasks_by_field("priority", "asc")
        priorities = [task.priority for task in sorted_tasks]

        # Ascending means high (0), medium (1), low (2) based on our sort mapping
        # So it should be high, medium, low
        self.assertEqual(priorities, ["high", "medium", "low"])

    def test_sort_by_priority_descending(self):
        """
        Test sorting tasks by priority in descending order.
        """
        # Add tasks with different priorities
        self.task_service.add_task("Low Priority", "Description", "low")
        self.task_service.add_task("High Priority", "Description", "high")
        self.task_service.add_task("Medium Priority", "Description", "medium")

        # Sort by priority (low to high)
        sorted_tasks = self.sort_service.sort_tasks_by_field("priority", "desc")
        priorities = [task.priority for task in sorted_tasks]

        # Descending means low, medium, high
        self.assertEqual(priorities, ["low", "medium", "high"])

    def test_sort_by_due_date(self):
        """
        Test sorting tasks by due date.
        """
        # Add tasks with different due dates
        self.task_service.add_task("Task 1", "Description", "medium", [], "2024-12-31")
        self.task_service.add_task("Task 2", "Description", "high", [], "2024-01-01")
        self.task_service.add_task("Task 3", "Description", "low", [], "2024-06-15")

        # Sort by due date (ascending)
        sorted_tasks = self.sort_service.sort_tasks_by_field("due_date", "asc")
        due_dates = [task.due_date for task in sorted_tasks]

        self.assertEqual(due_dates, ["2024-01-01", "2024-06-15", "2024-12-31"])


if __name__ == '__main__':
    unittest.main()