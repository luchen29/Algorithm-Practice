# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method 1: simply traversal
# append str(val) and pop it out after reaching leaf
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = []
        self.dfs(root, [str(root.val)], result)
        return result
        
    def dfs(self, root, nodes, result):
        if root.left:
            nodes.append(str(root.left.val))
            self.dfs(root.left, nodes, result)
            nodes.pop()
        if root.right:
            nodes.append(str(root.right.val))
            self.dfs(root.right, nodes, result)
            nodes.pop()
        if root.left is None and root.right is None:
            result.append("->".join(nodes))
            return 

# Method 2: simply divide and conquer
class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        paths = []
        for path in self.binaryTreePaths(root.left):
            paths.append(str(root.val) + "->" + path)

        for path in self.binaryTreePaths(root.right):
            paths.append(str(root.val) + "->" + path)
            
        return paths
        
        





