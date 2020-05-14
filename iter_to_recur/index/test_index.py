import pytest
from index import index_iter, index_recur

@pytest.mark.parametrize('lst, val, expected', [
  ([2, 3, 4, 5], 5, 3),
  ([2, 3, 4, 5], 7, -1)
])
def test_index_iter(lst, val, expected):
  actual = index_iter(lst, val)
  assert actual == expected

@pytest.mark.parametrize('lst, val, expected', [
  ([2, 3, 4, 5], 5, 3),
  ([2, 3, 4, 5], 7, -1)
])
def test_index_recur(lst, val, expected):
  actual = index_recur(lst, val)
  assert actual == expected
