class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
        	return 
        left, right = 0, 0
        while left<=right and right<=len(nums)-1:
        	if nums[right] != val:
        		if nums[left] != val:
	        		nums[left] = nums[right]
	        		left += 1 
	        		right += 1
	        	else:
	        		nums[left] = nums[right]
	        		left += 1 
	        		right += 1
        	else: 
        		right += 1
        return left