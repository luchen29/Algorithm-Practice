"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return None
        upper = self.get_upper_bound(root, target)
        lower = self.get_lower_bound(root, target)
        if upper is None:
            return lower.val
        if lower is None:
            return upper.val 
        
        upper_diff = abs(upper.val-target) 
        lower_diff = abs(lower.val-target)        
        return upper.val if upper_diff < lower_diff else lower.val

    def get_upper_bound(self, root, target):
        if not root:
            return None
        if root.val <= target:
            return self.get_upper_bound(root.right, target)
        upper = self.get_upper_bound(root.left, target)
        return root if upper is None else upper
    
    def get_lower_bound(self, root, target):
        if not root:
            return None
        if root.val > target:
            return self.get_lower_bound(root.left, target)
        lower = self.get_lower_bound(root.right, target)
        return root if lower is None else lower