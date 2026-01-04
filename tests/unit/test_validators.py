"""
Unit tests for the validators module with Intermediate Level Features.
"""
import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from src.lib.validators import (
    validate_task_title,
    validate_task_description,
    validate_priority,
    validate_tag,
    validate_tags,
    validate_due_date,
    validate_task_status,
    validate_task_id,
    validate_search_keyword,
    validate_sort_field,
    validate_sort_order,
    validate_filter_criteria
)


class TestValidators(unittest.TestCase):
    """
    Unit tests for validation functions.
    """

    def test_validate_task_title(self):
        """
        Test task title validation.
        """
        # Valid titles
        self.assertTrue(validate_task_title("Valid Title"))
        self.assertTrue(validate_task_title("A" * 200))  # Maximum length

        # Invalid titles
        self.assertFalse(validate_task_title(""))  # Empty
        self.assertFalse(validate_task_title(" "))  # Whitespace only
        self.assertFalse(validate_task_title(None))  # None

    def test_validate_task_description(self):
        """
        Test task description validation.
        """
        # Valid descriptions
        self.assertTrue(validate_task_description("Valid Description"))
        self.assertTrue(validate_task_description(""))  # Empty is OK
        self.assertTrue(validate_task_description("A" * 500))  # Valid length

        # Invalid descriptions (too long)
        # Note: Our validation only checks if it's too long, not if it's invalid otherwise
        self.assertTrue(validate_task_description(None))  # None is OK

    def test_validate_priority(self):
        """
        Test priority validation.
        """
        # Valid priorities
        self.assertTrue(validate_priority("high"))
        self.assertTrue(validate_priority("medium"))
        self.assertTrue(validate_priority("low"))

        # Invalid priorities
        self.assertFalse(validate_priority("invalid"))
        self.assertFalse(validate_priority(""))
        self.assertFalse(validate_priority("HIGH"))  # Case sensitive

    def test_validate_tag(self):
        """
        Test tag validation.
        """
        # Valid tags
        self.assertTrue(validate_tag("work"))
        self.assertTrue(validate_tag("home-work"))
        self.assertTrue(validate_tag("personal123"))
        self.assertTrue(validate_tag("tag_with_underscore"))

        # Invalid tags
        self.assertFalse(validate_tag(""))  # Empty
        self.assertFalse(validate_tag(" "))  # Whitespace
        self.assertFalse(validate_tag("tag@invalid"))  # Special characters
        self.assertFalse(validate_tag("a" * 51))  # Too long

    def test_validate_tags(self):
        """
        Test tags list validation.
        """
        # Valid tag lists
        self.assertTrue(validate_tags(["work", "urgent"]))
        self.assertTrue(validate_tags([]))  # Empty list is OK
        self.assertTrue(validate_tags(None))  # None is OK

        # Invalid tag lists
        self.assertFalse(validate_tags(["valid", "invalid@tag"]))

    def test_validate_due_date(self):
        """
        Test due date validation.
        """
        # Valid dates
        self.assertTrue(validate_due_date("2024-12-31"))
        self.assertTrue(validate_due_date("2023-02-28"))
        self.assertTrue(validate_due_date(None))  # None is OK
        self.assertTrue(validate_due_date(""))  # Empty is OK

        # Invalid dates
        self.assertFalse(validate_due_date("2024-13-01"))  # Invalid month
        self.assertFalse(validate_due_date("invalid-date"))
        self.assertFalse(validate_due_date("2024-12-32"))  # Invalid day

    def test_validate_task_status(self):
        """
        Test task status validation.
        """
        # Valid statuses
        self.assertTrue(validate_task_status("complete"))
        self.assertTrue(validate_task_status("incomplete"))

        # Invalid statuses
        self.assertFalse(validate_task_status("invalid"))
        self.assertFalse(validate_task_status(""))
        self.assertFalse(validate_task_status("Complete"))  # Case sensitive

    def test_validate_task_id(self):
        """
        Test task ID validation.
        """
        # Valid IDs
        self.assertTrue(validate_task_id(1))
        self.assertTrue(validate_task_id(100))

        # Invalid IDs
        self.assertFalse(validate_task_id(0))  # Zero
        self.assertFalse(validate_task_id(-1))  # Negative
        self.assertFalse(validate_task_id("1"))  # String instead of int

    def test_validate_search_keyword(self):
        """
        Test search keyword validation.
        """
        # Valid keywords
        self.assertTrue(validate_search_keyword("search"))
        self.assertTrue(validate_search_keyword("SEARCH"))  # Case insensitive

        # Invalid keywords
        self.assertTrue(validate_search_keyword(""))  # Empty is OK
        self.assertFalse(validate_search_keyword(" "))  # Whitespace is not OK (empty after strip)

    def test_validate_sort_field(self):
        """
        Test sort field validation.
        """
        # Valid fields
        self.assertTrue(validate_sort_field("due_date"))
        self.assertTrue(validate_sort_field("priority"))
        self.assertTrue(validate_sort_field("title"))
        self.assertTrue(validate_sort_field("created_at"))

        # Invalid fields
        self.assertFalse(validate_sort_field("invalid_field"))
        self.assertFalse(validate_sort_field(""))

    def test_validate_sort_order(self):
        """
        Test sort order validation.
        """
        # Valid orders
        self.assertTrue(validate_sort_order("asc"))
        self.assertTrue(validate_sort_order("desc"))

        # Invalid orders
        self.assertFalse(validate_sort_order("invalid"))
        self.assertFalse(validate_sort_order(""))

    def test_validate_filter_criteria(self):
        """
        Test filter criteria validation.
        """
        # Valid criteria
        self.assertTrue(validate_filter_criteria(status="complete"))
        self.assertTrue(validate_filter_criteria(priority="high"))
        self.assertTrue(validate_filter_criteria(tag="work"))
        self.assertTrue(validate_filter_criteria(due_date="2024-12-31"))
        self.assertTrue(validate_filter_criteria(status="complete", priority="high"))


if __name__ == '__main__':
    unittest.main()