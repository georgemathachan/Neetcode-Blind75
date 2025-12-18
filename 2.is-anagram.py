### Valid Anagram
### Given two strings s and t, return true if t is an anagram of s, and false otherwise.

import unittest
from typing import List
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # --------------------------------------------------
        # Original sorting-based solution (O(n log n))
        # --------------------------------------------------
        # if len(s) != len(t):
        #     return False
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # return sorted_s == sorted_t

        # --------------------------------------------------
        # Manual character counting solution (O(n))
        # --------------------------------------------------
        # if len(s) != len(t):
        #     return False
        #
        # count = {}
        #
        # for c in s:
        #     count[c] = count.get(c, 0) + 1
        #
        # for c in t:
        #     if c not in count:
        #         return False
        #     count[c] -= 1
        #     if count[c] < 0:
        #         return False
        #
        # return True

        # --------------------------------------------------
        # Pythonic + optimal solution (O(n))
        # --------------------------------------------------
        return Counter(s) == Counter(t)


class TestIsAnagram(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_basic_true(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))

    def test_basic_false(self):
        self.assertFalse(self.solution.isAnagram("rat", "car"))

    def test_different_lengths(self):
        self.assertFalse(self.solution.isAnagram("abc", "ab"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isAnagram("", ""))

    def test_single_character(self):
        self.assertTrue(self.solution.isAnagram("a", "a"))
        self.assertFalse(self.solution.isAnagram("a", "b"))

    def test_repeated_characters(self):
        self.assertTrue(self.solution.isAnagram("aabbcc", "baccab"))

    def test_case_sensitivity(self):
        self.assertFalse(self.solution.isAnagram("Listen", "Silent"))


if __name__ == '__main__':
    unittest.main()
