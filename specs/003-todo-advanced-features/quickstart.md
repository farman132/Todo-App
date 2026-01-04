# Quickstart Guide: Advanced Intelligent Features for Python In-Memory Todo App

## Setup

1. Ensure Python 3.13+ is installed on your system
2. Clone or navigate to the project directory
3. No additional dependencies required (using standard library only)

## Running the Application

```bash
cd src
python main.py
```

## Using Advanced Features

### Creating Recurring Tasks

When adding or updating a task, you can specify a recurrence pattern:
- Choose from daily, weekly, or monthly recurrence
- When a recurring task is marked complete, a new instance will be automatically created according to the pattern

### Setting Due Dates

When adding or updating a task, you can specify a due date:
- Enter date in YYYY-MM-DD format (e.g., 2024-12-31)
- Tasks with due dates will show their status (overdue, due soon, not due)

### Viewing Task Status

- Overdue tasks will be highlighted with special indicators
- Tasks due soon will have appropriate visual cues
- Recurring tasks will show their recurrence pattern

## Example Usage

1. Add a recurring task with weekly pattern (e.g., "Take out trash")
2. Add a task with a due date (e.g., "Submit report" due in 3 days)
3. Mark the recurring task as complete and see how a new instance appears
4. View all tasks to see overdue and due-soon indicators
5. Update existing tasks to add due dates or recurrence patterns

## Integration with Existing Features

All new advanced features work seamlessly with existing functionality:
- Priorities and tags continue to work as before
- Search and filter functions include the new attributes
- Sort functionality works with due dates and recurrence patterns
- All basic functionality remains unchanged