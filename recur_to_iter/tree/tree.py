
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def num_tree_nodes_recur(tree_node):
  """
  Count tree nodes by recursion.
  """
  if not tree_node:
    return 0
  return 1 + num_tree_nodes_recur(tree_node.left) + num_tree_nodes_recur(tree_node.right)

def num_tree_nodes_iter(tree_node):
  """
  Count tree nodes by iteration.
  """
  if not tree_node:
    return 0
  s = 0
  queue = []
  queue.append(tree_node)
  while len(queue) > 0:
    cur = queue.pop()
    if cur.left:
      queue.append(cur.left)
    if cur.right:
      queue.append(cur.right)
    s += 1
  return s
