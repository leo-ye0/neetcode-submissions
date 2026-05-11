class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
        peak_index = 0
        for i in range(len(height)):
            if height[i] > height[peak_index]:
                peak_index = i
        ans = 0
        left_max = 0
        for i in range(peak_index):
            if height[i] > left_max:
                left_max = height[i]
            else:
                ans += left_max - height[i]
        right_max = 0
        for i in range(len(height) - 1, peak_index, -1):
            if height[i] > right_max:
                right_max = height[i]
            else:
                ans += right_max - height[i]
                
        return ans