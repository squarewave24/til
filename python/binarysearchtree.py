class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinaryHashMapSearchTree(object):
    def __init__(self, val_type):
        self._root = None
        self._size = 0
        self._value_type = val_type

    def get(self, key):
        # walk the tree and find the node with matching key
        assert self._root, "Key {} not found".format(key)
        nodes_to_check = [self._root]
        while nodes_to_check:
            node = nodes_to_check.pop()
            if node.key == key:
                return node.value
            if node.right:
                nodes_to_check.append(node.right)
            if node.left:
                nodes_to_check.append(node.left)
        assert False, "Key {} not found".format(key)

    def put(self, key, value):
        assert isinstance(value, self._value_type), "value does not match expected type {}".format(self._value_type)
        self._size += 1
        if not self._root:
            self._root = Node(key, value)
            return
        node = self._root
        while node:
            if value >= node.value:
                # traverse right
                if node.right:
                    node = node.right
                    continue
                node.right = Node(key, value)
            else:
                # traverse left
                if node.left:
                    node = node.left
                    continue
                node.left = Node(key, value)
            return

    def size(self):
        return self._size

# testing
bhmst = BinaryHashMapSearchTree(str)
print(bhmst.size())
bhmst.put("test", "val")
print(bhmst.get("test"))
print(bhmst.size())
bhmst.put("test2", "zzz")
print(bhmst.get("test2"))
print(bhmst.size())
bhmst.put("test3", "aaa")
print(bhmst.get("test3"))
print(bhmst.size())
bhmst.put("test4", "aaa")
print(bhmst.get("test4"))
print(bhmst.size())
bhmst.put("test5", "b")
print(bhmst.get("test5"))
print(bhmst.size())
bhmst.put("test5", 6)


# runtime
# get: worst N, avg Log n
# put: worst N, avg Log n
# size: 
