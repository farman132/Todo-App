---
description: "Task list for Todo App Intermediate Level Features implementation"
---

# Tasks: Todo App – Intermediate Level Features

**Input**: Design documents from `/specs/002-todo-intermediate-features/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 [P] Create project structure per implementation plan (src/models/, src/services/, src/cli/, src/lib/)
- [ ] T002 Initialize Python project with standard library dependencies only
- [ ] T003 [P] Configure linting and formatting tools (pylint, black)

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 [P] Create base Task model in src/models/task.py with id, title, description, status fields
- [x] T005 [P] Implement TaskService in src/services/task_service.py with basic CRUD operations
- [x] T006 [P] Create CLI interface skeleton in src/cli/cli_interface.py
- [x] T007 Create basic validators in src/lib/validators.py
- [x] T008 Test basic task operations to ensure existing functionality remains intact

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Assign Priorities and Tags to Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to assign priority levels (high/medium/low) and tags (work/home/personal) to tasks

**Independent Test**: Can add a task with priority and tags, then view the task to confirm the priority and tags are properly stored and displayed

### Implementation for User Story 1

- [x] T009 [P] [US1] Update Task model in src/models/task.py to include priority (high/medium/low) and tags (list) fields
- [x] T010 [US1] Update TaskService in src/services/task_service.py to handle priority and tags in add_task method
- [x] T011 [US1] Update TaskService to allow updating priority and tags in update_task method
- [x] T012 [US1] Add validation for priority values in src/lib/validators.py
- [x] T013 [US1] Add validation for tag format in src/lib/validators.py
- [x] T014 [US1] Update CLI interface in src/cli/cli_interface.py to accept priority and tags when adding tasks
- [x] T015 [US1] Update CLI display to show priority indicators and tags for each task
- [x] T016 [US1] Add menu option to update task priority and tags
- [x] T017 [US1] Test that existing basic functionality (Add, Delete, Update, View, Mark Complete) remains intact

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - Search and Filter Tasks (Priority: P2)

**Goal**: Enable users to search tasks by keyword and filter by status, priority, or date

**Independent Test**: Can create multiple tasks with different attributes, then use search and filter functions to verify they return the correct subset of tasks

### Implementation for User Story 2

- [x] T018 [P] [US2] Create SearchService in src/services/search_service.py with keyword search functionality
- [x] T019 [P] [US2] Implement filter functionality in src/services/search_service.py for status, priority, and date
- [x] T020 [US2] Add filter by tags functionality to SearchService
- [x] T021 [US2] Create FilterService in src/services/search_service.py to handle complex filter combinations
- [x] T022 [US2] Update CLI interface in src/cli/cli_interface.py to add search functionality
- [x] T023 [US2] Update CLI interface to add filter functionality with menu options
- [x] T024 [US2] Add validation for search and filter parameters in src/lib/validators.py
- [x] T025 [US2] Test search functionality with various keyword inputs
- [x] T026 [US2] Test filter functionality with different criteria combinations

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 - Sort Tasks (Priority: P3)

**Goal**: Enable users to sort task list by due date, priority, or alphabetically

**Independent Test**: Can create multiple tasks with different attributes, then apply different sort orders to verify the tasks are displayed in the correct sequence

### Implementation for User Story 3

- [x] T027 [P] [US3] Create SortService in src/services/sort_service.py with sorting functionality
- [x] T028 [US3] Implement sort by due date functionality in SortService
- [x] T029 [US3] Implement sort by priority functionality in SortService (high to low, low to high)
- [x] T030 [US3] Implement sort alphabetically by title functionality in SortService
- [x] T031 [US3] Add sort functionality to CLI interface in src/cli/cli_interface.py with menu options
- [x] T032 [US3] Add validation for sort parameters in src/lib/validators.py
- [x] T033 [US3] Test sort functionality with various sorting criteria
- [x] T034 [US3] Ensure sort works in combination with search and filter functionality
- [x] T035 [US3] Test that all sorting options display correctly in CLI

**Checkpoint**: All user stories should now be independently functional

---
## Phase 6: Integration & CLI Enhancement

**Goal**: Integrate all features into a cohesive CLI experience

- [x] T036 [P] Add comprehensive input validation across all services
- [x] T037 Update CLI menu to provide clear navigation between all new features
- [x] T038 Add error handling and user feedback for all new features
- [x] T039 Ensure all new features maintain the CLI-only interface requirement
- [x] T040 Test that all features work together without conflicts

---
## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T041 [P] Add unit tests for all new functionality in tests/unit/
- [x] T042 [P] Add integration tests for feature combinations in tests/integration/
- [x] T043 Documentation updates in README.md for new features
- [x] T044 Code cleanup and refactoring
- [x] T045 Performance testing with up to 1000 tasks
- [x] T046 Run quickstart.md validation to ensure all features work as documented
- [x] T047 Final validation that all existing basic functionality remains intact

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Integration (Phase 6)**: Depends on all user stories being complete
- **Polish (Phase 7)**: Depends on all desired features being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May use components from US1
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May use components from US1/US2

### Within Each User Story

- Models before services
- Services before endpoints/cli
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members