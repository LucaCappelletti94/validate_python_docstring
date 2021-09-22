"""Module providing the implementation of a Numpy style Python docstring."""
from typing import List, Optional
from .docstring import Docstring
from .docstring_argument import DocstringArgument
from .docstring_section import DocstringSection
from .utils import count_left_spacers


class NumpyStyleDocstring(Docstring):
    """Class providing implementation of Numpy style Python docstring."""

    def _parse_brief_description(self) -> str:
        """Returns the return docstring section."""
        return self._raw.split("\n", maxsplit=1)[0]

    def has_raw_section_from_name(self, section_name: str) -> bool:
        """Return whether the docstring has section with given name following numpy style.

        Parameters
        -----------------------
        section_name: str
            The name of the section.

        Returns
        -----------------------
        Whether the section exists.
        """
        lines = self._raw.split("\n")
        return any(
            section_name == this_line.strip() and set(next_line.strip()) == set("-")
            for this_line, next_line in zip(
                lines[:-1],
                lines[1:],
            )
        )

    def has_parameters_section(self) -> bool:
        """Return whether the docstring has parameters section following numpy style."""
        return self.has_raw_section_from_name("Parameters")

    def has_returns_section(self) -> bool:
        """Return whether the docstring has returns section following numpy style."""
        return self.has_raw_section_from_name("Returns")

    def _parse_arguments(self) -> List[DocstringArgument]:
        """Returns the return docstring section."""
        if not self.has_parameters_section():
            return []
        # Iterate over the description lines
        lines_iterator = iter(self._raw.split("\n"))
        for line in lines_iterator:
            if line.strip() != "Parameters":
                continue
            else:
                break

        frame_line = next(lines_iterator)
        expected_number_of_spacers = count_left_spacers(frame_line)
        arguments = []
        current_argument_name = None
        current_argument_type = None
        current_argument_description = None
        current_argument_default_value = None
        for line in lines_iterator:
            if line.strip() == "":
                # We have finished the section
                break
            spacers_in_line = count_left_spacers(line)
            if spacers_in_line == expected_number_of_spacers and ": " in line:
                # This is an argument to be parsed.
                if current_argument_name is not None:
                    arguments.append(DocstringArgument(
                        argument_name=current_argument_name,
                        argument_type=current_argument_type,
                        description=current_argument_description,
                        default_value=current_argument_default_value,
                    ))
                    current_argument_name = None
                    current_argument_type = None
                    current_argument_description = None
                    current_argument_default_value = None
                current_argument_name, current_argument_type = line.strip().split(": ")
                current_argument_name = current_argument_name.strip()
                if " = " in current_argument_type:
                    current_argument_type, current_argument_default_value = current_argument_type.split(
                        " = ")
                    current_argument_default_value = current_argument_default_value.strip()
                current_argument_type = current_argument_type.strip()
            elif spacers_in_line > expected_number_of_spacers and current_argument_name is not None:
                # This is part of the description of the last argument.
                if current_argument_description is None:
                    current_argument_description = line.strip()
                else:
                    current_argument_description += " " + line.strip()
            else:
                # This is an error case
                raise ValueError(
                    (
                        "An error was encountered while trying to parse the "
                        "the following docstring arguments:\n {}\n"
                        "Specifically the line causing the class is: `{}`.\n"
                        "The number of spacers found in the line is {} and "
                        "the number of spacers representing the depth of "
                        "the section is {}."
                    ).format(
                        self._raw,
                        line,
                        spacers_in_line,
                        expected_number_of_spacers
                    )
                )
        return arguments

    def _parse_sections(self) -> List[DocstringArgument]:
        """Returns the sections."""
        sections = []
        lines = self._raw.split("\n")
        frame_symbols = {"-"}
        reserved_section_titles = {
            "Returns",
            "Parameters"
        }
        section_title = None
        section_description = None
        for i, line in enumerate(lines):
            if set(line.strip()) == frame_symbols:
                if section_title is not None:
                    sections.append(DocstringSection(
                        section_title=section_title,
                        section_description=section_description
                    ))
                    section_title = None
                    section_description = None
                tentative_section_title = lines[i-1].strip()
                if tentative_section_title in reserved_section_titles:
                    continue
                section_title = tentative_section_title
                # Then we continue because we want to skip the frame symbols
                continue
            if section_title is not None:
                if section_description is None:
                    section_description = line.strip()
                else:
                    section_description += " " + line.strip()
        return sections

    def _parse_return_statement(self) -> Optional[DocstringSection]:
        """Returns the return statement section."""
        if not self.has_returns_section():
            return None
        # Iterate over the description lines
        lines_iterator = iter(self._raw.split("\n"))
        for line in lines_iterator:
            if line.strip() != "Returns":
                expected_number_of_spacers = count_left_spacers(line)
                continue
            else:
                break

        # We skip the frame line
        _ = next(lines_iterator)

        description = ""
        for line in lines_iterator:
            if line.strip() == "":
                break
            description += line.strip()

        return DocstringSection(
            section_title="Returns",
            section_description=description
        )
