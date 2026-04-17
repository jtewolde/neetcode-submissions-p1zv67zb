# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Synposis: For this problem, we want to find the maximum sum between twin nodes
        # Where nodes are considered twins with two pointers. For example, node 0 and node n - 1 are twins
        # Approach: Use slow and fast pointers techinque to find the middle of the linked list
        # Then, reverse the first half of the linked list and then compute the sum of twin nodes by going outward
        
        # Initialize slow and fast pointers to find the midpoint of the linked list
        # Also, prev variable to pointing at previous node and ans variable for storing maximum sum of twin nodes
        slow, fast = head, head
        prev = None
        ans = 0

        # Find the middle of linked list while reversing the first half at the same time
        while fast and fast.next:
            # Move fast pointer two steps ahead
            fast = fast.next.next
            # Keep track of next node of slow pointer and reverse the link by setting next to prev
            temp = slow.next
            slow.next = prev
            # Update prev to be slow and then move slow forward by setting it to temp
            prev = slow
            slow = temp

        # Traverse both halves of linked list together and computing the sum of twin nodes
        # Update the ans variable with the maximum sum
        while slow:
            ans = max(ans, slow.val + prev.val)
            slow = slow.next
            prev = prev.next

        return ans