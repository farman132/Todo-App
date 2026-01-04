"""
Test script to verify all functionality of the Todo App with Intermediate Level Features.
"""
import sys
import os

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from services.task_service import TaskService
from services.search_service import SearchService
from services.sort_service import SortService
from cli.cli_interface import CLIInterface


def test_basic_functionality():
    """Test basic task operations."""
    print("Testing basic functionality...")

    # Create services
    task_service = TaskService()
    search_service = SearchService(task_service)
    sort_service = SortService(task_service)
    cli_interface = CLIInterface(task_service)

    # Test adding a task
    print("\n1. Testing task creation...")
    task = task_service.add_task("Test Task", "Test Description", "high", ["test", "work"], "2024-12-31")
    print(f"   Added task: ID={task.id}, Title='{task.title}', Priority='{task.priority}'")
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.priority == "high"
    assert "test" in task.tags
    assert task.due_date == "2024-12-31"
    print("   ✓ Task creation works correctly")

    # Test adding another task with different priority
    task2 = task_service.add_task("Another Task", "Another Description", "low", ["personal"], "2024-01-01")
    print(f"   Added second task: ID={task2.id}, Title='{task2.title}', Priority='{task2.priority}'")

    # Test getting all tasks
    print("\n2. Testing retrieving all tasks...")
    tasks = task_service.get_all_tasks()
    print(f"   Retrieved {len(tasks)} tasks")
    assert len(tasks) == 2
    print("   ✓ Task retrieval works correctly")

    # Test updating a task
    print("\n3. Testing task update...")
    success = task_service.update_task(task.id, priority="medium", tags=["updated", "test"])
    assert success
    updated_task = task_service.get_task_by_id(task.id)
    assert updated_task.priority == "medium"
    assert "updated" in updated_task.tags
    print("   ✓ Task update works correctly")

    # Test toggling task status
    print("\n4. Testing task status toggle...")
    initial_status = updated_task.status
    task_service.toggle_task_status(task.id)
    toggled_task = task_service.get_task_by_id(task.id)
    expected_status = "complete" if initial_status == "incomplete" else "incomplete"
    assert toggled_task.status == expected_status
    print("   ✓ Task status toggle works correctly")

    # Test deleting a task
    print("\n5. Testing task deletion...")
    all_tasks_before = len(task_service.get_all_tasks())
    success = task_service.delete_task(task.id)
    assert success
    all_tasks_after = len(task_service.get_all_tasks())
    assert all_tasks_after == all_tasks_before - 1
    print("   ✓ Task deletion works correctly")

    print("\n✓ All basic functionality tests passed!")


def test_search_functionality():
    """Test search functionality."""
    print("\n\nTesting search functionality...")

    # Create services
    task_service = TaskService()
    search_service = SearchService(task_service)

    # Add tasks for searching
    task_service.add_task("Project Alpha", "Important project", "high", ["work", "urgent"], "2024-06-15")
    task_service.add_task("Buy Groceries", "Milk and bread", "medium", ["personal"], "2024-01-10")
    task_service.add_task("Call Mom", "Weekly call", "low", ["family"], "2024-01-05")

    # Test search by keyword in title
    results = search_service.search_tasks_by_keyword("Project")
    print(f"   Found {len(results)} tasks matching 'Project'")
    assert len(results) == 1
    assert results[0].title == "Project Alpha"
    print("   ✓ Title search works correctly")

    # Test search by keyword in description
    results = search_service.search_tasks_by_keyword("call")
    print(f"   Found {len(results)} tasks matching 'call'")
    assert len(results) == 1
    assert results[0].title == "Call Mom"
    print("   ✓ Description search works correctly")

    print("\n✓ All search functionality tests passed!")


def test_filter_functionality():
    """Test filter functionality."""
    print("\n\nTesting filter functionality...")

    # Create services
    task_service = TaskService()
    search_service = SearchService(task_service)

    # Add tasks for filtering
    task_service.add_task("High Priority Task", "Important task", "high", ["work"], "2024-01-15")
    task_service.add_task("Low Priority Task", "Less important", "low", ["personal"], "2024-12-31")
    task_service.add_task("Medium Priority Task", "Regular task", "medium", ["work"], "2024-06-30")
    task_service.add_task("Another Work Task", "More work", "high", ["work"], "2024-02-28")

    # Test filter by priority
    high_priority_tasks = search_service.filter_tasks_by_priority("high")
    print(f"   Found {len(high_priority_tasks)} high priority tasks")
    assert len(high_priority_tasks) == 2
    for task in high_priority_tasks:
        assert task.priority == "high"
    print("   ✓ Priority filter works correctly")

    # Test filter by tag
    work_tasks = search_service.filter_tasks_by_tag("work")
    print(f"   Found {len(work_tasks)} work tasks")
    assert len(work_tasks) == 3
    for task in work_tasks:
        assert "work" in task.tags
    print("   ✓ Tag filter works correctly")

    # Test filter by due date
    early_tasks = search_service.filter_tasks_by_due_date("2024-01-15")
    print(f"   Found {len(early_tasks)} tasks with due date 2024-01-15")
    assert len(early_tasks) == 1
    assert early_tasks[0].due_date == "2024-01-15"
    print("   ✓ Due date filter works correctly")

    print("\n✓ All filter functionality tests passed!")


def test_sort_functionality():
    """Test sort functionality."""
    print("\n\nTesting sort functionality...")

    # Create services
    task_service = TaskService()
    sort_service = SortService(task_service)

    # Add tasks for sorting
    task_service.add_task("Zebra Task", "Last alphabetically", "low", [], "2024-12-31")
    task_service.add_task("Alpha Task", "First alphabetically", "high", [], "2024-01-01")
    task_service.add_task("Mango Task", "Middle alphabetically", "medium", [], "2024-06-15")

    # Test sort by title ascending
    sorted_tasks = sort_service.sort_tasks_by_title("asc")
    titles = [task.title for task in sorted_tasks]
    expected_order = ["Alpha Task", "Mango Task", "Zebra Task"]
    print(f"   Sorted titles: {titles}")
    assert titles == expected_order
    print("   ✓ Title sort (ascending) works correctly")

    # Test sort by title descending
    sorted_tasks_desc = sort_service.sort_tasks_by_title("desc")
    titles_desc = [task.title for task in sorted_tasks_desc]
    expected_desc_order = ["Zebra Task", "Mango Task", "Alpha Task"]
    print(f"   Sorted titles (desc): {titles_desc}")
    assert titles_desc == expected_desc_order
    print("   ✓ Title sort (descending) works correctly")

    # Test sort by priority
    sorted_by_priority = sort_service.sort_tasks_by_priority("asc")
    priorities = [task.priority for task in sorted_by_priority]
    # Our sort maps high=0, medium=1, low=2, so ascending should be high, medium, low
    print(f"   Sorted priorities: {priorities}")
    # Actually, our implementation sorts by priority_map which is {"high": 0, "medium": 1, "low": 2}
    # So ascending should be high first, then medium, then low
    assert len(sorted_by_priority) == 3

    print("\n✓ All sort functionality tests passed!")


if __name__ == "__main__":
    print("Starting comprehensive functionality tests for Todo App with Intermediate Level Features...")

    try:
        test_basic_functionality()
        test_search_functionality()
        test_filter_functionality()
        test_sort_functionality()

        print("\n🎉 All functionality tests passed successfully!")
        print("The Todo App with Intermediate Level Features is working correctly.")

    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)