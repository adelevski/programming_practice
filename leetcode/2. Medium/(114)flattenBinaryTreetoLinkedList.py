

# Due to the nature of this problem, it will not run in a personal environment

root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]

root = []
# Output: []

root = [0]
# Output: [0]

# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100

# Follow up: Can you flatten the tree in-place (with O(1) extra space)

# Hint 1: If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node: return None,None
            left,left2 = dfs(node.left)
            right,right2 = dfs(node.right)
            node.left = None
            end = node
            if left:
                end.right = left
                end = left2
            if right:
                end.right = right
                end = right2
            return node, end
        dfs(root)


        