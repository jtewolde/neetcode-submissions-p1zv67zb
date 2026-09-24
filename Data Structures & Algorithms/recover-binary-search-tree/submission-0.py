# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Approach: Use DFS and in order traversal to traverse through the entire BST and enter all nodes into a list
        # In-order traversal will reveal the nodes that are swapped and not in correct order that need to be swapped
        
        # Create arr list to store the nodes from inorder traversal aftermath
        arr = []

        # Create in order traversal function that goes through the BST in the "sorted" order that is suppose to be
        # By starting with going from left to right
        def inorder(node):
            if not node:
                return

            inorder(node.left)
            arr.append(node)
            inorder(node.right)

        # Call the inorder function on the root node,
        # Initialize two nodes as None for swapping nodes not in order
        inorder(root)
        node1, node2 = None, None

        # Scan through the arr list to find the inversions/places where nodes are out of place
        for indx in range(len(arr) - 1):
            # Compare two nodes next to each other to see if the current node is greater than next node in arr
            # Set node2 to the next node in arr with indx
            if arr[indx].val > arr[indx + 1].val:
                node2 = arr[indx + 1]

                # Set node1 to the current node if there is none in node1
                if node1 is None:
                    node1 = arr[indx]
                else:
                    break
        # Swap the values of node1 and node2 to restore the BST.
        node1.val, node2.val = node2.val, node1.val




