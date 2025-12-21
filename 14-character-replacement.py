"""
Longest Repeating Character Replacement
----------------------------------------
Solved

Problem:
--------
You are given a string s consisting of only uppercase English characters and an integer k.
You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Examples:
---------
Example 1:
Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:
Input: s = "AAABABB", k = 1
Output: 5
Explanation: We can replace one 'B' in the substring "AAABB" to get "AAAAA".

Constraints:
------------
1 <= s.length <= 1000
0 <= k <= s.length

Approach:
---------
Sliding Window + Character Frequency
1. Maintain a window [left, right] and a frequency count of characters inside it.
2. Track `max_freq`, the count of the most frequent character inside the window.
3. If (window_size - max_freq) > k, it means we need to replace more than k characters to make
   the entire window a single character. In this case, shrink the window from the left.
4. The maximum window size seen while keeping the condition valid is our answer.

Why it works:
-------------
The key insight is that we don't need to know *which* character we end up with.
We only need to ensure that the number of characters that need replacement does not exceed k.

Complexity:
-----------
Time: O(n)  – Each character is visited at most twice (once added, once removed).
Space: O(1) – Frequency dictionary has at most 26 entries for uppercase English letters.
"""

from collections import defaultdict
import unittest

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)   # frequency of characters in current window
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] += 1
            # track the highest frequency of a single character in the current window
            max_freq = max(max_freq, count[s[right]])

            # if replacements needed > k, shrink window from the left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # update answer
            max_len = max(max_len, right - left + 1)

        return max_len


# ---------------------- Unit Tests ---------------------- #
class TestCharacterReplacement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        self.assertEqual(self.sol.characterReplacement("XYYX", 2), 4)

    def test_example2(self):
        self.assertEqual(self.sol.characterReplacement("AAABABB", 1), 5)

    def test_all_same(self):
        # No replacement needed, longest substring is full length
        self.assertEqual(self.sol.characterReplacement("AAAA", 2), 4)

    def test_no_replacement(self):
        # k=0 means we can't replace anything, so answer is the longest run of same char
        self.assertEqual(self.sol.characterReplacement("ABAB", 0), 1)

    def test_mixed_chars(self):
        # Replace one char to get "BBBB"
        self.assertEqual(self.sol.characterReplacement("AABBB", 1), 4)

    def test_empty_k(self):
        # k can be zero, but we still need to handle single-character windows
        self.assertEqual(self.sol.characterReplacement("XYZ", 0), 1)

    def test_large_k(self):
        # Large k allows converting entire string to one char
        self.assertEqual(self.sol.characterReplacement("XYZ", 10), 3)


if __name__ == "__main__":
    unittest.main(argv=[''], verbosity=2, exit=False)
