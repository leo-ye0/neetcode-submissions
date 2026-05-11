class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        left=0
        seen = {}
        for right in range(len(s)):
            char = s[right]
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            max_len = max(max_len, right - left + 1)
        return max_len
            