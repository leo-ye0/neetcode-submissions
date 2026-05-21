# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case 1: Both are structural dead-ends (None) -> Match!
        if not p and not q:
            return True
            
        # Base Case 2: One is empty and the other isn't -> Mismatch!
        if not p or not q:
            return False
            
        # Base Case 3: Both exist, but have different data -> Mismatch!
        if p.val != q.val:
            return False
            
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)