from typing import List

"""
Longest Consecutive Sequence

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        longest_count = 1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 0:
                continue 
            if nums[i] - nums[i-1] == 1:
                count += 1
            else: 
                longest_count = max(longest_count, count)
                count = 1
        
        return max(longest_count, count)


# ---------------- TEST CASES ----------------
sol = Solution()

# Example 1
nums1 = [2,20,4,10,3,4,5]
print("Input:", nums1)
print("Output:", sol.longestConsecutive(nums1))
# Expected: 4 (sequence: [2,3,4,5])

# Example 2
nums2 = [0,3,2,5,4,6,1,1]
print("\nInput:", nums2)
print("Output:", sol.longestConsecutive(nums2))
# Expected: 7 (sequence: [0,1,2,3,4,5,6])

# Additional tests
nums3 = [100, 4, 200, 1, 3, 2]
print("\nInput:", nums3)
print("Output:", sol.longestConsecutive(nums3))
# Expected: 4 (sequence: [1,2,3,4])

nums4 = []
print("\nInput:", nums4)
print("Output:", sol.longestConsecutive(nums4))
# Expected: 0
