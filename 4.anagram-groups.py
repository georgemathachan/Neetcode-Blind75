from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))  # use tuple of sorted characters as key
            anagram_map[key].append(word)
        return list(anagram_map.values())
