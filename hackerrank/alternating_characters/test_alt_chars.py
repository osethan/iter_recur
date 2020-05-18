import pytest
from alt_chars import alternating_characters

@pytest.mark.parametrize('s, ss, expected', [
  ('AABAAB', 'ABAB', 2),
  ('AAA', 'A', 2),
  ('AAB', 'AB', 1),
  ('ABA', 'ABA', 0),
  ('ABB', 'AB', 1),
  ('AAAA', 'A', 3)
])
def test_alternating_characters(s, ss, expected):
  actual = alternating_characters(s)
  assert actual == expected
