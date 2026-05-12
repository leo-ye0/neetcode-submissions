class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        s1_counts = [0] * 26
        window_counts = [0] * 26
        
        # Initial count for s1 and the first window of s2
        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            window_counts[ord(s2[i]) - ord('a')] += 1
            
        if s1_counts == window_counts:
            return True
            
        # Slide the window across s2
        for i in range(n1, n2):
            # Add the new character (right side)
            window_counts[ord(s2[i]) - ord('a')] += 1
            # Remove the old character (left side)
            window_counts[ord(s2[i - n1]) - ord('a')] -= 1
            if s1_counts == window_counts:
                return True
                
        return False