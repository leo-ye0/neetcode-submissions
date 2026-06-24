from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        m, n = len(matrix), len(matrix[0])
        
        # dp(i, j) calculates the longest path starting from (i, j)
        @lru_cache(None)
        def dfs(i, j):
            max_path = 1  # Base case: a single cell has a path length of 1
            
            # Explore all 4 cardinal directions: up, down, left, right
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                
                # Check boundaries AND ensure the next cell is strictly INCREASING
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    max_path = max(max_path, 1 + dfs(ni, nj))
                    
            return max_path

        # Test every single cell as a starting point and find the global maximum
        return max(dfs(r, c) for r in range(m) for c in range(n))