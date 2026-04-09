# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach for solving this problem:
        # First, create a dummy node and set curr to dummy
        # Create a carry variable that is initially zero
        # Iterate through both l1 and l2 in for loop until either l1 or l2 or carry is null
        # Set variables v1 and v2 to the value of nodes in both lists unless the node is Null, set to zero
        # Add v1, v2 and the carry together to get the new digit
        # Extract the carry from the new digit by int- dividing by 10
        # Get the ones place of new value by doing modular division by 10
        # Insert new val to the linked list as a ListNode with the value of val
        # Update both pointers, l1, l2, and curr by setting them all to next

        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # New digit addition
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            # Update pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return dummy.next









