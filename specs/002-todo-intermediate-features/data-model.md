# Data Model: Todo App – Intermediate Level Features

## Task Entity

### Attributes
- **id**: Integer (unique, auto-incrementing)
- **title**: String (required, non-empty)
- **description**: String (optional)
- **status**: String (enum: "complete", "incomplete", default: "incomplete")
- **priority**: String (enum: "high", "medium", "low", default: "medium")
- **tags**: List of Strings (optional, default: empty list)
- **due_date**: String or null (optional, ISO 8601 date format: YYYY-MM-DD)
- **created_at**: String (ISO 8601 datetime format: YYYY-MM-DDTHH:MM:SS)

### Validation Rules
- **id**: Must be unique positive integer
- **title**: Must be non-empty string (1-200 characters)
- **status**: Must be one of the allowed values
- **priority**: Must be one of the allowed values (high, medium, low)
- **tags**: Each tag must be 1-50 characters, no special characters except hyphens and underscores
- **due_date**: If provided, must be valid ISO 8601 date format

### State Transitions
- **Status**: Can transition from "incomplete" to "complete" and vice versa
- **Priority**: Can be updated to any valid priority value
- **Tags**: Can be added, removed, or modified
- **Due date**: Can be set, updated, or cleared

## Task Search Criteria

### Search Attributes
- **keyword**: String to search in title or description
- **status**: Filter by completion status
- **priority**: Filter by priority level
- **due_date**: Filter by due date (exact match, before, after, or range)
- **tags**: Filter by specific tags

### Search Results
- **matches**: List of Task entities matching the criteria
- **total_count**: Integer count of matching tasks

## Task Sort Parameters

### Sort Attributes
- **field**: String (enum: "due_date", "priority", "title", "created_at")
- **order**: String (enum: "asc", "desc", default: "asc")

### Sort Results
- **sorted_tasks**: List of Task entities sorted according to parameters
- **sort_method**: String describing the sort applied