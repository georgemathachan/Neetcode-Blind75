####Valid Anagram
###Given two strings s and t, return true if the two strings are anagrams
#  of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as 
# another string, but the order of the characters can be different.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == len(t) == 0:
            return True
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            return True
        return False
