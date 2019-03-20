class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix == [] or matrix == [[]]:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        i = row-1
        j = 0
        count = 0
        while i >= 0 and j < col:
            if matrix[i][j] == target:
                count += 1
                i -= 1 
                j += 1 
            elif matrix[i][j] < target:
                j += 1 
            elif matrix[i][j] > target:
                i -= 1 
        return count   