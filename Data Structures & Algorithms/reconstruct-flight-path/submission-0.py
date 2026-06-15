class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        
        # Sort tickets in reverse alphabetical order.
        # This lets us pop from the end of the list in O(1) time 
        # while still getting the alphabetically smallest airport first!
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
            
        route = []
        
        def dfs(airport):
            while adj[airport]:
                next_destination = adj[airport].pop()
                dfs(next_destination)
            
            # If we get here, this airport has NO outgoing flights left.
            # It's either a dead-end or we used all its tickets. Record it!
            route.append(airport)
            
        dfs("JFK")
        
        # Since it's post-order, the route is backward. Reverse it!
        return route[::-1]