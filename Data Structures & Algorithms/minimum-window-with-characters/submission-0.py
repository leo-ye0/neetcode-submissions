class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        l, r = 0, 0
        # formed is used to keep track of how many unique characters in t are 
        # present in the current window in its desired frequency.
        formed = 0
        window_counts = {} # A map of what we currently have in our window
        # ans tuple of (window length, left, right)
        ans = float("inf"), None, None
        while r < len(s):
            # r (right) pointer moves forward
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the frequency of the current character added equals to the 
            # desired count in t then increment the formed count.
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'valid'.
            while l <= r and formed == required:
                # Save the smallest window until now
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window
                char = s[l]
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                # Move the left pointer ahead, this helps in look for a new window.
                l += 1    

            # Keep expanding the window by moving the right pointer
            r += 1    
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]