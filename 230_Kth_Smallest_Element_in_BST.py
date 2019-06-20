"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# idea: 这道题和inorder iterator思路一样的
class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        stack = []
        while root is not None:
            stack.append(root)
            root = root.left
        
        for i in range (k-1):
            if stack is None:
                break
            node = stack[-1]
            if node.right is not None:
                n = node.right
                while n is not None:
                    stack.append(n)
                    n = n.left
            else: 
                n = stack.pop()
                while stack is not None and stack[-1].right == n:
                    n = stack.pop()
        return stack[-1].val