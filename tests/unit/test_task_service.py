"""
Unit tests for the TaskService with Intermediate Level Features.
"""
import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.models.task import Task
from src.services.task_service import TaskService


class TestTaskService(unittest.TestCase):
    """
    Unit tests for TaskService functionality.
    """

    def setUp(self):
        """
        Set up a fresh TaskService instance for each test.
        """
        self.task_service = TaskService()

    def test_add_task_with_priority_and_tags(self):
        """
        Test adding a task with priority and tags.
        """
        task = self.task_service.add_task(
            title="Test Task",
            description="Test Description",
            priority="high",
            tags=["work", "urgent"]
        )

        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.priority, "high")
        self.assertEqual(task.tags, ["work", "urgent"])

    def test_update_task_priority_and_tags(self):
        """
        Test updating task priority and tags.
        """
        task = self.task_service.add_task("Test Task")
        task_id = task.id

        # Update priority and tags
        success = self.task_service.update_task(
            task_id,
            priority="low",
            tags=["personal"]
        )

        self.assertTrue(success)
        updated_task = self.task_service.get_task_by_id(task_id)
        self.assertEqual(updated_task.priority, "low")
        self.assertEqual(updated_task.tags, ["personal"])

    def test_get_all_tasks(self):
        """
        Test retrieving all tasks.
        """
        # Add multiple tasks
        self.task_service.add_task("Task 1")
        self.task_service.add_task("Task 2")

        tasks = self.task_service.get_all_tasks()
        self.assertEqual(len(tasks), 2)

    def test_delete_task(self):
        """
        Test deleting a task.
        """
        task = self.task_service.add_task("Test Task")
        task_id = task.id

        # Verify task exists
        self.assertIsNotNone(self.task_service.get_task_by_id(task_id))

        # Delete the task
        success = self.task_service.delete_task(task_id)
        self.assertTrue(success)

        # Verify task no longer exists
        self.assertIsNone(self.task_service.get_task_by_id(task_id))

    def test_toggle_task_status(self):
        """
        Test toggling task status.
        """
        task = self.task_service.add_task("Test Task")
        task_id = task.id

        # Initial status should be incomplete
        self.assertEqual(task.status, "incomplete")

        # Toggle status
        success = self.task_service.toggle_task_status(task_id)
        self.assertTrue(success)

        # Status should now be complete
        toggled_task = self.task_service.get_task_by_id(task_id)
        self.assertEqual(toggled_task.status, "complete")


if __name__ == '__main__':
    unittest.main()