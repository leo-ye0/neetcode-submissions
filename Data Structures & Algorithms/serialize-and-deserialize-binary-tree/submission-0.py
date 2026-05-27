# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
            
        vals = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if not node:
                vals.append('#')
                continue
                
            vals.append(str(node.val))
            # BFS Rule: Always queue up left and right children blindly, 
            # even if they are None!
            queue.append(node.left)
            queue.append(node.right)
            
        return ",".join(vals)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
            
        vals = data.split(',')
        root = TreeNode(int(vals[0]))
        
        # This queue holds physical nodes that are waiting for their children
        queue = deque([root])
        
        # A simple pointer to track our location on the flat data list
        idx = 1  
        
        while queue:
            parent = queue.popleft()
            
            # 1. Process the Left Child
            if vals[idx] != '#':
                parent.left = TreeNode(int(vals[idx]))
                queue.append(parent.left) # Queue it up so it can get its own kids later
            idx += 1
            
            # 2. Process the Right Child
            if vals[idx] != '#':
                parent.right = TreeNode(int(vals[idx]))
                queue.append(parent.right) # Queue it up so it can get its own kids later
            idx += 1
            
        return root