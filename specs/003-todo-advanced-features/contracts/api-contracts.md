# API Contracts: Advanced Intelligent Features for Python In-Memory Todo App

## Recurring Task Operations

### Create Recurring Task
- **Input**: title (string), description (optional string), priority (enum: high/medium/low), tags (list of strings), recurrence_pattern (enum: daily/weekly/monthly), due_date (optional date string)
- **Output**: Task object with all attributes including recurrence info
- **Errors**: Invalid recurrence pattern, invalid date format

### Update Recurring Task
- **Input**: task ID (integer), recurrence_pattern (optional enum), due_date (optional date string)
- **Output**: Updated Task object
- **Errors**: Task not found, invalid recurrence pattern

### Process Completed Recurring Task
- **Input**: task ID (integer) of completed recurring task
- **Output**: New instance of the recurring task created according to pattern
- **Errors**: Task not found, task is not recurring

## Due Date Management Operations

### Check Overdue Tasks
- **Input**: None
- **Output**: List of Task objects with overdue status
- **Errors**: None

### Update Due Date
- **Input**: task ID (integer), due_date (date string)
- **Output**: Updated Task object
- **Errors**: Invalid date format, task not found

### Calculate Due Status
- **Input**: Task object with due_date
- **Output**: Due status (overdue, due_soon, not_due) and days until due
- **Errors**: Invalid date format

## CLI Interface Operations

### Add Recurring Task
- **Input**: User selections for title, description, priority, tags, recurrence pattern
- **Output**: Confirmation message and new task ID
- **Errors**: Invalid recurrence pattern, validation errors

### View Due Status
- **Input**: None
- **Output**: Task list with due date indicators and overdue status
- **Errors**: None

### Set Due Date for Existing Task
- **Input**: Task ID and due date
- **Output**: Confirmation message
- **Errors**: Invalid date format, task not found