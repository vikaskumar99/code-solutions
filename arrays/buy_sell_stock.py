"""
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



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


def brute_force(prices):
    max_diff = -999

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            diff = prices[j] - prices[i]
            # print(prices[j], prices[i], diff, max_diff)
            if diff > max_diff:
                max_diff = diff
    if max_diff < 0:
        return 0
    return max_diff


def better_solution(prices):
    import sys
    min_price = sys.maxsize
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
    return max_profit
