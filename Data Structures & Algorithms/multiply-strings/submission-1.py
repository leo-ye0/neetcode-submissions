class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"
            
        m, n = len(num1), len(num2)
        # Array to store the digits of the final result
        result = [0] * (m + n)
        
        # Loop backwards through both strings (from rightmost digit to leftmost)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply single digit characters converted to small integers
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Add product to the current position in the result array
                p1 = i + j      # Carry position
                p2 = i + j + 1  # Current position
                
                total_sum = mul + result[p2]
                
                # Update positions with carry handling
                result[p2] = total_sum % 10
                result[p1] += total_sum // 10
                
        # Convert the digit array back to a string, skipping leading zeros
        start_idx = 0
        while start_idx < len(result) and result[start_idx] == 0:
            start_idx += 1
            
        return "".join(map(str, result[start_idx:]))