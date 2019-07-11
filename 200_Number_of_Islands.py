from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or grid[0] == []:
            return 0
        count = 0
        for x in range(0, len(grid)):
            for y in range(0, len(grid[0])):
                if grid[x][y] == '1':
                    grid[x][y] = 0
                    self.bfs(grid, x, y)
                    count += 1
                y += 1
            x += 1 
        return count 

    def bfs(self, grid, x, y):
        queue = deque()
        queue.append((x,y))
        while queue:
            r, c = queue.popleft()
            if self.isValid(grid, r, c-1) and grid[r][c-1]=='1':
                grid[r][c-1] = '0'
                queue.append((r,c-1))
            if self.isValid(grid, r, c+1) and grid[r][c+1]=='1':
                grid[r][c+1] = '0'
                queue.append((r,c+1))
            if self.isValid(grid, r+1, c) and grid[r+1][c]=='1':
                grid[r+1][c] = '0'
                queue.append((r+1,c))
            if self.isValid(grid, r-1, c) and grid[r-1][c]=='1':
                grid[r-1][c] = '0'
                queue.append((r-1,c))
    
    def isValid(self, grid, r, c):
        return True if 0<=r<len(grid) and 0<=c<len(grid[0]) else False
                
        