"""Test to check that all the docstring the package are OK according to the package itself."""
import validate_python_docstring
from validate_python_docstring import validate_package


def test_package_is_self_consistent():
    """This test is meant to check that all docstrings in the package are valid according to the package."""
    validate_package(validate_python_docstring)
