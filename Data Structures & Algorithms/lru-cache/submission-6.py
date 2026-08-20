class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = self.head

        self.size = 0
        self.capacity = capacity

        self.key_node = {}

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        
        curr = self.key_node[key]
        if curr != self.tail:
            # Remove curr from its current position
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

            # Add curr to the end
            curr.next = None
            curr.prev = self.tail

            self.tail.next = curr
            self.tail = curr

        return curr.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.key_node:
            curr = self.key_node[key]
            curr.val = value    # Update value

            if curr != self.tail:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev

                curr.next = None
                curr.prev = self.tail

                self.tail.next = curr
                self.tail = curr

            return

        if self.size == self.capacity:
            # Remove LRU from hashmap
            lru = self.head.next
            del self.key_node[lru.key]

            # Remove LRU form linked list
            self.head.next = lru.next
            if lru.next:
                lru.next.prev = self.head
            else:
                self.tail = self.head

            self.size -= 1

        # Create new node
        node = Node(
            key=key, 
            val=value, 
            prev=self.tail
        )

        # Add node to end
        self.tail.next = node
        self.tail = node

        # add node to hashmap
        self.key_node[key] = node
        self.size += 1


# GOAL
# =======
# Implement an LRU cache s.t.
#   * LRUCache() initializes capacity
#   * get() returns the value corresponding to key if exists. 
#       -1 otherwise.
#   * put() updates the value of key if exists. 
#       Adds to cache otherwise. If exceeds capacity, remove
#       least recently used key.
# Want O(1) avg. TC for get and put.

# BRUTE FORCE
# =======
#   * LRUCache(): Initialize a list of size capacity.
#   * get(): Loop through list to find the key.
#       If found, remove it from current position.
#       Append it to the end and return its value.
#   * put(): Loop through list to find the key.
#       If found, remove from current position and
#           append key with new value.
#       Othwerise, add to cache if capacity not exceeded.
#           If capacity exceeded, remove beginning of list and add
#           new pair.
# TC: O(N)
# SC: O(N)
        
# IDEA
# =======
# Why is brute force suboptimal?
#   We have to look through the cache to find the key.
# We can use a hashmap to find the key and its location, but
#   if something is removed, we'd have to move the location of each
#   element after it.
# We can use a doubly linked list and a hashmap.
#   The hashmap will map keys -> nodes.
#   Removing an element from a linked list does not require shifting.
#   The head of the linked list will give us our LRU.
#   Doubly linked to make removals easier.

# PSEUDOCODE
# =======
#   * LRUCache(): Initialize size and capacity.
#   * get(): Use hashmap to find key node.
#       If found, remove it from current position.
#       Append it to the end and return its value.
#   * put(): Use hashmap to see if key exists.
#       If found, remove it from current position and
#           append new node with new value to the end.
#       Othwerise, add to cache if capacity not exceeded.
#           If capacity exceeded, remove beginning of list and add
#           new pair at end.
# TC: O(1)
# SC: O(N)