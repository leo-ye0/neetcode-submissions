class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)  # Remove the last '1'
            count += 1
        return count