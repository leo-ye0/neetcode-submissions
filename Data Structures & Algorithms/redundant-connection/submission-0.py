class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) # Path compression
            return parent[i]
            
        # Process from left to right
        for u, v in edges:
            root_u = find(u)
            root_v = find(v)
            
            # If they have the same root, they are already connected!
            # Adding this edge creates the cycle.
            if root_u == root_v:
                return [u, v]
                
            # Otherwise, safely merge them
            parent[root_u] = root_v