"""Using the "assert" keyword, fill out each of these test cases.
Optional: find how to leverage pytest to parametrize the second test with
multiple inputs.
"""

import pytest

import app


def test_hello_default():
    """Test that hello with no arguments has expected result."""

    assert False


def test_hello_custom():
    """Test that hello with arguments has expected result[s]."""
    assert False


def test_count_lines():
    """Use the io module to pass in a string with "n" lines (as a file-like
    object) and test that "n" is returned."""

    assert False


# Note: By marking this as an integration test we can exclude it by adding
#     -m"not integration"
# when invoking pytest or
#     -m integration
# to select all integration tests.
@pytest.mark.integration
def test_hello_integration():
    """Create a test that opens a real file (app.py even) and passes it to
    app.count_lines. Test that the result is accurate. This is an integration
    test since a: it touches the filesystem and b: uses the open function (a
    different unit) to do so.
    """

    assert False