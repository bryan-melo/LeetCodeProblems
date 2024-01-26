# Problem Statement
""" 
Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
    Input: ransomNote = "a", magazine = "b"
    Output: false

Example 2:
    Input: ransomNote = "aa", magazine = "ab"
    Output: false
"""


# Approach
"""
    - Store individual characters of ransomNote into Dictionary
    - Search for each character in Dictionary and return true if
      characters exists
    - Otherwise return false
"""


# Time Complexity: O(N)
# Space Complexity: O(N)


# Code
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        my_dict = {}
        
        
    
    
# Example usage
if __name__ == "__main__":  
    # Creating a Solution instance 
    solution = Solution()
    
    solution.canConstruct("hello", "hi")