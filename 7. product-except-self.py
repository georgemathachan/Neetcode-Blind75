from typing import List

"""
Given an integer array nums, return an array output where output[i] 
is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: Build prefix products
        prefixes = [1] * n
        for i in range(1, n):
            prefixes[i] = prefixes[i-1] * nums[i-1]

        # Step 2: Build suffix products
        suffixes = [1] * n
        for i in range(n-2, -1, -1):
            suffixes[i] = suffixes[i+1] * nums[i+1]

        # Step 3: Multiply prefix and suffix for each index
        output = [prefixes[i] * suffixes[i] for i in range(n)]
        return output


# ---------------- TEST CASES ----------------
sol = Solution()

# Example 1
nums1 = [1,2,4,6]
print("Input:", nums1)
print("Output:", sol.productExceptSelf(nums1))
# Expected: [48,24,12,8]

# Example 2
nums2 = [-1,0,1,2,3]
print("\nInput:", nums2)
print("Output:", sol.productExceptSelf(nums2))
# Expected: [0,-6,0,0,0]
