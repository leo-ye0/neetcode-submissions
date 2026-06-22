class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if len(text1) < len(text2): self.longestCommonSubsequence(text2, text1)
        
        # Only track the previous/current row's data
        dp = [0] * (n + 1)
        
        for i in range(1, m + 1):
            prev_diagonal = 0  # Represents dp[i-1][j-1]
            
            for j in range(1, n + 1):
                temp = dp[j]  # Store the old value before overwriting it
                
                if text1[i - 1] == text2[j - 1]:
                    # Current match builds on top of the old diagonal
                    dp[j] = prev_diagonal + 1
                else:
                    # No match: take max of left (dp[j-1]) and above (old dp[j])
                    dp[j] = max(dp[j], dp[j - 1])
                    
                prev_diagonal = temp  # Update diagonal for the next column loop
                
        return dp[n]