"""
LeetCode Problem: Best Time to Buy and Sell Stock

Calculates the maximum profit that can be achieved from a single buy and sell operation on a list of stock prices.
Iterates through the list, tracking the minimum price seen so far and the maximum profit achievable at each step.

Args:
    prices (List[int]): List of stock prices where prices[i] is the price of a given stock on day i.

Returns:
    int: The maximum profit that can be achieved. Returns 0 if no profit is possible.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1 # left=buy, right=sell
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else:
                l = r # we found prices lower than current, so we want to buy here
            r += 1 # increment sell
        return maxProfit


# Intuition:
# The algorithm uses a two-pointer technique to track the minimum price seen so far (left pointer) and the current price (right pointer).
# It calculates the profit at each step and updates the maximum profit accordingly.
    
# Time Complexity: O(n), where n is the number of elements in prices.
# Space Complexity: O(1), as we are using only a constant amount of space for variables.
