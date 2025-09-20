from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        3Sum Problem
        -------------
        Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
        such that:
            • i, j, and k are distinct indices
            • nums[i] + nums[j] + nums[k] == 0
        The output must contain **no duplicate triplets**.
        
        Approach:
        ---------
        1. Sort the array to simplify duplicate handling and enable two-pointer search.
        2. Iterate through the array:
            - Skip duplicate first elements to avoid repeating the same triplet base.
        3. For each base element nums[i], use two pointers (left, right) to find pairs
           that sum to -nums[i].
            - Move pointers inward depending on whether the current sum is too small or too large.
            - Skip duplicate second/third numbers after finding a valid triplet.
        Complexity:
        -----------
        Time:  O(n^2)   (sorting + two-pointer scan for each element)
        Space: O(1)     (ignoring output list)
        """
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # Skip duplicate first numbers to prevent duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate second numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate third numbers
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res


# -------------------- TEST CASES --------------------

def run_tests():
    sol = Solution()
    
    # Example 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    print("Input:", nums1)
    print("Output:", sol.threeSum(nums1))
    # Expected: [[-1, -1, 2], [-1, 0, 1]]
    print()

    # Example 2
    nums2 = [0, 1, 1]
    print("Input:", nums2)
    print("Output:", sol.threeSum(nums2))
    # Expected: []
    print()

    # Example 3
    nums3 = [0, 0, 0]
    print("Input:", nums3)
    print("Output:", sol.threeSum(nums3))
    # Expected: [[0, 0, 0]]
    print()

    # Additional Test 1: duplicates that still form valid triplets
    nums4 = [-2, -2, 4, 0, 0]
    print("Input:", nums4)
    print("Output:", sol.threeSum(nums4))
    # Expected: [[-2, -2, 4], [0, 0, 0]] (if enough zeros exist) or [[-2,-2,4]]
    print()

    # Additional Test 2: no valid triplets
    nums5 = [5, 7, 9]
    print("Input:", nums5)
    print("Output:", sol.threeSum(nums5))
    # Expected: []
    print()

    # Additional Test 3: multiple zero combinations
    nums6 = [0,0,0,0]
    print("Input:", nums6)
    print("Output:", sol.threeSum(nums6))
    # Expected: [[0,0,0]]
    print()


# Run tests when file is executed
if __name__ == "__main__":
    run_tests()
