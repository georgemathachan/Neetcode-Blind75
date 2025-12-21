from typing import List

"""
Valid Palindrome

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Constraints:
1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower()
        clean_text = ''.join(char for char in text if char.isalnum())
        
        for i in range(1, int(len(clean_text)+1/2) + (len(clean_text) % 2 > 0)):
            if clean_text[i-1] == clean_text[-i]:
                continue
            else:
                return False
        return True


# ---------------- TEST CASES ----------------
sol = Solution()

# Example 1
s1 = "Was it a car or a cat I saw?"
print("Input:", s1)
print("Output:", sol.isPalindrome(s1))
# Expected: True

# Example 2
s2 = "tab a cat"
print("\nInput:", s2)
print("Output:", sol.isPalindrome(s2))
# Expected: False

# Additional tests
s3 = "A man, a plan, a canal: Panama"
print("\nInput:", s3)
print("Output:", sol.isPalindrome(s3))
# Expected: True

s4 = "race a car"
print("\nInput:", s4)
print("Output:", sol.isPalindrome(s4))
# Expected: False

s5 = "0P"
print("\nInput:", s5)
print("Output:", sol.isPalindrome(s5))
# Expected: False
