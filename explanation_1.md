
To implement the LRU cache, I am storing the input entries in a dictionary. Presuming Python's dict() to have a good enough collision-free hash function, dictionary access and insertion takes O(1) time.

To keep track of how recently each entry has been used (get/set), I implemented a deque as a doubly linked list. It always maintains the order of the least recently used entry on the left (head) end to the most recently used entry on the right (tail) end.

Since in the deque I always have references to the head and the tail, and each node has references to its previous and next node in a doubly linked list,

* Popping off the head (when the cache reaches its capacity) takes O(1) time; see pop_left() method

* Inserting a new entry at the tail end takes O(1) time; see push_right() method

* Moving an existing entry from anywhere in the deque to the tail end also takes O(1) time; see move_to_right_end() method
