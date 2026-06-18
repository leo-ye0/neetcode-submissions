class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        ans=[0,0]
        for i in range(n):
            dp[i][i] = True
            #check length 2
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                ans=[i,i+1]
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j=i+length-1
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    ans=[i,j]
        start, end = ans
        return s[start:end + 1]