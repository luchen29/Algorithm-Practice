# Lowest Common Ancestor of a Binary Tree (Leetcode 236 // Lintcode 88)
# 思路： 无脑divide& conqure

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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


# Lowest Common Ancestor of a Binary Search Tree (Leetcode 235)
# 思路： 先序排列，先判断给出的节点所有子树范围 -> 再divide& conquer 可以减少搜索成本
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
        
        if p.val == root.val or q.val == root.val:
            return root
        if p.val < root.val and q.val < root.val:
            left_node = self.lowestCommonAncestor(root.left, p, q)
            return left_node
        if p.val > root.val and q.val > root.val:
            right_node = self.lowestCommonAncestor(root.right, p, q)
            return right_node
        return root

# Lowest Common Ancestor without knowing whether nodes are in the tree (Lintcode 578)
# 思路：由于不知节点A，B是否在树里，因此需要多return两个para：a和b。只有当a，b同时存在在树里的时候才返回lca
# 如何找是否在树里：无脑divide& conquer；最终判断左/右/root那个有a或b，就赋给a/b
class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        a, b, lca = self.helper(root, A, B)
        if a and b:
            return lca 
        else:
            return None
    
    def helper(self, root, A, B):
        if not root:
            return False, False, None
        left_a, left_b, left_node = self.helper(root.left, A, B)
        right_a, right_b, right_node = self.helper(root.right, A, B)
        
        a = left_a or right_a or root==A 
        b = left_b or right_b or root==B 
        
        if root==A or root==B:
            return a, b, root 
        if left_node is not None and right_node is not None:
            return a, b, root 
        if left_node is not None and right_node is None:
            return a, b, left_node
        if left_node is None and right_node is not None:
            return a, b, right_node
        return a, b, None
        

# Lowest Common Ancestor with an extra attribute "parent" which point to the father of itself (Lintcode 474)
# 思路： 这道题用不上divide& conquer这么复杂。因为已知每个节点的parent，因此可直接由A，B出发往root走，走过的节点计入dict里；如果二者出现交叉则找到lca。
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""
class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        if not root:
            return None
            
        path_dict = {} 
        
        while A is not root:
            path_dict[A] = True
            A = A.parent
        while B is not root:
            if B in path_dict:
                return B
            B = B.parent
        return root

