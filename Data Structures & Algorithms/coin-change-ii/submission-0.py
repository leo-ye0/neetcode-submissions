class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #dp[i]=ways to make up amount i
        dp=[0]*(amount+1)
        dp[0]=1
        n=len(coins)
        for i in range(n-1,-1,-1):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        
        return dp[amount]