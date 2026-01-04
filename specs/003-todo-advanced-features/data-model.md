# Data Model: Advanced Intelligent Features for Python In-Memory Todo App

## Task Entity (Extended)

### Attributes
- **id**: Integer (unique, auto-incrementing)
- **title**: String (required, non-empty)
- **description**: String (optional)
- **status**: String (enum: "complete", "incomplete", default: "incomplete")
- **priority**: String (enum: "high", "medium", "low", default: "medium")
- **tags**: List of Strings (optional, default: empty list)
- **due_date**: String or null (optional, ISO 8601 date format: YYYY-MM-DD)
- **created_at**: String (ISO 8601 datetime format: YYYY-MM-DDTHH:MM:SS)
- **recurrence_pattern**: String or null (enum: "daily", "weekly", "monthly", null for non-recurring)
- **next_occurrence**: String or null (ISO 8601 date format: YYYY-MM-DD, when the next instance should appear)

### Validation Rules
- **id**: Must be unique positive integer
- **title**: Must be non-empty string (1-200 characters)
- **status**: Must be one of the allowed values
- **priority**: Must be one of the allowed values (high, medium, low)
- **tags**: Each tag must be 1-50 characters, no special characters except hyphens and underscores
- **due_date**: If provided, must be valid ISO 8601 date format
- **recurrence_pattern**: If provided, must be one of "daily", "weekly", "monthly"
- **next_occurrence**: If provided, must be valid ISO 8601 date format

### State Transitions
- **Status**: Can transition from "incomplete" to "complete" and vice versa
- **Priority**: Can be updated to any valid priority value
- **Tags**: Can be added, removed, or modified
- **Due date**: Can be set, updated, or cleared
- **Recurrence**: Can be set, updated, or cleared; when cleared, next_occurrence is also cleared

## Recurrence Entity

### Attributes
- **pattern**: String (enum: "daily", "weekly", "monthly")
- **original_task_id**: Integer (reference to the original task that should be duplicated)
- **next_occurrence**: String (ISO 8601 date format: YYYY-MM-DD)

### Validation Rules
- **pattern**: Must be one of the allowed values
- **original_task_id**: Must reference an existing task
- **next_occurrence**: Must be a valid future date

## Due Date Management

### Due Date Status
- **due_date**: Date when the task should be completed
- **overdue**: Boolean calculated based on due_date and current date
- **days_until_due**: Integer calculated as days between current date and due_date

### Calculated Properties
- **is_overdue**: True if due_date is in the past
- **is_due_soon**: True if due_date is within 1-3 days from current date
- **due_status**: Enum ("overdue", "due_soon", "not_due")

## Recurring Task Processing

### Recurrence Rules
- **Daily**: Create new instance every day after completion
- **Weekly**: Create new instance every 7 days after completion
- **Monthly**: Create new instance every month after completion (same day of month)
- **Completion**: When a recurring task is marked complete, schedule the next occurrence based on the pattern