class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        input = [x for x in range(1, n+1)]
        self.k = k
        self.res = []
        self.backtrack(input, [], 0)
        return self.res
        
    def backtrack(self, input, temp, first):
        if len(temp) == self.k:
            self.res.append(temp[:])
            return
        for i in range(first, len(input)):
            # small piece adding
            temp.append(input[i])
            
            # backtracking
            self.backtrack(input, temp, i+1)
            
            # pop()
            temp.pop()