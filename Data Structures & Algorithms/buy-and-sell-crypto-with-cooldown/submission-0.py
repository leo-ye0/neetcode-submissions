class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Best Time to Buy and Sell Stock with Cooldown
        #hold: the maximum profit when you are holding a stock.
        #sold: the maximum profit when you have just sold a stock.
        #rest: the maximum profit when you are in rest/cooldown state.
        n=len(prices)
        hold = [0] * n
        sold = [0] * n
        rest = [0] * n
        hold[0] = -prices[0]
        for i in range(1, n):
            hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
            sold[i] = hold[i - 1] + prices[i]
            rest[i] = max(rest[i - 1], sold[i - 1])  
        return max(sold[-1], rest[-1])