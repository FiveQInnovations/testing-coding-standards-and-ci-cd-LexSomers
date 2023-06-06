"""Sample code for testing."""


def hello(name='world'):
    """Optionally takes a name and returns hello <name>."""

    return f'Hello {name}'


def count_lines(file):
    """Return the number of lines in a given file object."""

    return len(file.readlines())
