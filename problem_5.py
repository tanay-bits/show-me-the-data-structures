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
        if self.size <= 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.tail = out.prev
            self.tail.next = None
            self.size -= 1
        return out

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

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

    def __str__(self):
        return str(self.data)

class Blockchain:
    def __init__(self):
        self.chain = LinkedList()
        self.create_initial_node()

    def create_initial_node(self):
        initial_node = Node(Block(time.gmtime(), '<genesis_block>', '0'))
        self.chain.push(initial_node)

    def last_block(self):
        return self.chain.tail.value

    def add_block(self, data):
        block = Block(time.gmtime(), data, self.last_block().hash)
        node = Node(block)
        self.chain.push(node)

    def size(self):
        if self.chain.size > 0:
            return self.chain.size - 1  # not counting the initial node
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


# Test 1
print("Test 1\n")
block_chain = Blockchain()
block_chain.add_block("data1")
block_chain.add_block("data2")
block_chain.add_block("data3")
block_chain.add_block("data4")
block_chain.add_block("data5")

print(block_chain.chain)
# <genesis_block> -> data1 -> data2 -> data3 -> data4 -> data5 ->
print(block_chain.last_block())
# data5
print(block_chain.size())
# 5
print(block_chain.verify())
# True

# Test 2
print("\nTest 2\n")
node = block_chain.chain.head
for i in range(3):
    node = node.next
node.value.data = "corrupted data"
print(block_chain.chain)
# <genesis_block> -> data1 -> data2 -> corrupted data -> data4 -> data5 ->
print(block_chain.verify())
# Wrong hash!
# False

# Test 3
print("\nTest 3\n")
block_chain = Blockchain()
block_chain.add_block("data1")
block_chain.add_block("data2")
block_chain.add_block("data3")
block_chain.add_block("data4")
block_chain.add_block("data5")
node = block_chain.chain.head
for i in range(3):
    node = node.next
node.value.data = "corrupted data"
node.value.hash = node.value.calc_hash()
print(block_chain.chain)
# <genesis_block> -> data1 -> data2 -> corrupted data -> data4 -> data5 ->
print(block_chain.verify())
# Wrong previous hash!
# False
