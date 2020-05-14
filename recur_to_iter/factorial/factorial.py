
def factorial_recur(n):
  """
  Find factorial by recursion.
  """
  if n <= 1:
    return 1
  return n * factorial_recur(n - 1)

def factorial_iter(n):
  """
  Find factorial by iteration.
  """
  k = 1
  while n > 1:
    k *= n
    n -= 1
  return k
