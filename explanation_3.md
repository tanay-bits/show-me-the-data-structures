I implemented the Priority Queue as a min-heap, sorted from least frequent character to most frequent character. The pop() and insert() methods of min-heap take O(log n) time (because of re-sorting the tree after every insertion or deletion). The nodes of the priority queue store the character, its frequency, its left child, right child, and bit for the Huffman Tree.

Huffman encoding is divided into the following steps:
* Creating a dictionary mapping characters to their frequencies -- **O(n)** time since we have to iterate over all characters in the input once. Dictionary access and insertion are O(1) so can be ignored.
* Creating a priority queue from the dictionary, sorted from lowest to highest frequency characters -- **O(n log n)** time -- because the insert operation takes O(log n) time and we have to do that for all n keys of the dictionary.
* Creating the Huffman Tree from the priority queue. This is done recursively since after replacing the two left most nodes in the queue with their "merged" node, the same procedure is applied on the modified queue, until the queue only has one node left. That is the root node of the Huffman Tree. This whole process takes **O(n log n)** time since the pop and insert operations at each recursive call take O(log n) time.
* Generating the Huffman code for each char -- **O(n)** time since we traverse the tree to find all the leaf nodes. Inserting to the dictionary mapping characters to codes takes O(1) time, so it can be ignored.
* Creating the final code -- **O(n)** time since we go over each character from the input data, access its code from the dictionary created in the previous step, and append it to our code string.

Huffman decoding takes **O(n)** time since we're doing O(1) operations over each bit of the encoded data.

Thus, the overall time complexity of my Huffman Coding routine is **O(n log n)**.

The test cases show the encoded data takes significantly less space than the input data.
