"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""

# idea: iteration存入stack，如果以中序遍历为例，则先把左侧一条上的node都放入栈
# 判断当前栈顶的节点是否有右节点 如果有，按中序方式加入stack； 如果没有判断该节点是否为其父节点的右节点
# 如果是 则pop出来， 如果不是则返回当前节点

class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return len(self.stack) > 0
        

    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        node = self.stack[-1]
        if node.right is not None:
            n = node.right
            while n is not None:
                self.stack.append(n)
                n = n.left
        else: 
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        return node.val
                
