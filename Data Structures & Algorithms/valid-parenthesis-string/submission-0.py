class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            elif char == '*':
                min_open -= 1
                max_open += 1
                
            # Guard Rail 1: If max_open is negative, there are too many ')'
            if max_open < 0:
                return False
                
            # Guard Rail 2: min_open cannot be negative (we can't have "negative" open brackets)
            if min_open < 0:
                min_open = 0
                
        # The string is valid if we can perfectly achieve 0 open brackets at the end
        return min_open == 0