class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Identify which half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 # Target is in the sorted left
                else:
                    left = mid + 1  # Target is in the right
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target is in the sorted right
                else:
                    right = mid - 1 # Target is in the left
                    
        return -1