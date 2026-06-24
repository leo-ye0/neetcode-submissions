class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #dp[i][j]=min steps transform first i letter of 1 to first j of 2
        s,t = len(word1),len(word2)
        dp=[[0]*(t+1) for _ in range(s+1)]
        for i in range(1,s+1):
            dp[i][0]=i
        for j in range(1,t+1):
            dp[0][j]=j
        for i in range(1,s+1):
            for j in range(1,t+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])+1
        return dp[s][t]
# Delete word1[i-1] (dp[i-1][j]). now compute
# Insert word1[j-1] (dp[i][j-1]).
# Replace word1[i-1] with word2[j-1] (dp[i-1][j-1]).
# word1=a, word2=aq