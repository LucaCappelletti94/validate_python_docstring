"""Module defining the CommonTypoException."""


class CommonTypoException(Exception):
    """Class defining the common typo exception.

    This exception is meant to be used to let the user know
    that they have made a common typo in one of the docstrings.
    """

    def __init__(
        self,
        expected_term: str,
        found_term: str,
        raw_documentation: str
    ):
        """Create new Common Typo Exception instance.

        Parameters
        -------------------------
        expected_term: str
            The expected correct term.
        found_term: str
            The term that was found inplace of the correct term.
        raw_documentation: str
            The raw documentation containing the error.
        """
        self._expected_term = expected_term
        self._found_term = found_term
        self._raw_documentation = raw_documentation

    def __str__(self) -> str:
        """Return representation of the current exception."""
        return (
            "A common typo was found! Specifically, we have found "
            "the term `{}` were likely you intended to write `{}`.\n"
            "The complete raw documentation is:\n{}"
        ).format(
            self._found_term,
            self._expected_term,
            self._raw_documentation
        )
