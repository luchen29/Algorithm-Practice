class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    # Two pointer
    def twoSum6(self, nums, target):
        # write your code here
        left = 0
        right = len(nums)-1 
        count = 0
        nums.sort()
        while left < right:
            if nums[left] + nums[right] == target:
                if left == 0:
                    count += 1
                    left += 1 
                    right -= 1
                    continue
                if left > 0 and nums[left] != nums[left-1]:
                    left += 1 
                    right -= 1
                    count += 1
                    continue
                left += 1 
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1 
            else: 
                right -= 1 
        return count    


    # Hash Table (0--> never used before// 1--> already used before)
    def twoSum6(self, nums, target):
        if not nums:
            return 0
        hash = {}
        count = 0
        for n in nums:
            if target-n in hash and hash[target-n] == 0:
                count += 1 
                hash[target-n] = 1 
                hash[n] = 1 
                continue
            if n not in hash:
                hash[n] = 0
        return count

# Unsorted, two sum, find unique pairs