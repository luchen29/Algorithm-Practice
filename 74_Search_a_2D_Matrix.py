class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [] or matrix == [[]]:
            return False
        rowIndex = self.findRowIndex(matrix, target)
        if rowIndex == "True":
            return True
        if rowIndex == "False":
            return False
        return self.findColIndex(matrix, target,rowIndex)

    def findRowIndex(self, matrix, target):
        row_num = len(matrix)
        col_num = len(matrix[0])
        row_start = 0
        row_end = row_num - 1
        while row_start+1<row_end:
            mid = (row_start+row_end)//2
            if matrix[mid][0] > target:
                row_end = mid
            if matrix[mid][0] == target:
                return "True"
            if matrix[mid][0] < target:
                row_start = mid
        if matrix[row_end][0] <= target:
            return row_end
        if matrix[row_start][0] <= target:
            return row_start
        return "False"

    def findColIndex(self, matrix, target, rowIndex):
        row_num = len(matrix)
        col_num = len(matrix[0])
        start = 0
        end = col_num - 1
        while start+1<end:
            mid = (start+end)//2
            if matrix[rowIndex][mid] > target:
                end = mid
            if matrix[rowIndex][mid] == target:
                return True
            if matrix[rowIndex][mid] < target:
                start = mid
        if matrix[rowIndex][start] == target:
            return True
        if matrix[rowIndex][end] == target:
            return True
        return False

# 2D Binary Search
