class Solution:
    def countSubstrings(self, s: str) -> int:
        self.total_palindromes = 0
        
        for i in range(len(s)):
            self.expand(s, i, i)
            self.expand(s, i, i + 1)
            
        return self.total_palindromes

    def expand(self, s: str, left: int, right: int) -> None:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.total_palindromes += 1
            left -= 1
            right += 1