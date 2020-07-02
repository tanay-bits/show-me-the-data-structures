I implemented the Priority Queue as a list, sorted from left to right as highest priority (least frequent character) to lowest priority (most frequent character). The pop() operation pops the highest priority item, and the insert() operation appends the new item and sorts the list to maintain the priority order. Because of sorting, this insert() operation takes O(n log n) time. The nodes of the priority queue store the character, its frequency, its left child, right child, and bit for the Huffman Tree.

Huffman encoding is divided into the following steps:
* Creating a dictionary mapping characters to their frequencies -- **O(n)** time since we have to iterate over all characters in the input once. Dictionary access and insertion are O(1) so can be ignored.
* Creating a priority queue from the dictionary, sorted from lowest to highest frequency characters -- **O(n log n)** time since we have to sort the list. Appending nodes to the list takes O(n) time since we have to iterate over the keys of the dictionary, so it can be ignored relative to the sorting step.
* Creating the Huffman Tree from the priority queue. This is done recursively since after replacing the two left most nodes in the queue with their "merged" node, the same procedure is applied on the modified queue, until the queue only has one node left. That is the root node of the Huffman Tree. This whole process takes **O(n^2 log n)** time since we have to sort the queue at each step.
* Generating the Huffman code for each char -- **O(n)** time since we traverse the tree to find all the leaf nodes. Inserting to the dictionary mapping characters to codes takes O(1) time, so can be ignored.
* Creating the final code -- **O(n)** time since we go over each character from the input data, access its code from the dictionary created in the previous step, and append it to our code string.

Huffman decoding takes **O(n)** time since we're doing O(1) operations over each bit of the encoded data.

Thus, the overall time complexity of my Huffman Coding routine is **O(n^2 log n)**.

The test cases show the encoded data takes significantly less space than the input data.
