from mypackage import add, divide
import pytest

from src.mypackage.calculator import app


def test_add_direct():
    print("test_add_direct")
    assert add(2, 3) == 5


def test_add_with_fixture(sample_values):
    print("test_add_direct2")
    a, b = sample_values
    assert add(a, b) == 5

def test_db(db_conn):
    print("test_db")
    assert db_conn == "db-connection"
    
@pytest.mark.parametrize(
    "a,b,expected",
    [(1,2,3), (5,5,10), (10,-5,5)]
)
def test_add(a, b, expected):
    assert a + b == expected
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        assert divide(10, 0)

def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200