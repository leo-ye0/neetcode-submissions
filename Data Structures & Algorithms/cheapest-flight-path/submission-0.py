class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        
        # We can take at most k stops, which means up to k + 1 flights
        for _ in range(k + 1):
            # Create a snapshot copy of the prices array from the previous round.
            # This prevents "chaining" flights within the same step loop.
            temp_prices = list(prices)
            
            for u, v, price in flights:
                # If we haven't even reached airport 'u' yet, skip this flight
                if prices[u] == float('inf'):
                    continue
                
                # If traveling from u to v is cheaper than what v currently has recorded,
                # update our temporary tracker.
                if prices[u] + price < temp_prices[v]:
                    temp_prices[v] = prices[u] + price
            
            # Commit this round's optimal prices back into our main array
            prices = temp_prices
            
        return prices[dst] if prices[dst] != float('inf') else -1