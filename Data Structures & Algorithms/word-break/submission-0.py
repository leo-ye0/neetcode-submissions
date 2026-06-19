class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #define dp[i] as True if the substring s[0:i] can be segmented into words from wordDict.
        #i is length
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):  # Check all substrings ending at i
            for j in range(i):  # Try all possible break points
                if dp[j] and s[j:i] in wordSet:  # If s[j:i] is a valid word
                    dp[i] = True
                    break
        return dp[n]