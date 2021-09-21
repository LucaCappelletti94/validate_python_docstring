"""Submodule defining the name and attributes of an argument in the docstring."""


class DocstringArgument:
    """Class defining an argument object in a Python docstring."""

    def __init__(
        self,
        argument_name: str,
        argument_type: str,
        description: str,
        default_value: str = None,
    ):
        """Create the instance of docstring argument.

        Parameters
        --------------------------
        argument_name: str
            Name of the argument.
        argument_type: str
            Type of the argument as a string.
        description: str
            The description of the argument.
        default_value: str = None
            Default value of the argument.
            Note that this value will be expected as STRING!
            So a None value will be expected as "None".

        Raises
        --------------------------
        ValueError
            If the argument name is an empty string.
        ValueError
            If the argument type is an empty string.
        ValueError
            If the argument description is an empty string.
        """
        if len(argument_name) == 0:
            raise ValueError(
                "The provided argument name is an empty string."
            )
        if len(argument_type) == 0:
            raise ValueError(
                "The provided argument type is an empty string."
            )
        if len(description) == 0:
            raise ValueError(
                "The provided description is an empty string."
            )
        self._argument_name = argument_name
        self._argument_type = argument_type
        self._description = description
        self._default_value = default_value

    @property
    def argument_name(self) -> str:
        """Return the argument name."""
        return self._argument_name

    @property
    def argument_type(self) -> str:
        """Return the argument type."""
        return self._argument_type

    @property
    def default_value(self) -> str:
        """Return the argument default type."""
        return self._default_value

    @property
    def description(self) -> str:
        """Return the argument default type."""
        return self._description
