
class Node(object):

    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def empty(self):
        return self.size == 0

    def push_right(self, node):
        if self.empty():
            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def pop_left(self):
        out = self.head
        if self.size <= 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
        return out

    def move_to_right_end(self, node):
        if node == self.head:
            self.pop_left()
        else:
            node.prev.next = node.next
        self.push_right(node)

class LRU_Cache(object):

    def __init__(self, capacity):
        assert capacity > 0
        # Initialize class variables
        self.capacity = capacity
        self.cache = dict()
        self.q = LinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            # Transport the node associated with this key to the tail of the queue
            node = self.cache[key]
            self.q.move_to_right_end(node)

            # Return the value of that node
            out = node.value
        else:
            out = -1

        print(out)
        return out

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache:
            # Transport the node associated with this key to the tail of the queue
            node = self.cache[key]
            self.q.move_to_right_end(node)

        else:
            if len(self.cache) == self.capacity:
                # remove oldest item
                nodeToRemove = self.q.pop_left()
                self.cache.pop(nodeToRemove.key)

            # add new item
            node = Node(key, value)
            self.q.push_right(node)
            self.cache[key] = node


# Test 1
print("Test 1\n")
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

our_cache.get(1)
# 1
our_cache.get(2)
# 2
our_cache.get(9)
# -1

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)
# -1

# Test 2
print("\nTest 2\n")
our_cache = LRU_Cache(1)
our_cache.set('a', 72)
our_cache.set('', 69)

our_cache.get('a')
# -1
our_cache.get('')
# 69

# Test 3
print("\nTest 3\n")
our_cache = LRU_Cache(0)
# should raise AssertionError due to invalid capacity argument
