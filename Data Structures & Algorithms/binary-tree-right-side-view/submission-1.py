# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def dfs(node, depth):
            if not node:
                return
            
            # If this is the first time we've reached this depth, 
            # this node is the rightmost one.
            if depth == len(result):
                result.append(node.val)
            
            # ALWAYS visit right first to ensure it's the first one seen at each depth
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            
        dfs(root, 0)
        return result