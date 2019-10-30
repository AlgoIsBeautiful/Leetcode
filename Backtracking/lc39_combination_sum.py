'''
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

'''

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