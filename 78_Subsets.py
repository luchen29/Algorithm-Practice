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

# another method:
#[]
#[1] []
#[1,2] [1] [2] []
#[1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []
class Solution(object):
    def subsets(self, nums):
        """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
        if not nums:
            return [[]]
        nums = sorted(nums)
        self.result = []
        self.dfs(nums, 0, [])
        return self.result
    
    def dfs(self, nums, curIndex, currentSet):
        if curIndex == len(nums):
            self.result.append(currentSet[:])
            return self.result
        
        currentSet.append(nums[curIndex])
        self.dfs(nums, curIndex+1, currentSet)
        
        currentSet.pop()
        self.dfs(nums, curIndex+1, currentSet)



