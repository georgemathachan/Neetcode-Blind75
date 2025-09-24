"""
Best Time to Buy and Sell Stock (NeetCoin)
------------------------------------------
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose:
- A single day to BUY one NeetCoin
- A different future day to SELL it

Return the maximum profit you can achieve.
If no profitable transaction exists, return 0.

Constraints:
------------
1 <= prices.length <= 100
0 <= prices[i] <= 100

Examples:
---------
Example 1:
Input:  prices = [10,1,5,6,7,1]
Output: 6
Explanation: Buy prices[1] (price = 1) and sell prices[4] (price = 7)
Profit = 7 - 1 = 6.

Example 2:
Input:  prices = [10,8,7,5,2]
Output: 0
Explanation: No profitable transactions can be made.

----------------------------------------------------------
Naive (Quadratic) Approach:
----------------------------------------------------------
Loop through each possible selling day (i), and for each day
find the minimum price among all earlier days to simulate buying
on the best earlier day.

Pseudocode:
    max_profit = 0
    for i from n-1 down to 1:
        sell = prices[i]
        buy  = min(prices[:i])   # O(i)
        update max_profit

Time Complexity  : O(n^2) because min() is called inside the loop
Space Complexity : O(1)
This is acceptable for n <= 100 but inefficient for large n.

----------------------------------------------------------
Optimized O(n) Solution:
----------------------------------------------------------
Instead of repeatedly finding the minimum for each day,
track the lowest price seen so far and update the maximum profit
at each step.

Algorithm:
----------
1. Initialize min_price = +∞
2. Initialize max_profit = 0
3. For each price:
       min_price  = min(min_price, price)
       max_profit = max(max_profit, price - min_price)
4. Return max_profit

Time Complexity  : O(n)
Space Complexity : O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')   # Lowest buy price encountered
        max_profit = 0             # Highest profit so far

        for price in prices:
            min_price = min(min_price, price)           # Update lowest buy price
            max_profit = max(max_profit, price - min_price)  # Check profit if selling today
        return max_profit


# --------------------
# Test Cases
# --------------------
if __name__ == "__main__":
    s = Solution()

    # Example 1
    print(s.maxProfit([10,1,5,6,7,1]))  # Expected: 6
    # Explanation: Buy at 1 (day 1), sell at 7 (day 4) → Profit = 6

    # Example 2
    print(s.maxProfit([10,8,7,5,2]))    # Expected: 0
    # Explanation: Prices keep falling → No profit possible

    # Edge Case 1: Single day
    print(s.maxProfit([5]))             # Expected: 0
    # Can't sell on a future day.

    # Edge Case 2: Constant prices
    print(s.maxProfit([3,3,3,3]))       # Expected: 0
    # No price increase at any time.

    # Edge Case 3: Best buy at start, best sell at end
    print(s.maxProfit([1,2,3,4,5]))     # Expected: 4
    # Buy at 1, sell at 5 → Profit = 4
