# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Approach: Use fast and slow pointers to get to middle node in linked list
        # Slow pointer moves one node at a time while fast moves two nodes at time
        # When the fast pointer reaches the end of linked list,
        # Slow pointer will be at the middle node since fast covers twice as many nodes

        # Initialize fast and slow pointers both at head of linked list
        fast, slow = head, head

        # Traverse through linked list while fast pointer isn't null/doesn't reach end
        while fast and fast.next:
            # Move fast pointers two nodes and slow pointer one at a time
            slow = slow.next
            fast = fast.next.next
        return slow

