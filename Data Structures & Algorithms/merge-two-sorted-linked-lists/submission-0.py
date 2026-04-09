# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initial approach for this problem:

        # Create a temp/dummy node to keep track of the head of the resulting linked list
        # Iterate through both linked lists
       
        # Compare the values of list1 and list2, if list1.val < list2.val, set temp.next to list1 and set list1 to list1.next
        # Do the same thing above for list2
        # After conditionals, update dummy node to the next node of dummy
        # If either lists are empty, take remaining porton of list and add to end of temp list

        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next

        node.next = list1 or list2

        return dummy.next









