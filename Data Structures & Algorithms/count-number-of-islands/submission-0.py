class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        def dfs(r, c):
            # Base Case: Out of bounds or hitting water
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            # "Sink" the land: Mark it as visited by changing it to '0'
            grid[r][c] = '0'
            
            # Explore all 4 neighbors (Up, Down, Left, Right)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c) # Sink the rest of this island
                    
        return island_count