class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        current_product = x
        
        while n > 0:
            # If n is odd, multiply the result by the current product
            if n % 2 == 1: #check binary rightmost if 1, update res, if 0 do not
                res *= current_product
            n //= 2    
            current_product *= current_product
            
            
        return res