from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies manually
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # Step 2: Convert frequency map to a list of (num, freq) pairs
        freq_list = []
        for num in freq_map:
            freq_list.append([num, freq_map[num]])

        # Step 3: Sort the list by frequency in descending order
        freq_list.sort(key=lambda x: x[1], reverse=True)

        # Step 4: Extract top k elements
        result = []
        for i in range(k):
            result.append(freq_list[i][0])
        
        return result

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(s.topKFrequent([4,1,-1,2,-1,2,3], 2))  # Output: [-1, 2]
