class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        if m < n:
            s1, s2 = s2, s1
            m, n = n, m
            
        # dp[j] now scales to the length of the smaller string (n)
        dp = [False] * (n + 1)
        dp[0] = True  
        
        # Pre-calculate Row 0 using the optimized shorter string s2
        for j in range(1, n + 1):
            dp[j] = (dp[j-1] and s2[j-1] == s3[j-1])
            
        # Process the remaining rows
        for i in range(1, m + 1):
            # Update Column 0 for the current row i
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            
            for j in range(1, n + 1):
                # Choice 1: Look up (history from the longer string s1)
                from_s1 = dp[j] and s1[i-1] == s3[i+j-1]
                
                # Choice 2: Look left (history from the shorter string s2)
                from_s2 = dp[j-1] and s2[j-1] == s3[i+j-1]
                
                dp[j] = from_s1 or from_s2
                
        return dp[n]