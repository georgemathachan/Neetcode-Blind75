# Two Sum
# Given an array of integers nums and an integer target, return the indices
# i and j such that nums[i] + nums[j] == target and i != j.
#
# You may assume that every input has exactly one solution.
# Return the answer with the smaller index first.

import unittest
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # --------------------------------------------------
        # Brute-force solution (O(n^2)) — suboptimal
        # --------------------------------------------------
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # --------------------------------------------------
        # Optimal hash-map solution (O(n))
        # --------------------------------------------------
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i


class TestTwoSum(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_basic_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_unsorted_array(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])

    def test_with_duplicates(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        self.assertEqual(self.solution.twoSum(nums, target), [2, 4])

    def test_zero(self):
        nums = [0, 4, 3, 0]
        target = 0
        self.assertEqual(self.solution.twoSum(nums, target), [0, 3])


if __name__ == '__main__':
    unittest.main()
