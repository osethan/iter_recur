
def fibonacci_recur(n):
  """
  Fibonacci by recurion.
  """
  if n <= 1:
    return n
  return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)

def fibonacci_iter(n):
  """
  Fibonacci by iteration.
  """
  a = 0
  b = 1
  s = 0
  i = 1
  while i < n:
    s = a + b
    a = b
    b = s
    i += 1
  return s
