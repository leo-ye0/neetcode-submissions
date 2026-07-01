class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        target_x, target_y, target_z = target
        
        # Track whether we've found a safe triplet that provides the exact x, y, and z we need
        found_x = False
        found_y = False
        found_z = False
        
        for a, b, c in triplets:
            # RULE: If any value is bigger than the target, this triplet is poison. Skip it!
            if a > target_x or b > target_y or c > target_z:
                continue
            
            # If it's safe, see if it contributes the exact value we need for any position
            if a == target_x:
                found_x = True
            if b == target_y:
                found_y = True
            if c == target_z:
                found_z = True
                
            # Optimization: If we found matches for all three positions, we can stop early!
            if found_x and found_y and found_z:
                return True
                
        return found_x and found_y and found_z