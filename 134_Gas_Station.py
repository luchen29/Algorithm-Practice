class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        startIdx, curGas = 0, 0
        
        for i in range (len(gas)):
            curGas += gas[i]-cost[i]
            if curGas < 0:
                curGas = 0
                startIdx = i + 1
        return startIdx
                