### Contains Duplicate
### Given an integer array nums, return true if any value
### appears more than once in the array, otherwise return false.

import unittest
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Original brute-force solution (O(n^2))
        # for i in range(0, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Set-based solution
        # set_nums = set(nums)
        # if len(nums) == len(set_nums):
        #     return False
        # else:
        #     return True

        # Pythonic concise solution (O(n))
        return len(nums) != len(set(nums))


class TestHasDuplicate(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 2, 3, 3]
        self.assertTrue(self.solution.hasDuplicate(nums))

    def test_example2(self):
        nums = [1, 2, 3, 4]
        self.assertFalse(self.solution.hasDuplicate(nums))


if __name__ == '__main__':
    unittest.main()
