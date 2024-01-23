# Approach
""" 
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""


# Approach
""" 

"""


# Time Complexity:
# Space Complexity


# Code
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = list()
        
        while head != None:
            new_list.append(head.val)
    

# Example usage
if __name__ == "__main__":  
    # Creating a Solution instance 
    solution = Solution()
    
    # Create Linked list
    head = ListNode(1)
    
    # Printing results    
    