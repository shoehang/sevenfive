'''
Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

class Solution(object):
    def maxProfit(self, prices):

        # initial minimum, profit is 0 (not 'sold' yet)
        minPrice= prices[0]
        profit = 0

        for price in prices[1:]:
            # update profit using max of current profit or 'next day' price - minimum price
            profit = max(profit, price - minPrice)

            # update minimum price after we calculte profit (cant sell before buy)
            minPrice = min(minPrice, price)

        return profit     