'''
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        self.res = []
        input = [x for x in range(1,10)]
        self.k = k
        self.n = n
        self.backtrack(input, [], 0) 
        return self.res
    
    
    def backtrack(self, input, curr, index):
        
        if len(curr) == self.k and sum(curr) == self.n and (curr not in self.res):
            self.res.append(curr[:])
            return 
        
        for i in range(index, len(input)):
            
            if (sum(curr) + input[i]) > self.n:
                break
            else:
                curr.append(input[i])
                self.backtrack(input, curr, i+1)
                curr.pop()