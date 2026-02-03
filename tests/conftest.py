import sys
from pathlib import Path
import pytest

# Add src to sys.path so tests can import the package without installing it
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

@pytest.fixture
def sample_values():
    return (2, 3)

@pytest.fixture
def db_conn():
    print("Setup DB")
    yield "db-connection"
    print("Teardown DB")
    
