# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Pre-order traversal 
# 1. recursive
class Solution(object):
    def preorderTraversal(self,root):
    	self.result = []
    	self.traverse(root)
    	return self.result

    def traverse(self, root):
    	if not root:
    		return 
    	self.result.append(root.val)
    	self.traverse(root.left)
    	self.traverse(root.right)

# 2. iterative
class Solution(object):
    def preorderTraversal(self,root):
    	if not root:
    		return 
    	stack = [root]
    	result = []
    	while stack:
	    	node = stack.pop()
	    	result.append(node.val)
	    	if node.right:
	    		stack.append(node.right)
	    	if node.left:
	    		stack.append(node.left)
    	return result


# In-order traversal 
# 1. recursive
class Solution(object):
    def inorderTraversal(self,root):
    	self.result = []
    	self.traverse(root)
    	return self.result

    def traverse(self, root):
    	if not root:
    		return 
    	self.traverse(root.left)
    	self.result.append(root.val)
    	self.traverse(root.right)

# 2. iterative
class Solution(object):
    def inorderTraversal(self,root):
        dummy = TreeNode(0)
        dummy.right = root
    	stack = [dummy]
    	result = []
    	while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                result.append(stack[-1].val)
    	return result


# Post-order traversal
# 1. recursive
class Solution(object):
    def postorderTraversal(self,root):
    	self.result = []
    	self.traverse(root)
    	return self.result

    def traverse(self, root):
    	if not root:
    		return 
    	self.traverse(root.left)
    	self.traverse(root.right)
    	self.result.append(root.val)


# 2. iterative
class Solution(object):
    def postorderTraversal(self,root):
    	if not root:
    		return 
    	stack = [root]
    	result = []
    	while stack:
    		node = stack.pop()
    		if root.right:
    			stack.append(root.right)
    		if root.left:
    			sutcl.append(root.left)
    		result.append(root.val)
    	return result



# construct binary tree with Pre-order & In-order
class Solution(object):
    def buildTree(self, preorder, inorder):
    	if preorder == [] or inorder == []:
    		return
    	



# construct binary tree with Post-order & In-order

# construct binary tree with Pre-order & Post-order

# construct binary tree with Preorder 

# Maximum Depth of Binary Tree


