# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
#   You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time.
# You must sell before buying again.


def buy_sell_stock1(data):
    # profit = 0
    # for i in range(len(data)-1):
    #     if data[i+1] > data[i]:
    #         profit += (data[i+1] - data[i])
    # return profit

    max_price = 0
    for i in range(len(data)-1):
        max_price += max(data[i+1] - data[i], 0)  # get the max from (SELL - BUY) else set to 0
    return max_price


a = [7, 1, 5, 3, 6, 4]
print(buy_sell_stock1(a))
