"""Submodule with utilities related to spasers."""


def count_left_spacers(line: str) -> int:
    """Return number of spasers on the left of line."""
    if len(line) == 0:
        return 0

    if line[0] in {"\t", " "}:
        target_spacer = line[0]
    else:
        return 0

    number_of_spasers = 0

    for char in line:
        if char != target_spacer:
            break
        number_of_spasers += 1
    return number_of_spasers
