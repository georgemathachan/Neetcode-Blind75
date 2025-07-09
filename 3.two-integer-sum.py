#Two Sum
#Solved 
#Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

#Return the answer with the smaller index first.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if target - nums[i] == nums[j]:
                    return [i,j]
        