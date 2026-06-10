"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old_to_new = {}
        def dfs(node):
            # If we've already cloned this node, return the clone
            if node in old_to_new:
                return old_to_new[node]
            
            # 1. Create the copy
            copy = Node(node.val)
            old_to_new[node] = copy
            
            # 2. Recursively clone all neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node)