# Problem Statement
"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 
 
Example:
    Input: n = 3
    Output: ["1","2","Fizz"]
"""


# Approach
""" 
    Numbers divisible by 3:
        - 3, 6, 9, 12, 15, etc.
    Numbers divisible by 5:
        - 5, 10, 15, 20, etc.
    Numbers divisible by 3 and 5:
        - 15, 30, 45, 60, etc.
      
    - Initialize an integer variable to 1, this will be used to iterate from 1 to n
    - Use a while-loop to iterate from 1 to n.
        * Use modulo operator  to figure out if 'i' is divisible by 3, 5, or 3 & 5 
        * Add the corresponding string to the list that will be returned.
    - while-loop logic:
        * if remainder is 0 for both 3 and 5, add "FizzBuzz" to list
        * else if remainder is 0 for 3, add "Fizz" to list
        * else if remainder is 0 for 5, return "Buzz"
        * else remainder is not zero for any of them, return 'i'
    - Return list
"""


# Time Complexity: O(N)
# Space Complexity: O(1)


# Code
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_buzz_list = list()
        i = 1
        
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                fizz_buzz_list.append("FizzBuzz")
            elif i % 3 == 0:
                fizz_buzz_list.append("Fizz")
            elif i % 5 == 0:
                fizz_buzz_list.append("Buzz")
            else:
                fizz_buzz_list.append(str(i))    
            i += 1
            
        return fizz_buzz_list
    
    
# Example usage
if __name__ == "__main__":  
    # Creating a Solution instance 
    solution = Solution()
    
    # Print results
    print(solution.fizzBuzz(3))     # n = 3
    print(solution.fizzBuzz(5))     # n = 5
    print(solution.fizzBuzz(15))    # n = 15