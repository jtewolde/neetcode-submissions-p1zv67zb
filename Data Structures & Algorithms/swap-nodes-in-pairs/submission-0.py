# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach: Use iteration and dummynode to take a pair of nodes and swap their pointers in the linked list
        # Continue with swapping the links between pair of nodes until last node is null
        # If the linked list is odd, leave the last node unchanged

        # Initialize dummy node that has val of 0 and points to the head of the linked list
        # Also, create prev and curr nodes that start at dummy and head nodes
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        # Iterate through each pair in linked list until either node is null
        while curr and curr.next:
            # Save pointers for swapping
            nxtPair = curr.next.next
            secondNode = curr.next

            # Reverse the links of the current pair
            secondNode.next = curr
            curr.next = nxtPair
            prev.next = secondNode

            # Update the pointers to point at the next pairs
            prev = curr
            curr = nxtPair
        return dummy.next
