"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
    	result = []
    	inDegreeTable = self.getIndegree(graph)
    	startNodes = [Node for Node in inDegreeTable if inDegreeTable[Node]==0]
    	queue = deque(startNodes)
    	while queue:
    		curNode = queue.popleft()
    		result.append(curNode)
    		del inDegreeTable[curNode]
    		for neighbor in curNode.neighbors:
    			inDegreeTable[neighbor] -= 1 
    			if inDegreeTable[neighbor] == 0:
    				queue.append(neighbor)
    	return result


    def getIndegree(self, graph):
    	hash = {Node: 0 for Node in graph}
    	for node in hash:
    		for neighbor in node.neighbors:
    			hash[neighbor] += 1 
    	return hash
