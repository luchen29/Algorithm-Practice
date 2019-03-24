class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {} 
        for i in range(0,len(nums)):
            if target - nums[i] in hash:
                return [hash[target-nums[i]],i]
            hash[nums[i]] = i 
        return [-1,-1]

# Unsorted Two sum --> Hash Table
# key: nums[index]
# value: index
# Need to return the index, so set index as value. return which--> set which to value.
