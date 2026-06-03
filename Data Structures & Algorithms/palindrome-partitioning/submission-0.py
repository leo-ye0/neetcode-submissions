class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        current_partition = []

        def is_palindrome(start: int, end: int) -> bool:
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(start_idx: int):
            # Base Case: If we've reached the end of the string, 
            # we found a completely valid partition layout.
            if start_idx >= len(s):
                res.append(current_partition[:])
                return

            # Explore all possible cutting points ahead of start_idx
            for end_idx in range(start_idx, len(s)):
                # If the substring from start_idx to end_idx is a palindrome
                if is_palindrome(start_idx, end_idx):
                    # 1. Choose: Add the palindrome substring to our current path
                    current_partition.append(s[start_idx:end_idx + 1])
                    
                    # 2. Explore: Recurse starting right after our cut point
                    backtrack(end_idx + 1)
                    
                    # 3. Unchoose: Backtrack and erase the choice to try the next cut
                    current_partition.pop()

        backtrack(0)
        return res