import pytest
from isvalid import isvalid

@pytest.mark.parametrize('s, expected', [
  ('abbac', 'YES'),
  ('aabbcd', 'NO'),
  ('aabbccddeefghi', 'NO'),
  ('abcdefghhgfedecba', 'YES')
])
def test_isvalid(s, expected):
  actual = isvalid(s)
  assert actual == expected
