class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        rev = 0
        while x != 0:
            # Pop the rightmost digit
            digit = x % 10
            x //= 10
            
            # Check for overflow before multiplying by 10
            # Condition A: rev is already too large
            if rev > INT_MAX // 10:
                return 0
            # Condition B: rev is right on the edge, check the final digit
            if rev == INT_MAX // 10 and digit > 7:
                return 0
                
            # Safely perform the step
            rev = rev * 10 + digit
            
        return sign * rev