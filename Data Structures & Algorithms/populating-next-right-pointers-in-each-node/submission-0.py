"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Approach: Use a optimal BFS techinque to traversing through the BST by each level
        # Instead of using a queue, use the next pointers that were established to traverse each level
        
        # Initialize curr and nxt pointers for tracking position in BST and traversing through
        # Curr pointer will be the current node being processed
        # Nxt pointer represents the leftmost node/children of curr pointer of the next level in BST
        curr, nxt = root, root.left if root else None

        # Continously traverse through BST at each level while both pointers aren't null
        while curr and nxt:
            # Set the next pointer for curr's left children to the right children 
            curr.left.next = curr.right

            # Check if the next pointer of the curr node exists or not,
            # If so, make the next pointer of the right child be the next node's left child
            if curr.next:
                curr.right.next = curr.next.left
            
            # Move the curr pointer to the next node in the same level
            # If there is no next node, then move both pointers down a level in BST
            curr = curr.next
            if not curr:
                curr = nxt
                nxt = curr.left
        return root
