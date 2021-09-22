"""Submodule with utilities related to tabs."""


def count_left_tabs(line: str) -> int:
    """Return number of tabs on the left of line."""
    number_of_tabs = 0
    for char in line:
        if char != "\t":
            break
        number_of_tabs += 1
    return number_of_tabs
