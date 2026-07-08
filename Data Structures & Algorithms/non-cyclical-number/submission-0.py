class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            sum_sq = 0
            for digit in str(n):
                sum_sq += int(digit) ** 2
            n = sum_sq
            
        return True
