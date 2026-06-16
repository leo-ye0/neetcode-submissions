class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        # Min-Heap stores: (max_elevation_so_far, row, col)
        # We start at (0, 0), so the initial cost is the elevation of (0, 0)
        min_heap = [(grid[0][0], 0, 0)]
        
        visited = set()
        visited.add((0, 0))
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while min_heap:
            current_time, r, c = heapq.heappop(min_heap)
            
            # The moment we pop the bottom-right cell, we are done!
            if r == n - 1 and c == n - 1:
                return current_time
                
            # Check all 4 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and ensure neighbor hasn't been visited
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    
                    # The cost to swim into the neighbor is the maximum of:
                    # 1. The highest water level we've had to endure so far
                    # 2. The elevation of the neighbor cell itself
                    next_time = max(current_time, grid[nr][nc])
                    
                    heapq.heappush(min_heap, (next_time, nr, nc))