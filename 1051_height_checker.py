from typing import List
import utils

# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         cur_order = sorted(heights)

#         ans = 0
#         for idx, height in enumerate(cur_order):
#             if heights[idx] != height:
#                 ans += 1
#         return ans

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        bucket = [0] * 101
        for height in heights:
            bucket[height] += 1

        ans = 0
        j = 0
        for i in range(1, 101):
            while bucket[i] > 0:
                if heights[j] != i:
                    ans += 1
                j += 1
                bucket[i] -= 1

        return ans

cases = [
    {
        'input': [[1,1,4,2,1,3]],
        'result': 3,
    },
    {
        'input': [[5,1,2,3,4]],
        'result': 5,
    },
    {
        'input': [[1,2,3,4,5]],
        'result': 0,
    },
    {
        'input': [[23,52,46,7,50,87,20,32,85,65,62,34,8,86,15,66,66,30,11,96,18,26,24,10,57,13,37,69,85,6,8,17,40,88,14,72,85,51,40,38,54,65,65,27,18,59,77,12,25,46,10,19,10,28,64,79,5,88,2,1,14,50,91,34,58,32,90,67,28,81,84,76,88,45,42,54,59,56,20,6,56,51,72,69,6,48,67,68,6,10,93,69,4,29,28]],
        'result': 95,
    },
    {
        'input': [[31,81,41,78,48,2,83,48,21,20,43,15,26,78,96,55,5,46,35,89,85,54,76,64,71,36,98,94,100,7,88,92,80,43,24,89,50,61,59,20,94,57,99,62,82,46,28,57,66,62,56,15,12,63,19,35,12,26,15,59,8,44,46,45,33,20,27,31,85,15,92,63,63,40,35,95,91,1,4,57,55,68,53,28,15,94,74,89,77,7,25,63,77,24,76,44]],
        'result': 95,
    }

]

utils.test(Solution().heightChecker, cases)