from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_size = len(nums)
        def move_next():
            prev = None

            for i in range(nums_size):
                cur = nums[i]
                if prev is not None:
                    cur = prev

                if i + 1 < nums_size:
                    prev = nums[i + 1]
                    nums[i + 1] = cur
                else:
                    nums[0] = cur

        for i in range(k):
            move_next()

        print(nums)
if __name__ == '__main__':
    solution = Solution()
    ex = [1,2,3,4,5,6,7]
    # ex = [-1,-100,3,99]
    k = 3
    # k = 2
    solution.rotate(ex, k)