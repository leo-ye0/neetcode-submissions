class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        ROWS, COLS = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, reachable_set, prev_height):
            # If out of bounds, already visited, or water can't flow uphill from prev_height
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
                (r, c) in reachable_set or heights[r][c] < prev_height):
                return
                
            # Mark this cell as able to reach the ocean
            reachable_set.add((r, c))
            
            # Walk to 4 neighbors, passing current height as the "previous height"
            dfs(r + 1, c, reachable_set, heights[r][c])
            dfs(r - 1, c, reachable_set, heights[r][c])
            dfs(r, c + 1, reachable_set, heights[r][c])
            dfs(r, c - 1, reachable_set, heights[r][c])

        # Step 1: Start DFS from Pacific (Top/Left) and Atlantic (Bottom/Right) horizontal borders
        for c in range(COLS):
            dfs(0, c, pacific_reachable, heights[0][c])             # Top Row (Pacific)
            dfs(ROWS - 1, c, atlantic_reachable, heights[ROWS - 1][c]) # Bottom Row (Atlantic)
            
        # Step 2: Start DFS from Pacific (Top/Left) and Atlantic (Bottom/Right) vertical borders
        for r in range(ROWS):
            dfs(r, 0, pacific_reachable, heights[r][0])             # Left Column (Pacific)
            dfs(r, COLS - 1, atlantic_reachable, heights[r][COLS - 1]) # Right Column (Atlantic)
            
        # Step 3: Find the intersection of both reachable sets
        common_cells = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    common_cells.append([r, c])
                    
        return common_cells