'''
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.backtrack(nums, [], 0)
        return self.res
    
    def backtrack(self, nums, curr, index):
        
        self.res.append(curr[:])
        
        for i in range(index, len(nums)):
            curr.append(nums[i])
            self.backtrack(nums, curr, i+1)
            curr.pop()