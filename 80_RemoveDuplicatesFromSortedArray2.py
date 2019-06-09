# fast slow pointer
# fast dont care, just go 
# 用快指针的内容给慢指针指向的下一个赋值 to fast value; slow go forward
# write the loop 
# set the condition for loop
# slow to end -> ignore
# consider the threshold

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for fast in range(0,range):


		if not nums:
			return 
		left, right = 0, 0
		while left<=right and right<=len(nums)-1:
			if nums[right] != nums[left]:
				if right - left > 2:
					nums[left+2] = nums[right]
					left += 3
				elif right - left == 2:
					nums[left+1] = nums[right]
					left += 2
				else:
					nums[left] = nums[right]
			else:
				right += 1 
		return left







