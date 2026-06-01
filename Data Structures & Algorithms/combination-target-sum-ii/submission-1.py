class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(remain, start, path):
            # Base Case 1: We hit the target exactly
            if remain == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remain:
                    break
                path.append(candidates[i])
                backtrack(remain - candidates[i], i+1, path)
                path.pop()

        backtrack(target, 0, [])
        return res