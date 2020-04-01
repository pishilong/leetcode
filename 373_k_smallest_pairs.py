from typing import List
import utils
import heapq
import itertools


# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         pairs = [list(t) for t in itertools.product(nums1, nums2)]
#         return heapq.nsmallest(k, pairs, key=lambda p: p[0] + p[1])

# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         heap = []
#         heap_idx = 0
#         for n1 in nums1:
#             for n2 in nums2:
#                 heapq.heappush(heap, (n1 + n2, heap_idx, [n1, n2]))
#                 heap_idx += 1

#         idx = 0
#         result = []
#         bound = k if k < len(heap) else len(heap)
#         while idx < bound:
#             result.append(heapq.heappop(heap)[-1])
#             idx += 1

#         return result

# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         streams = map(lambda u: ([u + v, u, v] for v in nums2), nums1)
#         stream = heapq.merge(*streams)
#         return [suv[1:] for suv in itertools.islice(stream, k)]

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs



cases = [
    {
        'input': [[1, 7, 11], [2, 4, 6], 3],
        'result': [[1, 2], [1, 4], [1, 6]],
    },
    {
        'input': [[1, 1, 2], [1, 2, 3], 2],
        'result': [[1, 1], [1, 1]],
    },
    {
        'input': [[1, 2], [3], 3],
        'result': [[1, 3], [2, 3]],
    }
]

method = Solution().kSmallestPairs
utils.test(method, cases)
