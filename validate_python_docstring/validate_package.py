"""Module providing methods to validate a python package documentation."""
import inspect

from .numpy_style_docstring import NumpyStyleDocstring
from .utils import explore_python


def validate_function(function):
    """Execute validation of the provided function."""
    NumpyStyleDocstring(function.__doc__)


def validate_class(klass):
    """Execute validation of the provided class."""
    NumpyStyleDocstring(klass.__doc__)
    for object_to_validate in dir(klass):
        if type(getattr(klass, object_to_validate)) != property and inspect.ismethod(getattr(klass, object_to_validate)):
            validate_function(object_to_validate)


def validate_package(module):
    """Execute validation on the provided package."""
    for object_to_validate in explore_python(module):
        if inspect.isclass(object_to_validate):
            content = validate_class(object_to_validate)
        else:
            content = validate_function(object_to_validate)
