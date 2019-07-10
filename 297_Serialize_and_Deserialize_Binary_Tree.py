# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        if not root: return 
        queue = deque([root])
        result = [str(root.val)]
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    result.append(str(node.left.val))
                else: result.append("#")
                if node.right:
                    queue.append(node.right)
                    result.append(str(node.right.val))
                else: result.append("#")
        return ",".join(result)

    def deserialize(self, data):
        if not data: return
        datalist = data.split(",")
        nodes = []
        for data in datalist:
            nodes.append(None) if data == "#" else nodes.append(TreeNode(int(data)))
        root = nodes[0]
        slow, fast  = 0, 1
        if len(nodes) == 1: 
            return root
        if len(nodes) == 2:
            root.left = nodes[fast]
            return root
        while fast < len(nodes)-1:
            if nodes[slow] == None:
                slow += 1
                continue 
            curNode = nodes[slow]
            if nodes[fast] or nodes[fast+1]:
                curNode.left = nodes[fast]
                curNode.right = nodes[fast+1]
            fast += 2
            slow += 1
        return root
            
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))