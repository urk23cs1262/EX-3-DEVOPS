import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import multiply

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(5, 0) == 0