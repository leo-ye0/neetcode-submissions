class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        # Helper DFS to check if a path already exists between source and target
        def has_path(source, target, visited):
            if source == target:
                return True
            visited.add(source)
            for neighbor in adj[source]:
                if neighbor not in visited:
                    if has_path(neighbor, target, visited):
                        return True
            return False
            
        # Process left to right
        for u, v in edges:
            # If both nodes are already in our map, check if they are connected
            if u in adj and v in adj and has_path(u, v, set()):
                return [u, v]
                
            # If not connected yet, safely add the two-way edge to our map
            adj[u].append(v)
            adj[v].append(u)