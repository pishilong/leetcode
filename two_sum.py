from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        slots = {}
        for idx, num in enumerate(nums):
            need = target - num
            if need in slots:
                return [slots[need], idx]

            slots[num] = idx

if __name__ == '__main__':
    nums = [-3, 4, 3, 90]
    target = 0
    solution = Solution()
    print(solution.twoSum(nums, target))
