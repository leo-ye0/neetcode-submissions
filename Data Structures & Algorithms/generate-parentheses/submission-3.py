class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        current_list=[]
        
        def backtrack(open_count, close_count):
            if len(current_list) == 2 * n:
                res.append("".join(current_list))
                return
            
            if open_count < n:
                current_list.append("(") # 1. Choose
                backtrack(open_count + 1, close_count) # 2. Explore
                current_list.pop() # 3. Unchoose
                
            if close_count < open_count:
                current_list.append(")") # 1. Choose
                backtrack(open_count, close_count + 1) # 2. Explore
                current_list.pop() # 3. Unchoose
                
        backtrack(0, 0)
        return res