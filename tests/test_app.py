from app import multiply

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(5, 0) == 0