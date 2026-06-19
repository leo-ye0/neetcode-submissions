class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Build the Trie
        root = TrieNode()
        for word in wordDict:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
            
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True # Base case: empty string
        
        for i in range(n):
            if not dp[i]:
                continue
            
            # Start searching the Trie from the current valid index i
            node = root
            for j in range(i, n):
                if s[j] not in node.children:
                    break # No words in dictionary start with this prefix
                node = node.children[s[j]]
                if node.is_word:
                    dp[j + 1] = True
                    
        return dp[n]
        