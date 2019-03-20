class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        i = row-1
        j = 0
        count = 0
        while i >= 0 and j < col:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return False

# O(m+n), search from left_bottom corner to right_top corner.
# Similar to: return occur-times-problem. 
