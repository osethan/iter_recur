
def map_iter(lst, fn):
  """
  Map list values by iteration.
  """
  map = []
  i = 0
  while i < len(lst):
    map.append(fn(lst[i]))
    i += 1
  return map

def map_recur(lst, fn):
  """
  Map list values by recursion.
  """
  def helper(i, map):
    if i >= len(lst):
      return map
    map.append(fn(lst[i]))
    i += 1
    return helper(i, map)
  return helper(0, [])
