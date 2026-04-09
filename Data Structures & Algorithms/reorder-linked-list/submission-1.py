# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Techinque to solving this linked list problem is by using fast and slow pointers
        # Synposis: Find the middle node of the linked list by using fast and slow pointers ans split it in two halves
        # Then, reverse the second half of the linked list
        # Finally, merge the two halves of the list alternatively
        # Example: [0, 1, 2, 3, 4, 5] --> [0, 5, 1, 4, 2, 3]

        # Initialize fast and slow pointers
        fast = slow = head

        # Step 1: Locate the midpoint of the linked list
        # Go through linked list until fast pointer lands on null/Tail of list
        # Slow pointer at the end will be the middle node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split the linked list into two halves
        # Use second_half variable to keep track of middle node while disconnecting second half to first half
        second_half = slow.next
        slow.next = None

        # Step 3: Reverse the second half of linked list
        # Create previous variable to keep track of previous nodes
        # Set temp pointer to hold second half's next,
        # Set current node to previous = None
        # Then, set the previous.next to current node of second half and second half to temp
        # Move both pointers forward
        previous = None
        current = second_half
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        # Step 4: Merge both halves alteratively

        # Initialize pointers for both first and second halves
        reversed_second_half = previous
        first_half = head

        # Save the next node of second half to temp
        # Insert the second half node after current node from first half of list
        # Set the next node of first half to point to second half node
        # Move forward two next alternating nodes
        while reversed_second_half:
            # Save both next nodes
            first_half_next = first_half.next
            second_half_next = reversed_second_half.next
            
            # Connect the nodes alternativerly
            first_half.next = reversed_second_half
            reversed_second_half.next = first_half_next

            first_half = first_half_next
            reversed_second_half = second_half_next


