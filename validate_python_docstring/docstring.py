"""Module providing the abstract implementation of a Python docstring."""
from typing import List, Optional
from .docstring_argument import DocstringArgument
from .docstring_section import DocstringSection


class Docstring:
    """Class providing abstract implementation of Python docstring."""

    def __init__(self, raw: str):
        """Create new docstring object.

        Parameters
        -----------------------------
        raw: str
            The raw version of the docstring.
        """
        self._raw: str = raw
        self._brief_description: str = self._parse_brief_description()
        self._arguments = self._parse_arguments()
        self._return_statement = self._parse_return_statement()
        self._sections = self._parse_sections()

    def _parse_brief_description(self) -> str:
        """Returns the return docstring section."""
        raise NotImplementedError(
            "The Docstring._parse_brief_description must be implemented "
            "in the child class."
        )

    def _parse_arguments(self) -> List[DocstringArgument]:
        """Returns the return docstring section."""
        raise NotImplementedError(
            "The Docstring._parse_arguments must be implemented "
            "in the child class."
        )

    def _parse_sections(self) -> List[DocstringArgument]:
        """Returns the sections."""
        raise NotImplementedError(
            "The Docstring._parse_sections must be implemented "
            "in the child class."
        )

    def _parse_return_statement(self) -> Optional[DocstringSection]:
        """Returns the return statement section."""
        raise NotImplementedError(
            "The Docstring._parse_return_statement must be implemented "
            "in the child class."
        )
