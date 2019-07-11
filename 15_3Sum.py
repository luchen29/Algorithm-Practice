class Solution(object):
    def threeSum(self, nums):
    	if not nums:
    		return None 
    	nums.sort()
    	result = [] 
    	length = len(nums)
    	index = 0
    	while index < length-2:
    		left = index+1 
    		right =	 length-1 
    		target = 0 - nums[index]
    		if index > 0 and nums[index] == nums[index-1]:
    			index += 1 
    			continue 
    		while left < right:
    			if left > index+1 and nums[left] == nums[left-1]:
    				left += 1 
    				continue
    			if nums[left] + nums[right] == target:
    				result.append([nums[index],nums[left],nums[right]])
    				left += 1 
    				right -= 1 
    			elif nums[left] + nums[right] > target:
    				right -= 1 
    			else:
    				left += 1 
    		index += 1 
    	return result

class Solution(object):
    def threeSum(self, nums):
        if not nums or len(nums)<3:
            return []
        nums.sort()
        self.result = []
        for idx in range(0, len(nums)-2):
            left, right = idx+1, len(nums)-1
            target = 0-nums[idx]
            if idx != 0 and nums[idx] == nums[idx-1]:
                continue
            self.findSum(nums, target, left, right)
        return self.result
    
    def findSum(self, nums, target, left, right):
        while left < right:
            if nums[left] + nums[right] == target:
                self.result.append([-target, nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -=1
            elif nums[left] + nums[right] < target:
                left += 1
            else: right -= 1

class Solution(object):
    def threeSum(self, nums):
		resultset = []
        nums.sort()
        for fixindex in range(len(nums)-2):
            if fixindex > 0 and nums[fixindex] == nums[fixindex-1]:
                continue
            endindex = len(nums)-1
            startindex = fixindex+1
            while startindex < endindex:
                if nums[fixindex] + nums[startindex] + nums[endindex] < 0:
                    startindex += 1
                elif nums[fixindex] + nums[startindex] + nums[endindex] > 0:
                    endindex -= 1
                else: 
                    resultset.append([nums[fixindex],nums[startindex],nums[endindex]])
                    startindex += 1
                    endindex -= 1
                    while nums[startindex] == nums[startindex-1] and startindex< endindex: 
                        startindex += 1
                    while nums[endindex] == nums[endindex+1] and startindex< endindex:
                        endindex -= 1          
        return resultset  
