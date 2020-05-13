import pytest
from max import max_iter, max_recur

@pytest.mark.parametrize('lst, expected', [
  ([2, 3, 4, 5], 5)
])
def test_max_iter(lst, expected):
  actual = max_iter(lst)
  assert actual == expected

@pytest.mark.parametrize('lst, expected', [
  ([2, 3, 4, 5], 5)
])
def test_max_recur(lst, expected):
  actual = max_recur(lst)
  assert actual == expected
