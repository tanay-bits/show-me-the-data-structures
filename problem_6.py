
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.head.next = self.tail
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

def union(llist_1, llist_2):
    union_list = LinkedList()
    uniques_1 = set()
    uniques_2 = set()

    node = llist_1.head
    while node:
        if node.value not in uniques_1:
            union_list.append(node)
        uniques_1.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if node.value not in uniques_1 and node.value not in uniques_2:
            union_list.append(node)
        uniques_2.add(node.value)
        node = node.next

    return union_list

def intersection(llist_1, llist_2):
    intersection_list = LinkedList()
    uniques_1 = set()
    uniques_2 = set()

    node = llist_1.head
    while node:
        uniques_1.add(node.value)
        node = node.next

    node = llist_2.head
    while node:
        if node.value in uniques_1 and node.value not in uniques_2:
            intersection_list.append(node)
            uniques_2.add(node.value)
        node = node.next

    return intersection_list

# Test 1
print("Test 1\n")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 ->
print(intersection(linked_list_1, linked_list_2))
# 6 -> 4 -> 21 ->

# Test 2
print("\nTest 2\n")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_1, linked_list_2))
# <empty>, since the intersection of these sets contains no element

# Test 3
print("\nTest 3\n")
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_1, linked_list_2))
# <empty>, since the intersection of these sets contains no element
