class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Can the first i characters of s1 and the first j characters of s2 form the first i+j characters of s3
        # dp[i][j]
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(n + 1):
                # using a char from s1
                if i > 0 and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                
                # using a char from s2
                if j > 0 and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
                    
        return dp[m][n]