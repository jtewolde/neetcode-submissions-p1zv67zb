# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initial approach for this problem:
        # Create two different pointers, fast and slow
        # fast pointer is to look ahead the linked list(two nodes ahead)
        # slow pointer is to see the next node 
        # Iterate through the linked list
        # If any point does the slow and fast pointer equal each other(same node), return true
        # Otherwise, return false

        fast, slow = head, head # create pointers

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False



