# Problem Statement
"""
You are given the root of a binary tree that consists of exactly 3 nodes: 
    - the root
    - its left child
    - its right child

Return true if the value of the root is equal to the sum of the values of its two children, 
or false otherwise. 
"""


# Approach
"""
    - Start from Root node: check if node is empty/None, return false if empty.
    - Check children nodes: 
        * if one of them is empty, assign the value of 0, 
        * otherwise assign the value of each children node to a corresponding variable
    - Check sum and return: 
        * True if both children sum up to the root, 
        * otherwise return false.
"""


# Time complexity: O(1)
# Space complexity: O(1)


# Code
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
        Solution class to check if the sum of the left & right child nodes equal the root node.
    """
    def checkTree(self, root: Optional[TreeNode]) -> bool:        
        if root is None:
            return False
        
        left = root.left.val if root.left else 0
        right = root.right.val if root.right else 0
        
        return root.val == left + right
    
    
# Example usage:
if __name__ == "__main__":
    # Creating TreeNode with Root & both Left and Right Children
    root1 = TreeNode(10, TreeNode(4), TreeNode(6))   # (Root, Left_Child, Right_Child)
    root2 = TreeNode(10, TreeNode(5), TreeNode(10))
    root3 = TreeNode(10, None, TreeNode(6))
    root4 = TreeNode(10, TreeNode(4), None)
    root5 = TreeNode(10, TreeNode(5), TreeNode(5))
    
    # Creating a Solution instance
    solution = Solution()
    
    # Print results
    print(solution.checkTree(root1))
    print(solution.checkTree(root2))
    print(solution.checkTree(root3))
    print(solution.checkTree(root4))
    print(solution.checkTree(root5))
      