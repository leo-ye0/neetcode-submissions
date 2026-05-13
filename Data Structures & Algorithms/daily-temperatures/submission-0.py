class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n  # Initialize result array with 0s
        stack = []        # This will store indices
        
        for i, temp in enumerate(temperatures):
            # Resolve earlier days that are cooler than the current day's temperature
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            
            stack.append(i) # Push the current day index onto the stack
            
        return result