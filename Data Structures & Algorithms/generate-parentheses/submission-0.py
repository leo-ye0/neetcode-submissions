class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(current_str, open_count, close_count):
            if len(current_str) == 2 * n:
                res.append(current_str)
                return
            
            # Rule 1: We can always add an opening bracket if we haven't used all n
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
            
            # Rule 2: We can only add a closing bracket if it "matches" an open one
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
                
        backtrack("", 0, 0)
        return res