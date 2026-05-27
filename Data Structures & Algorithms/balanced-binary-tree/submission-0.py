# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0  # Base Case: An empty node has a height of 0
            
            # 1. Check the left subtree
            left_height = dfs(node.left)
            if left_height == -1: 
                return -1  # Left side is already broken! Pass the error up.
                
            # 2. Check the right subtree
            right_height = dfs(node.right)
            if right_height == -1: 
                return -1  # Right side is already broken! Pass the error up.
            
            # 3. Check the current node's balancing condition
            if abs(left_height - right_height) > 1:
                return -1  # The scale tipped! Return our custom error code (-1).
                
            # 4. If perfectly balanced, return the actual height normally
            return 1 + max(left_height, right_height)
            
        # If the master root returns -1, it means the tree is unbalanced
        return dfs(root) != -1