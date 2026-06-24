class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        
        # dp[j] stores the number of ways to form prefix t[0...j-1]
        dp = [0] * (m + 1)
        
        # Base Case: There is always 1 way to form an empty target string t
        dp[0] = 1 
        
        for i in range(1, n + 1):
        # Before starting the row, the "diagonal left" for the first element is dp[0]
            prev_diagonal = dp[0] 
            
            for j in range(1, m + 1):
                # 1. Back up the current value before it gets overwritten.
                # This will become the "prev_diagonal" for the NEXT element (j + 1)
                next_diagonal = dp[j]
                
                if s[i - 1] == t[j - 1]:
                    # dp[j] is the old "Up" value
                    # prev_diagonal is the old "Top-Left Diagonal" value
                    dp[j] = dp[j] + prev_diagonal
                else:
                    # Mismatch: dp[j] stays as it was, but we still updated its state
                    pass
                
                # 2. Shift our tracking variable forward for the next iteration
                prev_diagonal = next_diagonal
                        
        return dp[m]