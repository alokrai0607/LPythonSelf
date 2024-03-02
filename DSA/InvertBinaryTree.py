class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(root):
   
    if root is None:
        return None

    # Swap the left and right child nodes of the current node
   
    root.left, root.right = root.right, root.left


    # Recursively invert the left and right subtrees
   
    invert_binary_tree(root.left)
   
    invert_binary_tree(root.right)

    return root

# Example binary tree
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
# Inverted binary tree will be:
#         1
#       /   \
#      3     2
#     / \   / \
#    7   6 5   4

# Input binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Output: Inverted binary tree
inverted_root = invert_binary_tree(root)
