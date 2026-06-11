class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
            
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        
        # Step 1: Add all gates to the queue to start multi-source BFS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    
        # Step 2: Step outward level-by-level
        while queue:
            r, c = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
                    # Update distance in-place
                    grid[nr][nc] = grid[r][c] + 1
                    # Enqueue the neighbor so it can expand to its neighbors
                    queue.append((nr, nc))