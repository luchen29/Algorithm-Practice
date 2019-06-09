"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Method 1: 
# use traverse to Post-order-遍历 all nodes; 
# use divide & conqure method for solving this problem;
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
    	self.minimum_weight = sys.maxsize
    	self.subtree = None
    	self.helper(root)
    	return self.subtree 

    def helper(self, root):
    	if not root:
    		return 0
    	left_weight = self.helper(root.left)
    	right_weight = self.helper(root.right)
    	root_weight = left_weight + right_weight + root.val

    	if root_weight < self.minimum_weight:
    		self.minimum_weight = root_weight
    		self.subtree = root

    	return self.minimum_weight


# (Optimization) Method 2:
# use less global variables (self.xxx)
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
    	minimum_weight, subtree, sum_weights = self.helper(root)
    	return subtree
    
    def helper(self, root):
    	if not root:
    		return sys.maxsize, None, 0
    	left_min_weight, left_subtree,left_sum_weights = self.helper(root.left)
    	right_min_weight, right_subtree,right_sum_weights = self.helper(root.right)
    	sum_weights = left_sum_weights + right_sum_weights + root.val 

    	if sum_weights == min(left_min_weight,right_min_weight,sum_weights):
    		return sum_weights, root, sum_weights
    	if left_min_weight == min(left_min_weight,right_min_weight,sum_weights):
    		return left_min_weight, left_subtree, sum_weights
    	return right_min_weight, right_subtree, sum_weights 




