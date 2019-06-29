class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return num  
        if k >= len(num):
            return "0"
        result = []
        for i in range(len(num)):
            while len(result) > 0 and k > 0 and result[-1] > num[i]:
                result.pop()
                k -= 1 
            if num[i] != '0' or len(result) > 0:
                result.append(num[i])
        while len(result) > 0 and k > 0:
            result.pop()
            k -= 1 
        if len(result) == 0:
            return '0'
        return ''.join(result)
