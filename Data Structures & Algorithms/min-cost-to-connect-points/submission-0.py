class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0
            
        # Min-heap stores tuples of (edge_cost, point_index)
        # We start arbitrarily at point 0 with a cost of 0
        min_heap = [(0, 0)]
        visited = set()
        total_cost = 0
        
        while len(visited) < n:
            cost, curr_node = heapq.heappop(min_heap)
            
            # If the point is already part of our tree, skip it
            if curr_node in visited:
                continue
                
            # Bring this point into our tree
            visited.add(curr_node)
            total_cost += cost
            
            # Calculate distances to all other unvisited points
            curr_x, curr_y = points[curr_node]
            for next_node in range(n):
                if next_node not in visited:
                    next_x, next_y = points[next_node]
                    # Manhattan distance formula
                    manhattan_dist = abs(curr_x - next_x) + abs(curr_y - next_y)
                    heapq.heappush(min_heap, (manhattan_dist, next_node))
                    
        return total_cost