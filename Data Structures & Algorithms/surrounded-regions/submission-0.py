class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        def dfs(r, c):
            # Base case: out of bounds or not an 'O'
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            # Mark as Safe
            board[r][c] = 'S'
            # Explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for r in range(rows):
            dfs(r, 0)           # Left Column
            dfs(r, cols - 1)    # Right Column

        # STEP 2: Scan ONLY the top and bottom horizontal borders
        for c in range(cols):
            dfs(0, c)           # Top Row
            dfs(rows - 1, c)    # Bottom Row

        

        # STEP 3: Final pass to flip the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    # This 'O' was never reached by DFS, so it must be surrounded
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    # This was a safe 'O', restore its original value
                    board[r][c] = 'O'