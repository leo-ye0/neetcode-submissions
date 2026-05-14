class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # Dummy bar to force final pops avoid strictly increasing
        stack = [-1]       # Initialize with -1 to handle width calculation
        max_area = 0
        
        for i in range(len(heights)):
            # While current height is less than the top of the stack
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
            
        return max_area