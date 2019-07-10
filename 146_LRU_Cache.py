class LinkNode():
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hash = {}
        self.head,self.tail = LinkNode(None,None), LinkNode(None,None)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash:
            return -1
        getNode = self.hash[key]
        getNode.prev.next, getNode.next.prev = getNode.next, getNode.prev
        getNode.prev, getNode.next = self.tail.prev, self.tail 
        getNode.prev.next = getNode 
        self.tail.prev = getNode
        return getNode.val
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.get(key) != -1:
            self.hash[key].val = value
            return 
        if len(self.hash) >= self.capacity:
            del self.hash[self.head.next.key]
            self.head.next = self.head.next.next
            self.head.next.prev = self.head            
        newNode = LinkNode(key,value)
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.hash[key] = newNode