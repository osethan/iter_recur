
def index_iter(lst, val):
  """
  Find list value index by iteration.
  """
  i = 0
  while i < len(lst):
    if val == lst[i]:
      return i
    i += 1
  return -1

def index_recur(lst, val):
  """
  Find list value index by recursion.
  """
  def helper(i):
    if i >= len(lst):
      return -1
    if val == lst[i]:
      return i
    i += 1
    return helper(i)
  return helper(0)
