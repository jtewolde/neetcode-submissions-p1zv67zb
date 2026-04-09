# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initial Approach: Convert linked list into an ordinary list,
        # Use Two pointers approach to traverse through the list.
        # See if character at each pointer are the same. If so, move pointers inward
        # If not, return False.
        
        # Create curr variable for traversing through linked list and palin array for two pointers
        curr = head
        palin = []

        # Traverse through linked list and store each node's value in palin array
        while curr:
            palin.append(curr.val)
            curr = curr.next

        # Initialize left and right pointers for two pointers traversal
        left, right = 0, len(palin) - 1

        # Iterate through palin array with left and right pointers
        # If characters at both pointers are the same, move pointers inward
        # Else, return False as final answer
        while left <= right:
            if palin[left] == palin[right]:
                left += 1
                right -= 1
            else:
                return False

        return True


