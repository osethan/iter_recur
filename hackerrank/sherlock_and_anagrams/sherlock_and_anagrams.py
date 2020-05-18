from collections import Counter
from itertools import combinations


def sherlock_and_anagrams(s):
  """
  Given a string, find the number of pairs of substrings which are anagrams of each other.
  * Answer assisted by HackerRank Sherlock and Anagrams Discussion
  """
  
  # Get all substrings sorted
  substrs = tuple()
  for i in range(1, len(s) + 1): # i, len+1 to include full string
    for j in range(len(s) - i + 1): # j, len-i+1 to include last check
      substrs += (''.join(sorted(s[j:j + i])),)

  # Count the number of substrings sorted
  b = Counter(substrs)

  # Count the number of ways to choose two matching sorted substrings
  k = 0
  for key in b.keys():
    k += len(list(combinations(['a'] * b[key], 2)))
  
  return k


# def substring_anagrams(s, idx, seen):
#   """
#   Count substring anagrams by recursion.
#   """
#   if idx[1] > len(s):
#     return 0
#   if idx in seen:
#     return 0

#   anagrams = 0
#   for pair in seen:
#     if is_anagram(s[idx[0]:idx[1]], s[pair[0]:pair[1]]):
#       anagrams += 1
#   seen.add(idx)

#   idx_left = (idx[0] + 1, idx[1] + 1)
#   idx_right = (idx[0], idx[1] + 1)
#   anagrams += substring_anagrams(s, idx_left, seen) + substring_anagrams(s, idx_right, seen)
#   return anagrams


# def substring_anagrams_iter(s):
#   """
#   Count substring anagrams by iteration.
#   """
#   idx = (0, 1)
#   seen = set()
#   anagrams = 0
#   queue = []
#   queue.append(idx)
#   while len(queue) > 0:
#     cur = queue.pop()
#     if cur[1] > len(s):
#       continue
#     if cur in seen:
#       continue

#     for pair in seen:
#       if is_anagram(s[cur[0]:cur[1]], s[pair[0]:pair[1]]):
#         anagrams += 1
#     seen.add(cur)

#     cur_left = (cur[0] + 1, cur[1] + 1)
#     cur_right = (cur[0], cur[1] + 1)
#     queue.append(cur_left)
#     queue.append(cur_right)
#   return anagrams


# def is_anagram(s1, s2):
#   """
#   Two strings are anagrams.
#   """
#   s1_counter = {}
#   for c in s1:
#     if c in s1_counter:
#       s1_counter[c] += 1
#     else:
#       s1_counter[c] = 1
  
#   s2_counter = {}
#   for c in s2:
#     if c in s2_counter:
#       s2_counter[c] += 1
#     else:
#       s2_counter[c] = 1

#   for k in s1_counter.keys():
#     if k not in s2_counter or s1_counter[k] != s2_counter[k]:
#       return False

#   for k in s2_counter.keys():
#     if k not in s1_counter or s2_counter[k] != s1_counter[k]:
#       return False

#   return True
