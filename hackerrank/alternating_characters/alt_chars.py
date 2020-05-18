
def alternating_characters(s):
  ss = s[0]
  for i in range(1, len(s)):
    if s[i] == ss[-1]:
      continue
    ss += s[i]
  return len(s) - len(ss)

def alternating_characters_one(s):
  """
  Remove matching adjacent chars from a str.
  """
  i = 0
  ss = ''
  while i < len(s)-1:
    ss += s[i]
    if s[i] == s[i+1]:
      i += 2
    else:
      i += 1
  if ss[-1] != s[-1]:
    ss += s[-1]
  return len(s) - len(ss)
