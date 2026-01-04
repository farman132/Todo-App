# API Contracts: Todo App – Intermediate Level Features

## Task Management Operations

### Add Task with Priority and Tags
- **Input**: title (string), description (optional string), priority (enum: high/medium/low), tags (list of strings)
- **Output**: Task object with all attributes
- **Errors**: Invalid input format, missing required fields

### Update Task Priority and Tags
- **Input**: task ID (integer), priority (optional enum), tags (optional list)
- **Output**: Updated Task object
- **Errors**: Task not found, invalid input format

### Search Tasks
- **Input**: keyword (string), filters (optional object with status, priority, date, tags)
- **Output**: List of matching Task objects
- **Errors**: Invalid filter parameters

### Filter Tasks
- **Input**: filter criteria (object with status, priority, date, tags)
- **Output**: List of matching Task objects
- **Errors**: Invalid filter parameters

### Sort Tasks
- **Input**: sort criteria (field enum, order enum)
- **Output**: List of Task objects sorted according to criteria
- **Errors**: Invalid sort parameters

## CLI Interface Operations

### Display Tasks with Priority and Tags
- **Input**: None
- **Output**: Formatted list of tasks with priority indicators and tags
- **Errors**: None

### Get User Input for Priority
- **Input**: User selection (high/medium/low)
- **Output**: Priority value
- **Errors**: Invalid selection

### Get User Input for Tags
- **Input**: User input (comma-separated string)
- **Output**: List of tag strings
- **Errors**: Invalid tag format