"""Module providing the implementation of a Numpy style Python docstring."""
from validate_python_docstring.utils import check_for_common_errors
from .docstring import Docstring
from .utils import check_for_common_errors


class NumpyStyleDocstring(Docstring):
    """Class providing implementation of Numpy style Python docstring."""

    def _parse(self):
        check_for_common_errors(self._raw)
