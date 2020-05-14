import pytest
from fibonacci import fibonacci_iter, fibonacci_recur

@pytest.mark.parametrize('n, expected', [
  (7, 13)
])
def test_fibonacci_recur(n, expected):
  actual = fibonacci_recur(n)
  assert actual == expected

@pytest.mark.parametrize('n, expected', [
  (7, 13)
])
def test_fibonacci_iter(n, expected):
  actual = fibonacci_iter(n)
  assert actual == expected
