"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Approach for solving this problem with two passes and hashmap
        # Creating deep copy = cloning nodes to hashmap and then connect nodes
        # First, initialize hashmap where it stores copys of the old linked list, make sure none points to none
        # Make the first pass through linked list using while loop
        # Inside first loop, create copy of current node, store it inside of hash map, them move to next node
        # Inside second loop, retrieve copy node from hashmap
        # Connect copy node's next pointer with next pointer from the node inside of the hashmap
        # Connect copy node's random pointer with random from node inside of hash map
        # Move to next node with curr.next
        # Return the head from the hashmap

        orignalToCopy = { None:None }

        curr = head
        while curr:
            copy = Node(curr.val)
            orignalToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = orignalToCopy[curr]
            copy.next = orignalToCopy[curr.next]
            copy.random = orignalToCopy[curr.random]
            curr = curr.next

        return orignalToCopy[head]


















