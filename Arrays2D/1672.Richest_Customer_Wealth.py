# Problem Statement
"""
You are given an m x n integer grid accounts where accounts[i][j] is the 
amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that 
the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.
    
    
Example:
    Input: accounts = [[1,2,3],[3,2,1]]
    Output: 6
        
     Explanation:
        - 1st customer has wealth = 1 + 2 + 3 = 6
        - 2nd customer has wealth = 3 + 2 + 1 = 6
        - Both customers are considered the richest with a wealth of 6 each, so return 6.
"""


# Approach
"""
    - Use a for-loop to iterate through lists within the lists
    - Save the sum of integers of current list
    - Compare with the previous highest sum
    - Save the highest sum
    - Return highest sum after iterating through the entire list
"""


# Time Complexity: O(n x m)
# Space Complexity: O(1)


# Code
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest_customer = 0
        
        for account in accounts:
            customer_wealth = sum(account)
           
            if richest_customer < customer_wealth:
                richest_customer = customer_wealth
                
        return richest_customer


# Example usage
if __name__ == "__main__":  
    # Creating a Solution instance 
    solution = Solution()

    # Test Cases
    # accounts = [[1,2,3], [3,2,1]]
    # accounts = [[1,5],[7,3],[3,5]]
    accounts = [[2,8,7],[7,1,3],[1,9,5]]

    # Print results
    print(solution.maximumWealth(accounts))
