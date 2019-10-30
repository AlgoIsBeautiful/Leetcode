class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        visited = set()
        self.backtrack(nums, visited, [])
        return self.res
    
    
    def backtrack(self, nums, visited, curr):
        
        if len(curr) == len(nums):
            self.res.append(curr[:])
        
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            else:
                visited.add(nums[i])
                self.backtrack(nums, visited, curr+[nums[i]])
                visited.remove(nums[i])


'''
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''