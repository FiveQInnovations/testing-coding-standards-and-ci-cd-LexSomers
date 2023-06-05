"""Sample code for testing."""


def hello(name='world'):
    """Optionally takes a name and returns hello <name>."""

    return f'Hello {name}'


def count_lines(f):
    """Return the number of lines in a given file object."""

    return len(f.readlines())
