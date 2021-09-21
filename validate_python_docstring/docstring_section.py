"""Submodule providing class representing a docstring section."""


class DocstringSection:
    """Class providing representation of a docstring section."""

    def __init__(
        self,
        section_title: str,
        section_description: str
    ):
        """Create new instance of Docstring Section.
        
        Parameters
        ---------------------
        section_title: str
            Title of the section.
        section_description: str
            Description of the section.
        
        Raises
        --------------------------
        ValueError
            If the section title is an empty string.
        ValueError
            If the section description is an empty string.
        """
        if len(section_title) == 0:
            raise ValueError(
                "The provided section title is an empty string."
            )
        if len(section_description) == 0:
            raise ValueError(
                "The provided section description is an empty string."
            )
        self._section_title = section_title
        self._section_description = section_description

    @property
    def section_title(self) -> str:
        """Return the section title."""
        return self._section_title

    @property
    def section_description(self) -> str:
        """Return the section description."""
        return self._section_description