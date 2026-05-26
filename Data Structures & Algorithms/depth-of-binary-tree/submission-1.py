# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        queue = deque([root])
        depth = 0
        
        while queue:
            # Every time we enter this loop, we are at a new level
            depth += 1
            level_size = len(queue)
            
            # Process every node currently at THIS level
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return depth