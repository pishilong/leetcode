from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        buy = None
        profit = 0
        pre = prices[0]
        for price in prices[1:]:
            if price > pre: #上涨
                if buy is None:
                    buy = pre
            else: #开始下跌了
                if buy is not None: #有买入
                    profit += pre - buy # 卖出
                    buy = None
            pre = price

        if buy is not None: # 有买入，但结束了还没卖出，说明一直上涨
            profit += prices[-1] - buy

        return profit

if __name__ == '__main__':
    solution = Solution()
    # ex = [7,1,5,3,6,4]
    # ex = [1,2,3,4,5]
    ex = [7,6,4,3,1]
    print(solution.maxProfit(ex))
