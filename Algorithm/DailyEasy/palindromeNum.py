"""

9. Palindrome Number

Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""

import math

def isPalindrome(x):

    string = str(x)
    midPoint = math.floor(len(string)/2)
    
    j = len(string) - 1
    for i in range(0, midPoint, 1): 
        if string[i] != string[j]:
            return False
        
        j -= 1
    
    return True

ans = isPalindrome(11)
print(ans)
