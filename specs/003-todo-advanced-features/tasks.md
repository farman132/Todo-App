---
description: "Task list for Advanced Intelligent Features implementation"
---

# Tasks: Advanced Intelligent Features for Python In-Memory Todo App

**Input**: Design documents from `/specs/003-todo-advanced-features/`
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

- [x] T001 [P] Create recurrence model in src/models/recurrence.py with recurrence pattern and next occurrence fields
- [x] T002 [P] Extend Task model in src/models/task.py to include recurrence and due date attributes
- [x] T003 [P] Add recurrence and due date validation functions in src/lib/validators.py

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 [P] Implement RecurrenceService in src/services/recurrence_service.py with recurring task logic
- [x] T005 [P] Implement DateService in src/services/date_service.py with due date management
- [x] T006 [P] Update TaskService in src/services/task_service.py to handle recurring tasks and due dates
- [x] T007 [P] Add due date and recurrence functionality to CLI interface in src/cli/cli_interface.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Recurring Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to create tasks that repeat automatically (daily, weekly, monthly) with automatic rescheduling on completion

**Independent Test**: Can create a recurring task, mark it complete, and verify that a new instance of the task is automatically created according to the recurrence schedule

### Implementation for User Story 1

- [x] T008 [US1] Update CLI interface in src/cli/cli_interface.py to accept recurrence pattern when adding tasks
- [x] T009 [US1] Add menu option to set recurrence pattern for existing tasks in CLI
- [x] T010 [US1] Implement recurring task creation logic in RecurrenceService
- [x] T011 [US1] Implement automatic rescheduling when recurring tasks are completed
- [x] T012 [US1] Add recurrence pattern validation in validators.py
- [x] T013 [US1] Update task display to show recurrence indicators in CLI
- [x] T014 [US1] Test that recurring tasks are properly created and rescheduled

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - Due Dates & Reminders (Priority: P2)

**Goal**: Enable users to assign due dates to tasks and see overdue status with visual indicators

**Independent Test**: Can create tasks with due dates, view them to confirm due date display, and check that overdue tasks are properly identified

### Implementation for User Story 2

- [x] T015 [US2] Update CLI interface in src/cli/cli_interface.py to accept due dates when adding tasks
- [x] T016 [US2] Add menu option to set due dates for existing tasks in CLI
- [x] T017 [US2] Implement due date management in DateService
- [x] T018 [US2] Implement overdue status detection logic
- [x] T019 [US2] Add due date validation in validators.py
- [x] T020 [US2] Update task display to show due dates and overdue status in CLI
- [x] T021 [US2] Test that due dates are properly assigned and overdue status is detected

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: Integration & CLI Enhancement

**Goal**: Integrate all advanced features into a cohesive CLI experience

- [x] T022 [P] Update CLI menu to provide clear navigation between all new advanced features
- [x] T023 Add error handling and user feedback for all new advanced features
- [x] T024 Ensure all new features maintain the CLI-only interface requirement
- [x] T025 Test that all advanced features work together without conflicts
- [x] T026 Test integration with existing basic and intermediate features

---
## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T027 [P] Add unit tests for all new advanced functionality in tests/unit/
- [x] T028 [P] Add integration tests for advanced feature combinations in tests/integration/
- [x] T029 Update documentation in README.md for new advanced features
- [x] T030 Code cleanup and refactoring
- [x] T031 Run quickstart.md validation to ensure all advanced features work as documented
- [x] T032 Final validation that all existing basic and intermediate functionality remains intact

---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2)
- **Integration (Phase 5)**: Depends on all user stories being complete
- **Polish (Phase 6)**: Depends on all desired features being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1

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