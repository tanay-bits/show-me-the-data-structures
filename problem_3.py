import sys

class Node(object):
    def __init__(self, char, freq, bit=''):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.bit = bit

    def is_leaf(self):
        return (self.left is None and self.right is None)


class PriorityQueue(object):
    def __init__(self):
        self.q = []

    def size(self):
        return len(self.q)

    def pop(self):
        if self.size() == 0:
            return None
        return self.q.pop(0)

    def insert(self, node):
        self.q.append(node)
        self.q.sort(key=lambda node: node.freq)

    def __repr__(self):
        char_freq_tuples = []
        for node in self.q:
            char_freq_tuples.append((node.char, node.freq))
        return f"PQ is {char_freq_tuples}"

def find_frequencies(data):
    char_to_freq = {}
    for char in data:
        if char in char_to_freq:
            char_to_freq[char] += 1
        else:
            char_to_freq[char] = 1
    return char_to_freq

def create_huffman_tree(pq):
    if pq.size() == 1:
        return pq.q[0]

    first = pq.pop()
    second = pq.pop()
    merged = Node(None, first.freq + second.freq)
    merged.left = first
    merged.right = second
    merged.left.bit = '0'
    merged.right.bit = '1'
    pq.insert(merged)

    return create_huffman_tree(pq)

def populate_codes(root, prefix, codes):
    left = root.left
    right = root.right

    # Terminal condition: being at a leaf node
    if root.is_leaf():
        codes[root.char] = prefix if prefix is not '' else '0'
        return

    # Otherwise update the prefix based on the children's bits and traverse down the tree
    if left is not None:
        new_prefix = prefix + left.bit
        populate_codes(left, new_prefix, codes)
    if right is not None:
        new_prefix = prefix + right.bit
        populate_codes(right, new_prefix, codes)

def generate_huffman_codes(root):
    codes = {}
    prefix = ''
    populate_codes(root, prefix, codes)
    return codes

def huffman_encoding(data):
    # Handle empty input
    if data == "":
        return "0", None

    # Create a mapping from characters to their frequencies
    char_to_freq = find_frequencies(data)

    # Create a priority queue from the map, sorted from lowest to highest frequency characters
    pq = PriorityQueue()
    for char in char_to_freq:
        node = Node(char, char_to_freq[char])
        pq.q.append(node)
    pq.q.sort(key=lambda node: node.freq)

    # Create Huffman Tree from the priority queue
    ht_root = create_huffman_tree(pq)

    # Generate Huffman code for each char from input data
    codes = generate_huffman_codes(ht_root)

    # Create final code from input data
    encoded_data = ''
    for char in data:
        encoded_data = encoded_data + codes[char]

    return encoded_data, ht_root

def huffman_decoding(encoded_data, tree):
    decoded_data = ''
    node = tree
    if node:
        for bit in encoded_data:
            if bit == '0' and node.left:
                node = node.left
            elif bit == '1' and node.right:
                node = node.right

            if node.is_leaf():
                decoded_data = decoded_data + node.char
                node = tree

    return decoded_data

if __name__ == "__main__":
    # Test 1: regular sentence
    print("Test 1\n")
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 69
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 36
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 0110111011111100111000001010110000100011010011110111111010101011001010

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 69
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    # The content of the decoded data is: The bird is the word

    assert decoded_data == a_great_sentence
    # AssertionError only if something is wrong

    # Test 2: really long sentence
    print("\nTest 2\n")
    a_great_sentence = "The bird is the word"
    for i in range(10000):
        a_great_sentence = a_great_sentence + " wow!"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 50069

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 14704

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 50069

    assert decoded_data == a_great_sentence
    # AssertionError only if something is wrong

    # Test 3: empty string input
    print("\nTest 3\n")
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 49
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is:

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 24
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 0

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 49
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    # The content of the decoded data is:

    assert decoded_data == a_great_sentence
    # AssertionError only if something is wrong

    # Test 4: one character input
    print("\nTest 4\n")
    a_great_sentence = "x"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # The size of the data is: 50
    print ("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: x

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 24
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 0

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 50
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    # The content of the decoded data is: x

    assert decoded_data == a_great_sentence
    # AssertionError only if something is wrong
