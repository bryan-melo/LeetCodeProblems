# Problem Statement
""" 
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""


# Approach
""" 
    - Initialize middle_node and assign it to the head of linked list being passed
    - Use while-loop to iterate linked-list while making sure the current and
      next nodes are not None.
    - while-loop logic:
        - Advance middle_node pointer for every two advances in head pointer
        - Example:
            * head = [1, 2, 3, 4, 5]                       # head.val = 1
            * middle_node = head                           # middle_node.val = 1
            * Advance the head pointer by two nodes        # head.val = 3
            * Advance the middle_node pointer by one node  # middle_node.val = 2
            * Advance the head pointer by two nodes        # head.val = 5
            * Advance the middle_node pointer by one node  # middle_node.val = 3
            * etc.
"""


# Time Complexity: O(N)
# Space Complexity O(1)


# Code
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        middle_node = head
        
        while head and head.next != None:
            head = head.next
            head = head.next
            middle_node = middle_node.next
            
        return middle_node
        

# Example usage
if __name__ == "__main__":  
    # Creating a Solution instance 
    solution = Solution()
    
    # Create Nodes
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    # Create Linked-List
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    # Printing results    
    head = solution.middleNode(node1)
    
    current = head
    
    while current:
        print(current.val)
        current = current.next
        