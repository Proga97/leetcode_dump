class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.cache.pop(node.key)
    
    def _insert(self,key,value):
        next = self.head.next
        node = Node(key,value)
        self.cache[key] = node
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node

    def get(self, key: int) -> int:
        # print(self.cache,self.head)
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert(node.key,node.val)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # print(self.cache,self.head)
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        if len(self.cache) >= self.capacity:
            self._remove(self.tail.prev)
        self._insert(key,value)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)