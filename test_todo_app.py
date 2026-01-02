"""
Test script to verify all functionality of the Todo In-Memory Python Console App.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.todo_app.services.task_service import TaskService
from src.todo_app.models.task import Task


def test_task_creation():
    """Test creating tasks with the TaskService."""
    print("Testing task creation...")
    service = TaskService()

    # Add a task
    task1 = service.add_task("Test Task 1", "This is a test task")
    assert task1.id == 1
    assert task1.title == "Test Task 1"
    assert task1.description == "This is a test task"
    assert task1.status == "incomplete"
    print("PASS: Task creation works")

    # Add another task
    task2 = service.add_task("Test Task 2")
    assert task2.id == 2
    assert task2.title == "Test Task 2"
    assert task2.description == ""
    print("PASS: Multiple task creation works")


def test_get_all_tasks():
    """Test retrieving all tasks."""
    print("Testing get all tasks...")
    service = TaskService()

    # Add some tasks
    service.add_task("Task 1", "Description 1")
    service.add_task("Task 2", "Description 2")

    tasks = service.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"
    print("PASS: Get all tasks works")


def test_get_task_by_id():
    """Test retrieving a task by ID."""
    print("Testing get task by ID...")
    service = TaskService()

    # Add a task
    task = service.add_task("Find Me", "Description")
    task_id = task.id

    # Retrieve by ID
    found_task = service.get_task_by_id(task_id)
    assert found_task is not None
    assert found_task.title == "Find Me"
    assert found_task.description == "Description"

    # Try to find non-existent task
    not_found = service.get_task_by_id(999)
    assert not_found is None
    print("PASS: Get task by ID works")


def test_update_task():
    """Test updating a task."""
    print("Testing update task...")
    service = TaskService()

    # Add a task
    task = service.add_task("Original Title", "Original Description")
    task_id = task.id

    # Update the task
    updated = service.update_task(task_id, "New Title", "New Description")
    assert updated is True

    # Verify the update
    updated_task = service.get_task_by_id(task_id)
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Description"

    # Test updating only title
    updated = service.update_task(task_id, title="Title Only")
    updated_task = service.get_task_by_id(task_id)
    assert updated_task.title == "Title Only"
    assert updated_task.description == "New Description"  # Should remain unchanged

    # Test updating only description
    updated = service.update_task(task_id, description="Desc Only")
    updated_task = service.get_task_by_id(task_id)
    assert updated_task.title == "Title Only"  # Should remain unchanged
    assert updated_task.description == "Desc Only"
    print("PASS: Update task works")


def test_delete_task():
    """Test deleting a task."""
    print("Testing delete task...")
    service = TaskService()

    # Add tasks
    task1 = service.add_task("Task 1", "Description 1")
    task2 = service.add_task("Task 2", "Description 2")

    # Verify both exist
    all_tasks = service.get_all_tasks()
    assert len(all_tasks) == 2

    # Delete one task
    deleted = service.delete_task(task1.id)
    assert deleted is True

    # Verify only one remains
    all_tasks = service.get_all_tasks()
    assert len(all_tasks) == 1

    # Try to delete non-existent task
    deleted = service.delete_task(999)
    assert deleted is False
    print("PASS: Delete task works")


def test_toggle_task_status():
    """Test toggling task status."""
    print("Testing toggle task status...")
    service = TaskService()

    # Add a task (should be incomplete by default)
    task = service.add_task("Status Test", "Testing status toggle")
    assert task.status == "incomplete"

    # Toggle to complete
    toggled = service.toggle_task_status(task.id)
    assert toggled is True
    assert task.status == "complete"

    # Toggle back to incomplete
    toggled = service.toggle_task_status(task.id)
    assert toggled is True
    assert task.status == "incomplete"

    # Try to toggle non-existent task
    toggled = service.toggle_task_status(999)
    assert toggled is False
    print("PASS: Toggle task status works")


def test_task_model():
    """Test the Task model."""
    print("Testing Task model...")

    # Create a task
    task = Task(1, "Test Title", "Test Description", "incomplete")
    assert task.id == 1
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.status == "incomplete"
    # Using regular characters instead of Unicode for Windows compatibility
    assert task.status_indicator == "✖" or task.status_indicator == "X"

    # Toggle status and check indicator
    task.toggle_status()
    assert task.status == "complete"
    # Using regular characters instead of Unicode for Windows compatibility
    assert task.status_indicator == "✔" or task.status_indicator == "O"

    # Test mark_complete and mark_incomplete
    task.mark_incomplete()
    assert task.status == "incomplete"
    task.mark_complete()
    assert task.status == "complete"
    print("PASS: Task model works")


def test_input_validation():
    """Test input validation."""
    print("Testing input validation...")
    service = TaskService()

    # Test empty title validation
    try:
        service.add_task("", "Description")
        assert False, "Should have raised ValueError for empty title"
    except ValueError:
        pass  # Expected

    try:
        service.add_task("   ", "Description")  # Only whitespace
        assert False, "Should have raised ValueError for whitespace-only title"
    except ValueError:
        pass  # Expected

    # Test update with empty title
    task = service.add_task("Valid Task", "Description")
    try:
        service.update_task(task.id, "")  # Empty title
        assert False, "Should have raised ValueError for empty title"
    except ValueError:
        pass  # Expected

    print("PASS: Input validation works")


def run_all_tests():
    """Run all tests."""
    print("Running all functionality tests for Todo App...\n")

    test_task_model()
    test_task_creation()
    test_get_all_tasks()
    test_get_task_by_id()
    test_update_task()
    test_delete_task()
    test_toggle_task_status()
    test_input_validation()

    print("\nPASS: All tests passed! The Todo In-Memory Python Console App is working correctly.")


if __name__ == "__main__":
    run_all_tests()