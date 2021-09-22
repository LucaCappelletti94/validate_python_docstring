"""Module with methods to scrape packages."""
from typing import Set, Any
import inspect


def _explore_python(module) -> Set[Any]:
    """Return set of modules in given module."""
    return {
        getattr(module, x)
        for x in dir(module)
        if not x.startswith("_")
        and (
            inspect.isfunction(getattr(module, x))
            or inspect.isclass(getattr(module, x))
            or inspect.ismodule(getattr(module, x))
        ) and (
            module.__name__ in inspect.getmodule(getattr(module, x)).__name__
        ) and
        not inspect.isbuiltin(getattr(module, x))
    }


def explore_python(module) -> Set[Any]:
    """Return ricursively set of modules in given module."""
    if inspect.isfunction(module) or inspect.isclass(module):
        return {module}

    return {
        y
        for x in _explore_python(module)
        for y in explore_python(x)
    }
