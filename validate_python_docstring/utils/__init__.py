"""Submodule with utilities to validate docstrings."""
from .check_for_common_errors import check_for_common_errors
from .count_left_tabs import count_left_tabs

__all__ = [
    "check_for_common_errors",
    "count_left_tabs"
]
