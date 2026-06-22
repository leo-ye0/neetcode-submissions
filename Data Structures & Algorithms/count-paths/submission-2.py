class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n  # Only store one row
        
        for _ in range(m - 1):  # Iterate over rows
            for j in range(1, n):  # Update from left to right
                dp[j] += dp[j - 1]  # Paths from left + above (previous row)
        
        return dp[n-1]