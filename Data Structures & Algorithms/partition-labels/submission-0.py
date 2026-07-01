class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indices = {}
        for idx, char in enumerate(s):
            last_indices[char] = idx
        result = []
        start = 0
        end = 0
        
        # Step 2: Slide through the string and make greedy cuts
        for idx, char in enumerate(s):
            # Expand our horizon to include the last copy of the current character
            end = max(end, last_indices[char])
            
            # If we've reached the furthest horizon, make a cut!
            if idx == end:
                # Calculate the size of the current substring partition
                partition_size = end - start + 1
                result.append(partition_size)
                
                # Move the start pointer to the beginning of the next partition
                start = idx + 1
                
        return result