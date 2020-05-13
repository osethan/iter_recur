
def max_iter(lst):
  """
  Find max of list by iteration.
  """
  x = lst[0]
  i = 1
  while i < len(lst):
    if x < lst[i]:
      x = lst[i]
    i += 1
  return x

def max_recur(lst):
  """
  Find max of list by recursion.
  """
  def helper(i, x):
    if i >= len(lst):
      return x
    if x < lst[i]:
      x = lst[i]
    i += 1
    return helper(i, x)
  return helper(1, lst[0])
