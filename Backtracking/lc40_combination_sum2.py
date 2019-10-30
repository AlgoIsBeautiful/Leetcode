class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if len(candidates) == 0 and target == 0:
            return []
        self.res = []
        candidates.sort()
        self.backtrack(candidates, target, [], 0) 
        return self.res
    
    
    def backtrack(self, candidates, target, curr, index):
        
        if sum(curr) == target and (curr not in self.res):
            self.res.append(curr[:])
            return 
        
        for i in range(index, len(candidates)):
            
            if (sum(curr) + candidates[i]) > target:
                break
            
            else:
                curr.append(candidates[i])
                self.backtrack(candidates, target, curr, i+1)
                curr.pop()