from acsecompendium import *
from pytest import fixture

# Use pytest fixtures to generate objects we know we'll reuse.
# This makes sure tests run quickly


@fixture(scope="module")
def acsecompendium():
    import acsecompendium

    return acsecompendium


def test_import(acsecompendium):
    assert acsecompendium
