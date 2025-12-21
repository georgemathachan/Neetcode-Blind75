# Group Anagrams
# Given an array of strings strs, group the anagrams together.
# You can return the answer in any order.

import unittest
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # --------------------------------------------------
        # Suboptimal solution using sorting
        #
        # Time Complexity:
        #   Let n = number of strings
        #   Let k = average length of a string
        #   Sorting each string costs O(k log k)
        #   Total: O(n * k log k)
        #
        # Space Complexity:
        #   O(n * k) for storing keys and grouped strings
        # --------------------------------------------------
        # anagram_map = defaultdict(list)
        # for word in strs:
        #     key = tuple(sorted(word))  # sorted characters as key
        #     anagram_map[key].append(word)
        # return list(anagram_map.values())

        # --------------------------------------------------
        # Optimal solution using character frequency counts
        #
        # Time Complexity:
        #   Counting characters per string costs O(k)
        #   Total: O(n * k)
        #
        # Space Complexity:
        #   O(n * k) for hash map storage
        # --------------------------------------------------
        anagram_map = defaultdict(list)

        for word in strs:
            # Assuming lowercase English letters
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagram_map[key].append(word)

        return list(anagram_map.values())


class TestGroupAnagrams(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def normalize(self, result: List[List[str]]) -> List[List[str]]:
        """Helper to sort inner lists and outer list for comparison."""
        return sorted([sorted(group) for group in result])

    def test_basic_case(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(self.normalize(self.solution.groupAnagrams(strs)),
                         self.normalize(expected))

    def test_single_string(self):
        strs = ["abc"]
        self.assertEqual(self.solution.groupAnagrams(strs), [["abc"]])

    def test_empty_input(self):
        strs = []
        self.assertEqual(self.solution.groupAnagrams(strs), [])

    def test_no_anagrams(self):
        strs = ["a", "b", "c"]
        expected = [["a"], ["b"], ["c"]]
        self.assertEqual(self.normalize(self.solution.groupAnagrams(strs)),
                         self.normalize(expected))

    def test_all_anagrams(self):
        strs = ["abc", "bca", "cab", "cba"]
        expected = [["abc", "bca", "cab", "cba"]]
        self.assertEqual(self.normalize(self.solution.groupAnagrams(strs)),
                         self.normalize(expected))

    def test_empty_strings(self):
        strs = ["", "", "a"]
        expected = [["", ""], ["a"]]
        self.assertEqual(self.normalize(self.solution.groupAnagrams(strs)),
                         self.normalize(expected))


if __name__ == '__main__':
    unittest.main()
