# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Approach: 
        # Create two pointers, prev and curr, for tracking current and previous nodes
        # Traverse through the linked list, if encounter a node that has val as its value
        # Keep track of the node that it was pointing to(node.next), remove the node
        # See the previous node's next pointer to what the removed node was

        # Initialize prev, dummy, and curr pointers where curr starts at head of linked list
        # Prev will point to the previous node of curr that is a dummy node
        curr = head
        prev = dummy = ListNode(0, head)

        # Iterate through linked list while cur node isn't null
        while curr:
            # Get the next node for current regardless
            next_temp = curr.next
            # If the value of the current node is the val that needs to be removed,
            # Set the next pointer for previous node to get the next node of curr to be removed
            if curr.val == val:
                prev.next = next_temp
            # Otherwise, set previous to curr to iterate through rest of linked list
            # By moving curr and prev pointers forward
            else:
                prev = curr
            curr = next_temp
        # Return next node of dummy to get the rest of new linked list with removed elements
        return dummy.next
           