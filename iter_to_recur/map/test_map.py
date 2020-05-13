import pytest
from map import map_iter, map_recur

@pytest.mark.parametrize('lst, expected', [
  ([2, 3, 4, 5], [4, 9, 16, 25])
])
def test_map_iter(lst, expected):
  def fn(i):
    return i ** 2
  actual = map_iter(lst, fn)
  assert actual == expected

@pytest.mark.parametrize('lst, expected', [
  ([2, 3, 4, 5], [4, 9, 16, 25])
])
def test_map_recur(lst, expected):
  def fn(i):
    return i ** 2
  actual = map_recur(lst, fn)
  assert actual == expected
