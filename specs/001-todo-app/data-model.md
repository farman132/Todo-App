# Data Model for Todo In-Memory Python Console App

## Task Entity

**Description**: Represents a single todo item in the application

**Fields**:
- `id` (integer): Unique identifier for the task; assigned sequentially starting from 1
- `title` (string): Title of the task; required field, cannot be empty
- `description` (string): Detailed description of the task; optional field, can be empty
- `status` (string): Completion status of the task; values are "incomplete" or "complete"

**Validation Rules**:
- ID must be a positive integer
- Title must not be empty or contain only whitespace
- Status must be one of the allowed values ("incomplete", "complete")
- Description can be empty but cannot contain control characters

**State Transitions**:
- Default state: "incomplete" when task is created
- State can be toggled between "incomplete" and "complete" using mark complete/incomplete operation

## TaskList Collection

**Description**: In-memory collection that holds all Task entities during application runtime

**Operations**:
- Add task: Adds a new Task to the collection with a unique ID
- Get all tasks: Returns all tasks in the collection
- Get task by ID: Returns a specific task by its unique ID
- Update task: Modifies an existing task's title or description
- Delete task: Removes a task from the collection
- Mark complete/incomplete: Updates a task's status

**Constraints**:
- All IDs must be unique within the collection
- Collection exists only during application runtime
- No persistence outside of application runtime