class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base Case: Empty string matches empty pattern
        dp[0][0] = True
        
        # Initialize Row 0 (Empty string matching patterns with '*')
        for j in range(2, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
                
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    # Choice 1: Match 0 occurrences of the preceding element
                    match_zero = dp[i][j-2]
                    
                    # Choice 2: Match 1 or more occurrences (if characters align)
                    match_one_or_more = False
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        match_one_or_more = dp[i-1][j]
                        
                    dp[i][j] = match_zero or match_one_or_more
                else:
                    # Current characters must match or pattern must be a '.'
                    if p[j-1] == s[i-1] or p[j-1] == '.':
                        dp[i][j] = dp[i-1][j-1]
                        
        return dp[m][n]