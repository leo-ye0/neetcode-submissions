# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')  # Global maximum path sum

        def dp(node):
            if not node:
                return 0

            # Recursively calculate max gain from left/right subtrees
            left_gain = max(dp(node.left), 0)
            right_gain = max(dp(node.right), 0)

            # Local path: left → node → right
            current_path = node.val + left_gain + right_gain

            # Update global result if this path is better
            self.max_sum = max(self.max_sum, current_path)

            # Return max gain from this node to its parent (choose one side)
            return node.val + max(left_gain, right_gain)

        dp(root)
        return self.max_sum
