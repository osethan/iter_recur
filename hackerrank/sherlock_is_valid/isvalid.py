from collections import Counter

def isvalid(s):
  """
  A string is valid if
  1) Chars appear the same num of times
  2) Remove one char means chars appear the same num of times

  In:
  s (str)

  Out:
  (str): 'YES' for valid, 'NO' for invalid
  """
  b = Counter(s)
  lst = list(b.values())
  if len(set(lst)) == 1:
    return 'YES'

  vmax = max(lst)
  lst.remove(vmax)
  if len(set(lst)) == 1 and lst[0] == vmax - 1:
    return 'YES'

  return 'NO'
