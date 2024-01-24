# Approach
""" 
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""


# Approach
""" 
    - Initialize a variable (count) that will store the number of nodes in linked list
    - Initiliaze another variable (check) that will be used to compare to count
    - Initialize an empty node (new_head)
    - Save the head of linked list
    - Iterate through linked list
        * Increment count if node exist
    - Divide count by 2
    - Iterate though linked list
        * when check == count, assign node to new_head
        * keep iterating through linked list until None is reached, add each node to new_linked_list
    - Return new_linked_list
    
"""


# Time Complexity: O(N)
# Space Complexity O(N)


# Code
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        check = 0
        
        count = Solution.countNodes(temp)
        count = count / 2
        
        print(count)
        return temp
        
        
        
    
    def countNodes(self, head: Optional[ListNode]) -> int:
        count = 0
        
        while head:
            count += 1
            head = head.next

        return count        
        

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