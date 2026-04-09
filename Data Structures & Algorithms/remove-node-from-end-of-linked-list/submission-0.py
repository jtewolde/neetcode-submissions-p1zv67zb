# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initial approach using left/right pointers
        # Create a dummy node that points to the head where left pointer starts there
        # Create a gap between left and right pointer of n length where right is initialized at with loop
        # Loop until right is null and n > 0, move right pointer to next node
        # Create another loop until right is null where it shifts both pointers
        # Then, delete node by making the left pointer skip over next node and point to the other node
        # Return dummy.next

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next









