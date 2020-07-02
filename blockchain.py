import hashlib
import time

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def empty(self):
        return self.size == 0

    def push(self, node):
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

    def pop(self):
        out = self.tail
        if self.size() <= 1:
            self.head = None
            self.tail = None
        else:
            self.tail = out.prev
            self.tail.next = None
        self.size -= 1
        return out

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        information = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        hash_str = information.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:

    def __init__(self):
        self.chain = LinkedList()
        self.create_initial_node()

    def create_initial_node(self):
        initial_node = Node(Block(time.gmtime(), '', '0'))
        self.chain.push(initial_node)

    def last_block(self):
        return self.chain.tail.value

    def add_block(self, data):
        block = Block(time.gmtime(), data, self.last_block().hash)
        node = Node(block)
        self.chain.push(node)

    def size(self):
        if self.chain.size > 0:
            return self.chain.size - 1
        else:
            return 0

    def verify(self):
        node = self.chain.tail
        while node is not self.chain.head:
            if node.value.previous_hash != node.prev.value.hash:
                print("Wrong previous hash!")
                return False
            if node.value.hash != node.value.calc_hash():
                print("Wrong hash!")
                return False
            node = node.prev
        return True


# Tests
block_chain = Blockchain()
block_chain.add_block("data1")
block_chain.add_block("data2")

print(block_chain.size())
print(block_chain.verify())
