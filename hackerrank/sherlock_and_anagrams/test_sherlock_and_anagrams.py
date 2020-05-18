import pytest
from sherlock_and_anagrams import sherlock_and_anagrams, substring_anagrams, substring_anagrams_iter

@pytest.mark.parametrize('s, expected', [
  ('abba', 4),
  ('abcd', 0),
  ('kkkk', 10),
  ('cdcd', 5)
])
def test_substring_anagrams(s, expected):
  actual = substring_anagrams(s, (0, 1), set())
  assert actual == expected

@pytest.mark.parametrize('s, expected', [
  ('abba', 4),
  ('abcd', 0),
  ('kkkk', 10),
  ('cdcd', 5),
  # ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 166650)
])
def test_substring_anagrams_iter(s, expected):
  actual = substring_anagrams_iter(s)
  assert actual == expected

@pytest.mark.parametrize('s, expected', [
  ('abba', 4),
  ('abcd', 0),
  ('kkkk', 10),
  ('cdcd', 5),
  ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 166650)
])
def test_sherlock_and_anagrams(s, expected):
  actual = sherlock_and_anagrams(s)
  assert actual == expected
