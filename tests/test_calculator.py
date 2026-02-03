from mypackage import add


def test_add_direct():
    assert add(2, 3) == 5


def test_add_with_fixture(sample_values):
    a, b = sample_values
    assert add(a, b) == 5
