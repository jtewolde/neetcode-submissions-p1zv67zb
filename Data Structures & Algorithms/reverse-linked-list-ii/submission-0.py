# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Logic: Left and right pointers indicate the window in the linked list.
        # That need to be reversed within the linked list.
        # Split linked list into three different sections: nodes before reversed section, reversed section itself, and after reversed section
        
        # First section, creating dummy node before head of linked list to prevent edge cases
        # Move curr and prev pointer to node before left pointer

        # Initialize dummy node to put before head for edge cases
        # Also, create leftPrev and curr pointers where leftPrev = dummy and curr is at head
        dummy = ListNode(0, head)
        leftPrev, curr = dummy, head

        # Shift prev and curr pointers forward until curr reaches left poitner
        for _ in range(left - 1):
            leftPrev = curr
            curr = curr.next

        ##################################################################################

        ### Second section: Reversing section of linked list between left and right pointers
        
        # Use same reversing logic from first reverse linked list problem
        prev = None
        # Iterate through reversed section where (right - left + 1) represents # of nodes in section
        for i in range(right - left + 1):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext

        ##################################################################################

        ### Third Section: Update and clean up pointers from reversed section's nodes

        # Update next pointers for node before left to point at node after right
        leftPrev.next.next = curr
        leftPrev.next = prev
        
        # Return dummy.next node to display entire linked list excluding dummy
        return dummy.next



        

        
