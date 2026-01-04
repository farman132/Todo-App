"""
Recurrence model for the Advanced Intelligent Features of the Todo In-Memory Python Console App.

This module defines the Recurrence data structure with pattern, original_task_id, and next_occurrence.
"""
from dataclasses import dataclass
from typing import Optional
from datetime import datetime, timedelta


@dataclass
class Recurrence:
    """
    Represents a recurrence pattern for a recurring task.

    Attributes:
        pattern (str): The recurrence pattern ('daily', 'weekly', 'monthly')
        original_task_id (int): The ID of the original task that should be duplicated
        next_occurrence (str): The date when the next instance should appear (YYYY-MM-DD format)
    """

    pattern: str
    original_task_id: int
    next_occurrence: Optional[str] = None

    def __post_init__(self):
        """Validate the recurrence after initialization."""
        if self.pattern not in ["daily", "weekly", "monthly"]:
            raise ValueError("Recurrence pattern must be 'daily', 'weekly', or 'monthly'")

        if not isinstance(self.original_task_id, int) or self.original_task_id <= 0:
            raise ValueError("Original task ID must be a positive integer")

        if self.next_occurrence:
            try:
                datetime.strptime(self.next_occurrence, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Next occurrence must be in YYYY-MM-DD format")

    def calculate_next_occurrence(self, current_date_str: str) -> str:
        """
        Calculate the next occurrence date based on the recurrence pattern.

        Args:
            current_date_str (str): The current date in YYYY-MM-DD format

        Returns:
            str: The next occurrence date in YYYY-MM-DD format
        """
        current_date = datetime.strptime(current_date_str, "%Y-%m-%d")

        if self.pattern == "daily":
            next_date = current_date + timedelta(days=1)
        elif self.pattern == "weekly":
            next_date = current_date + timedelta(weeks=1)
        elif self.pattern == "monthly":
            # Calculate next month - handle month overflow
            year = current_date.year
            month = current_date.month + 1
            day = current_date.day

            # Handle year overflow
            if month > 12:
                year += 1
                month = 1

            # Handle day overflow for months with fewer days (e.g., Jan 31 -> Feb 28/29)
            try:
                next_date = current_date.replace(year=year, month=month, day=day)
            except ValueError:
                # If the day doesn't exist in the next month, use the last day of the next month
                # For example, Jan 31 -> Feb 28 (or 29 in leap years)
                if month == 2:
                    # February - get last day of February
                    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                        # Leap year
                        next_date = current_date.replace(year=year, month=month, day=29)
                    else:
                        # Non-leap year
                        next_date = current_date.replace(year=year, month=month, day=28)
                elif month in [4, 6, 9, 11]:
                    # April, June, September, November have 30 days
                    next_date = current_date.replace(year=year, month=month, day=30)
                else:
                    # All other months have 31 days, so the day exists
                    next_date = current_date.replace(year=year, month=month, day=day)
                    # Actually, we'd need to go to the next month since this day doesn't exist
                    # Let's try the last day of the target month
                    import calendar
                    max_day = calendar.monthrange(year, month)[1]
                    next_date = current_date.replace(year=year, month=month, day=max_day)

        return next_date.strftime("%Y-%m-%d")