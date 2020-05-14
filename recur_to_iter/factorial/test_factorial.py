import pytest
from factorial import factorial_iter, factorial_recur

@pytest.mark.parametrize('n, expected', [
  (5, 120)
])
def test_factorial_recur(n, expected):
  actual = factorial_recur(n)
  assert actual == expected

@pytest.mark.parametrize('n, expected', [
  (5, 120)
])
def test_factorial_iter(n, expected):
  actual = factorial_iter(n)
  assert actual == expected
