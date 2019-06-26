class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        self.dfs(nums, 0, [])
        return self.result
    
    def dfs(self, nums, index, combination):
        self.result.append(combination[:])
        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i+1, combination)
            combination.pop()