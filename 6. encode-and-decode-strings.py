from typing import List

class Solution:
    def __init__(self):
        # Store lengths and final string as instance variables
        self.lengths = []
        self.final_string = ""

    def encode(self, strs: List[str]) -> str:
        self.lengths = []
        self.final_string = ""
        for i in strs:
            current = str(i)
            self.final_string += current
            length = 0
            for _ in current:
                length += 1
            self.lengths.append(length)
        return self.final_string

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        for length in self.lengths:
            output.append(s[i:i+length])
            i += length
        return output


# ---------------- TEST CASES ----------------
sol = Solution()

# Example 1
input1 = ["neet","code","love","you"]
encoded1 = sol.encode(input1)
decoded1 = sol.decode(encoded1)
print("Input:", input1)
print("Encoded:", encoded1)
print("Decoded:", decoded1)
print("Pass?" , decoded1 == input1)
print()

# Example 2
sol = Solution()  # new instance so lengths don’t clash
input2 = ["we","say",":","yes"]
encoded2 = sol.encode(input2)
decoded2 = sol.decode(encoded2)
print("Input:", input2)
print("Encoded:", encoded2)
print("Decoded:", decoded2)
print("Pass?" , decoded2 == input2)
