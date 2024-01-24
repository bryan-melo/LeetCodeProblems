# Problem Statement
""" 
Given an integer: num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, 
otherwise, you have to subtract 1 from it. 

 
Example 1:

    Input: num = 14
    Output: 6

    Explanation: 
        - Step 1) 14 is even; divide by 2 and obtain 7. 
        - Step 2) 7 is odd; subtract 1 and obtain 6.
        - Step 3) 6 is even; divide by 2 and obtain 3. 
        - Step 4) 3 is odd; subtract 1 and obtain 2. 
        - Step 5) 2 is even; divide by 2 and obtain 1. 
        - Step 6) 1 is odd; subtract 1 and obtain 0.
"""


# Approach
""" 
    Approach 1 (using modulo):
        - Use a while loop to iterate from num to zero
        - Initialize step_count to keep track of the number of steps to reach zero
        - while-loop logic:
            * if num % 2 == 0 then divide by 2
            * else subtract by 1
            * increment step_count by 1
        - return step_count
        
    Approach 2 (using bitwise operations):
        - Use a while loop to iterate from num to zero
        - Initialize step_count to keep track of the number of steps to reach zero
        - while-loop logic:
            * Compare the least significant to check if it is set to zero
                - if zero then num is an even number
                - if one then numn is an odd number
                    * By setting the least significant number to zero, 
                    * it becomes equivalent to subtracting 1 to num when it is an odd number
            * if least significant bit is zero, then shift 2 bits to the right
                - This is equivalent to num / 2^1 when using 'num = num >> 1'
                    * Note: num = num >> y is equivalent to num / 2^y
            * else, if least significant bit is one then set it to zero
                - This is equivalent to subtracting 1 from num
            * increment step_count by 1
        - Return step_count
"""


# Approach 1 & 2
# Time Complexity: O(log N)
# Space Complexity: O(1)


# Code
class Solution:
    def numberOfSteps(self, num: int) -> int:
        step_count = 0
        
        while num > 0:
            # Using modulo
            """
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            step_count = step_count + 1
            """
            
            # Using bitwise operations
            if num & 1 == 0:    # Compares least significant bit to zero
                num = num >> 1   # Shifts 2 bits to the right
            else:
                num &= num - 1  # Sets the least significant bit to 0
            step_count = step_count + 1
            
        return step_count
    
    
# Example usage:
if __name__ == "__main__":
    # Creating a Solution instance
    solution = Solution()
    
    # Print results
    print(solution.numberOfSteps(14))       # Output: 6
    print(solution.numberOfSteps(8))        # Output: 4
    print(solution.numberOfSteps(123))      # Output: 12
    