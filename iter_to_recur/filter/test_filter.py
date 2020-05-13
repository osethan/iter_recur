import pytest
from filter import filter_iter, filter_recur

@pytest.mark.parametrize('lst, expected', [
  ([2, 3, 4, 5], [2, 4])
])
def test_filter_iter(lst, expected):
  def fn(i):
    return i % 2 == 0
  actual = filter_iter(lst, fn)
  assert actual == expected

@pytest.mark.parametrize('lst, expected', [
  ([2, 3, 4, 5], [2, 4])
])
def test_filter_recur(lst, expected):
  def fn(i):
    return i % 2 == 0
  actual = filter_recur(lst, fn)
  assert actual == expected
