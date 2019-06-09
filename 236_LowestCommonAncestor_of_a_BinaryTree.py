# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Use divide and conquer method:
# Try to fine the return of left-sub and right-sub tree 
# then base on the result -> get the overall node return. 

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None 
        
        if root == p or root == q:
            return root 
        
        left_node = self.lowestCommonAncestor(root.left, p, q)
        right_node = self.lowestCommonAncestor(root.right, p, q)
        
        if left_node is not None and right_node is not None:
            return root 
        if left_node is not None and right_node is None:
            return left_node 
        if left_node is None and right_node is not None:
            return right_node
        return None