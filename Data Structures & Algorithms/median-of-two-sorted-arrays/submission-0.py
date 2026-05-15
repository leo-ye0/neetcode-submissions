class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        while low <= high:
            partition1 = (low + high) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            # Edge cases: if partition is at the very beginning or end
            maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            minRight1 = nums1[partition1] if partition1 < m else float('inf')
            
            maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            minRight2 = nums2[partition2] if partition2 < n else float('inf')
            
            # Check if we found the perfect split
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Even total elements
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                # Odd total elements
                else:
                    return max(maxLeft1, maxLeft2)
            
            elif maxLeft1 > minRight2:
                # We are too far right in nums1, move left
                high = partition1 - 1
            elif maxLeft2 > minRight1:
                # We are too far left in nums1, move right
                low = partition1 + 1