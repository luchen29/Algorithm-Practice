def canFinish(self, numCourses, prerequisites):
        # write your code here
        if not prerequisites:
            return True
        self.n = numCourses
        courseOrder = []
        AOV, nodeIndegree = self.getAOVNIndegree(prerequisites)
        initCourses = [initcourse for initcourse in nodeIndegree if nodeIndegree[initcourse]==0]
        queue = deque(initCourses)
        while queue:
            curCourse = queue.popleft()
            courseOrder.append(curCourse)
            del nodeIndegree[curCourse]
            for neighbor in AOV[curCourse]:
                nodeIndegree[neighbor] -= 1 
                if nodeIndegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(nodeIndegree) > 0 :
            return False
        return True
    
    def getAOVNIndegree(self, prerequisites):
        AOV = {x: [] for x in range(self.n)}
        nodeIndegree = {x: 0 for x in range(self.n)}
        for coursePair in prerequisites:
            AOV[coursePair[1]].append(coursePair[0])
            nodeIndegree[coursePair[0]] += 1
        return AOV, nodeIndegree