class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        if len(numbers) < 3:
            return 0
        numbers.sort()
        result = None 
        for i in range (0,len(numbers)-2):
            left = i + 1 
            right = len(numbers)-1
            while left < right:
                threeSum = numbers[i] + numbers[left] + numbers[right]
                if result is None or abs(threeSum-target) < abs(result-target):
                    result = threeSum
                if threeSum == target:
                    return threeSum
                elif threeSum < target:
                    left += 1 
                else:
                    right -= 1
        return result  
            