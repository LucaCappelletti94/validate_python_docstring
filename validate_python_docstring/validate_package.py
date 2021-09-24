"""Module providing methods to validate a python package documentation."""
import inspect

from .numpy_style_docstring import NumpyStyleDocstring
from .utils import explore_python


def validate_function(function, verbose: bool = False, depth: int = 0):
    """Execute validation of the provided function."""
    if verbose:
        print("{}Validating {}".format("\t"*depth, function))
    docstring = NumpyStyleDocstring(function.__doc__)
    print(docstring)


def validate_class(klass, verbose: bool = False):
    """Execute validation of the provided class."""
    NumpyStyleDocstring(klass.__doc__)
    if verbose:
        print("Validating {}".format(klass))
    for object_to_validate in dir(klass):
        if type(getattr(klass, object_to_validate)) != property and (
            inspect.ismethod(getattr(klass, object_to_validate)) or
            inspect.isfunction(getattr(klass, object_to_validate))
        ):
            validate_function(
                getattr(klass, object_to_validate),
                verbose=verbose,
                depth=1
            )


def validate_package(module, verbose: bool = False):
    """Execute validation on the provided package."""
    for object_to_validate in explore_python(module):
        if inspect.isclass(object_to_validate):
            validate_class(object_to_validate, verbose=verbose)
        else:
            validate_function(object_to_validate, verbose=verbose)
