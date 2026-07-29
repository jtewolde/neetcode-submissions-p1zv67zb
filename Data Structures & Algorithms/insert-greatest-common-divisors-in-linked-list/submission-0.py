# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach: Use simulation to traverse through the linked list, get consective pairs of nodes,
        # And compute the GCD and create a new node with that value
        # The built-in GCD function can be used but I will create the helper GCD function for better understanding

        # Create the helper GCD function that takes two parameters as nodes to use
        # While b is greater than zero, set a variable to b and b to the result of modular division between a and b
        # Return the value at a as final
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        # Start with curr pointing to the head of the list
        curr = head

        # While the next node from curr still exists
        while curr.next:
            # Get the values of the current pair in linked list traversion
            node1, node2 = curr.val, curr.next.val
            # Insert a new node between curr and curr.next into the list where the value is the GCD of node1 and node2
            curr.next = ListNode(gcd(node1, node2), curr.next)
            # Move the curr pointer past two nodes to get new pair
            curr = curr.next.next

        return head