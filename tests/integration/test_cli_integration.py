"""
Integration tests for CLI functionality combining multiple features.
"""
import unittest
from src.services.task_service import TaskService
from src.services.search_service import SearchService
from src.services.sort_service import SortService
from src.cli.cli_interface import CLIInterface


class TestCLIIntegration(unittest.TestCase):
    """
    Integration tests for CLI functionality combining multiple features.
    """

    def setUp(self):
        """
        Set up fresh services for each test.
        """
        self.task_service = TaskService()
        self.search_service = SearchService(self.task_service)
        self.sort_service = SortService(self.task_service)
        self.cli_interface = CLIInterface(self.task_service)

    def test_add_task_with_all_features(self):
        """
        Test adding a task with all new features (priority, tags, due date).
        """
        task = self.task_service.add_task(
            title="Integration Test Task",
            description="Test task with all features",
            priority="high",
            tags=["work", "important", "test"],
            due_date="2024-12-31"
        )

        self.assertEqual(task.title, "Integration Test Task")
        self.assertEqual(task.description, "Test task with all features")
        self.assertEqual(task.priority, "high")
        self.assertIn("work", task.tags)
        self.assertIn("important", task.tags)
        self.assertIn("test", task.tags)
        self.assertEqual(task.due_date, "2024-12-31")

    def test_search_filter_sort_combination(self):
        """
        Test combining search, filter, and sort functionality.
        """
        # Add tasks with various attributes
        self.task_service.add_task("Project A", "High priority project", "high", ["work", "urgent"], "2024-01-15")
        self.task_service.add_task("Project B", "Low priority project", "low", ["personal"], "2024-12-31")
        self.task_service.add_task("Project C", "Medium priority project", "medium", ["work"], "2024-06-30")
        self.task_service.add_task("Project D", "High priority project", "high", ["work", "important"], "2024-02-28")

        # Search for tasks containing "project"
        search_results = self.search_service.search_tasks_by_keyword("project")
        self.assertEqual(len(search_results), 4)

        # Filter high priority tasks
        high_priority_results = self.search_service.filter_tasks(priority="high")
        self.assertEqual(len(high_priority_results), 2)

        # Sort the high priority tasks by due date
        sorted_tasks = self.sort_service.sort_tasks_by_field("due_date", "asc")
        high_priority_sorted = [task for task in sorted_tasks if task.priority == "high"]

        # Verify the high priority tasks are sorted by due date
        expected_order = ["2024-01-15", "2024-02-28"]
        actual_order = [task.due_date for task in high_priority_sorted]
        self.assertEqual(actual_order, expected_order)

    def test_filter_by_multiple_criteria(self):
        """
        Test filtering by multiple criteria.
        """
        # Add tasks with various attributes
        self.task_service.add_task("Task 1", "Complete this", "high", ["work", "urgent"], "2024-01-15")
        self.task_service.add_task("Task 2", "Do this later", "low", ["personal"], "2024-12-31")
        self.task_service.add_task("Task 3", "Important work", "high", ["work"], "2024-06-30")
        self.task_service.add_task("Task 4", "Personal task", "medium", ["personal"], "2024-02-28")

        # Filter by high priority and work tag
        filtered_tasks = self.search_service.filter_tasks(
            priority="high",
            tag="work"
        )
        self.assertEqual(len(filtered_tasks), 2)

        # Verify all results match both criteria
        for task in filtered_tasks:
            self.assertEqual(task.priority, "high")
            self.assertIn("work", task.tags)

    def test_update_task_with_multiple_attributes(self):
        """
        Test updating multiple task attributes at once.
        """
        # Add a task
        original_task = self.task_service.add_task(
            title="Original Task",
            description="Original Description",
            priority="low",
            tags=["old", "tag"],
            due_date="2024-01-01"
        )
        task_id = original_task.id

        # Update multiple attributes
        success = self.task_service.update_task(
            task_id,
            title="Updated Task",
            description="Updated Description",
            priority="high",
            tags=["new", "tags"],
            due_date="2024-12-31"
        )
        self.assertTrue(success)

        # Verify all attributes were updated
        updated_task = self.task_service.get_task_by_id(task_id)
        self.assertEqual(updated_task.title, "Updated Task")
        self.assertEqual(updated_task.description, "Updated Description")
        self.assertEqual(updated_task.priority, "high")
        self.assertEqual(updated_task.tags, ["new", "tags"])
        self.assertEqual(updated_task.due_date, "2024-12-31")


if __name__ == '__main__':
    unittest.main()