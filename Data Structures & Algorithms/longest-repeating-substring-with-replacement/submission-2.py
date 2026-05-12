class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        max_freq = 0
        left = 0
        
        for right in range(len(s)):
            # Update frequency of the incoming character
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            # Current window size is (right - left + 1)
            # If (window_size - max_freq) > k, we have too many replacements
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            
        return max_length