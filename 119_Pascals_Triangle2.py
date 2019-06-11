class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1] + [0]*rowIndex
        for i in range (rowIndex):
        	for j in range(i+1,0,-1):
        		result[j] = result[j] + result[j-1]
        return result

# only one row is needed to be pre-defined
# update vals in this row from right to left (otherwise previoud answer will affect later one)
# return the last state of the row as result.