"""
Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
prices=[7,1,5,3,6,4]
current_profit=0
final_profit=0
n=len(prices)
for i in range(n):
    for j in range(i+1,n):
        current_profit=prices[j]-prices[i]
        final_profit=max(current_profit,final_profit)

print(final_profit)
