# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Basic understanding of reverse linked list:
        Create two pointers, prev and curr to keep track of nodes where
        Prev is initially none b/c there is no previous node from the head
        Curr is the current head
        While curr is not at the end of the linked list(None)
        Create a temporary variable to get the current node's next
        Set the next node to be the previous node
        Then, set prev to be the current node
        Finally, set curr to be the temporary variable
        Return prev as it should be the new head 
        """

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev