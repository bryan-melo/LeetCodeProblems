# Problem Statement
"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.


Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

"""

# Approach
"""
Approach 1:

    - Perform in-place modifications and return the original array with updated values.
        - Iterate through array, starting at index 1
        - Add the previous index value to the current index value
    - Return updated array
    

Approach 2: 

    - Create a new array
    - Create a variable to keep track of the sum of the previous index
        - count will store the sum of previous value and will be used to add to the current value
    - Return the new array

"""
# Approach 1
# Time Complexity: O(N)
# Space Complexity: O(1)

# Approach 2
# Time Complexity: O(N)
# Space Complexity: O(N)

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Approach 1: Returning existing list with in-place modifications
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        return nums
        
        """
        # Approach 2: Returning a new list
        
        newList = list()
        newList.append(nums[0])
        
        for i in range(1, len(nums)):
            newList.append(nums[i] + newList[i - 1])

        return newList
        """
    
# Example usage
if __name__ == "__main__":  
    # Creating a Solution instance 
    solution = Solution()
    
    # Printing results
    print(solution.runningSum([1,2,3,4]))
