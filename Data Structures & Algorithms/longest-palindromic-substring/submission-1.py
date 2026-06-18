class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            # Case 1: Odd length (Center is a single character)
            len1 = self.expand(s, i, i)
            # Case 2: Even length (Center is the gap between i and i+1)
            len2 = self.expand(s, i, i + 1)
            
            # Find the max of the two expansions
            max_len = max(len1, len2)
            
            # Update the global longest boundaries
            if max_len >= end - start+1:
                # Math to find new start/end from center i and total length
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start : end + 1]

    def expand(self, s, left, right):
        # Expand as long as pointers are in bounds and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Returns the length of the palindrome found
        return right - left - 1
        