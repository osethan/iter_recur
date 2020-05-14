import pytest
from tree import num_tree_nodes_iter, num_tree_nodes_recur, TreeNode

@pytest.mark.parametrize('expected', [(5)])
def test_num_tree_nodes_recur(expected):
  tree_node = TreeNode(2)
  tree_node.left = TreeNode(3)
  tree_node.right = TreeNode(4)
  tree_node.left.left = TreeNode(5)
  tree_node.left.right = TreeNode(7)

  actual = num_tree_nodes_recur(tree_node)
  assert actual == expected

@pytest.mark.parametrize('expected', [(5)])
def test_num_tree_nodes_iter(expected):
  tree_node = TreeNode(2)
  tree_node.left = TreeNode(3)
  tree_node.right = TreeNode(4)
  tree_node.left.left = TreeNode(5)
  tree_node.left.right = TreeNode(7)

  actual = num_tree_nodes_iter(tree_node)
  assert actual == expected
