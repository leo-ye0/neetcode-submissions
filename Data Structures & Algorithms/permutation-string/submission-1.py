class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        s1_counts = Counter(s1)
        # Initialize window with first n1 chars
        window_counts = Counter(s2[:n1])
        
        if s1_counts == window_counts:
            return True
            
        for i in range(n1, n2):
            # Add RHS
            window_counts[s2[i]] += 1
            # Remove LHS
            window_counts[s2[i - n1]] -= 1
            # Counter clean up: If count is 0, remove key to keep comparison accurate
            if window_counts[s2[i - n1]] == 0:
                del window_counts[s2[i - n1]]
                
            if s1_counts == window_counts:
                return True
        return False