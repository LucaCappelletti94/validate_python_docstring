"""Submodule checking for common errors in docstrings."""
import compress_json
from ..exceptions import CommonTypoException


def check_for_common_errors(raw: str):
    """Check and raise if errors have been found.

    Parameters
    ------------------------
    raw: str
        The raw docstring to check.
    """
    common_errors = compress_json.local_load("common_errors.json")
    lowercase_docstring = raw.lower()
    for expected_term, this_common_errors in common_errors.items():
        for target_error, placeholders in this_common_errors.items():
            for placeholder in placeholders:
                needle = placeholder.format(target_error)
                if needle in lowercase_docstring:
                    raise CommonTypoException(
                        expected_term=expected_term,
                        found_term=needle,
                        raw_documentation=raw
                    )
