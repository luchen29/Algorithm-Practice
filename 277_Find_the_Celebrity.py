# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
    	if not n:
    		return -1 
    	stack = []
    	for i in range(n):
    		stack.append(i)
    	while len(stack)>1:
    		personA = stack.pop()
    		personB = stack.pop()
    		if knows(personA,personB):
    			stack.append(personB)
    		else:
    			stack.append(personA)
    	lastPerson = stack.pop()
    	for i in range(n):
    		if i != lastPerson and knows(lastPerson,i)==True or knows(i,lastPerson)==False:
    			return -1 
    		else: 
    			continue
    	return lastPerson
# Time-complexity: O(n*n)