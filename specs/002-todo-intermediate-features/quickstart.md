# Quickstart Guide: Todo App – Intermediate Level Features

## Setup

1. Ensure Python 3.13+ is installed on your system
2. Clone or navigate to the project directory
3. No additional dependencies required (using standard library only)

## Running the Application

```bash
cd src
python main.py
```

## Using Intermediate Features

### Adding Tasks with Priority and Tags

When adding a task, you'll be prompted to optionally specify:
- Priority: high, medium, or low
- Tags: comma-separated list (e.g., "work,urgent")
- Due date: in YYYY-MM-DD format (optional)

### Viewing Tasks

All tasks are displayed with:
- Status indicator (✔ for complete, ✖ for incomplete)
- Priority indicator (🔴 high, 🟡 medium, 🟢 low)
- Priority level (HIGH, MEDIUM, LOW)
- Tags
- Due date (if set)
- Creation timestamp

### Searching Tasks

From the main menu, select option 6 (Search tasks) and enter a keyword to search in task titles and descriptions.

### Filtering Tasks

From the main menu, select option 7 (Filter tasks) and specify criteria:
- Status: complete/incomplete
- Priority: high/medium/low
- Tag: specific tag to filter by
- Due date: specific date in YYYY-MM-DD format

### Sorting Tasks

From the main menu, select option 8 (Sort tasks) and choose:
- Field to sort by: Title, Priority, Due Date, or Creation Date
- Sort order: Ascending (A-Z, low to high) or Descending (Z-A, high to low)

## Example Usage

1. Add a new task with high priority and work tag
2. View all tasks to see priority indicators
3. Filter tasks by "high" priority to see only high priority tasks
4. Sort tasks by due date to see what's coming up soon
5. Search for specific keywords in task titles or descriptions

## Existing Basic Features

All original features remain functional:
- Add, Delete, Update, View, Mark Complete/Incomplete
- These operations now support the new attributes (priority, tags, due date)