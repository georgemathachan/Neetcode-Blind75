"""
Longest Substring Without Repeating Characters
----------------------------------------------
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:
----------
Input:  s = "zxyzxyz"
Output: 3
Explanation:
The string "xyz" is the longest substring without duplicate characters.

Example 2:
----------
Input:  s = "xxxx"
Output: 1
Explanation:
The longest substring without duplicate characters is "x" of length 1.

Constraints:
------------
0 <= s.length <= 1000
s may consist of printable ASCII characters.

Approach:
---------
Use a sliding window with a set to track unique characters.
- Expand the window by moving the right pointer.
- If a duplicate is found, shrink the window from the left until the duplicate is removed.
- Track the maximum window size at each step.

Time Complexity:  O(n)  -> Each character is visited at most twice (once by left, once by right).
Space Complexity: O(k)  -> k is the size of the character set (<= n).
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()       # Stores unique characters in the current window
        left = 0           # Left boundary of the window
        max_len = 0        # Maximum length of substring without duplicates
        
        for right in range(len(s)):
            # Shrink window if s[right] is already in the set
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # Add current character and update max_len
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len


# -------------------------
# Tests
# -------------------------
def test_length_of_longest_substring():
    sol = Solution()
    # Provided examples
    assert sol.lengthOfLongestSubstring("zxyzxyz") == 3   # "xyz"
    assert sol.lengthOfLongestSubstring("xxxx") == 1      # "x"
    # Additional tests
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3  # "abc"
    assert sol.lengthOfLongestSubstring("bbbbb") == 1     # "b"
    assert sol.lengthOfLongestSubstring("pwwkew") == 3    # "wke"
    assert sol.lengthOfLongestSubstring("") == 0          # ""
    assert sol.lengthOfLongestSubstring("au") == 2        # "au"
    assert sol.lengthOfLongestSubstring("dvdf") == 3      # "vdf"
    assert sol.lengthOfLongestSubstring("anviaj") == 5    # "nviaj"
    print("✅ All tests passed!")


# Run tests
test_length_of_longest_substring()
