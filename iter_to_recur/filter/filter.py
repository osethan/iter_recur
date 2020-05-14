
def filter_iter(lst, fn):
  """
  Filter a list by iteration.
  """
  fltr = []
  i = 0
  while i < len(lst):
    if fn(lst[i]):
      fltr.append(lst[i])
    i += 1
  return fltr

def filter_recur(lst, fn):
  """
  Filter a list by recursion.
  """
  def helper(i, fltr):
    if i >= len(lst):
      return fltr
    if fn(lst[i]):
      fltr.append(lst[i])
    i += 1
    return helper(i, fltr)
  return helper(0, [])
