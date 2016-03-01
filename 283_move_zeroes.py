# -*- coding: utf-8 -*-
class Solution(object):
    def moveZeroesDC(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        不具备最优子结构，不能转化为动态规划问题
        采用分治策略
        """
        left = 0
        right = len(nums)
        self.moveZeroesPart(nums, left, right - 1)

    def moveZeroesPart(self, nums, left, right):
        """divid"""
        if left == right:
            return

        if right == left + 1 and nums[left] == 0:
            nums[left], nums[right] = nums[right], nums[left]

        mid = (left + right) / 2

        self.moveZeroesPart(nums, left, mid)
        self.moveZeroesPart(nums, mid + 1, right)
        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        i = left
        j = mid + 1
        while nums[i] != 0 and i <= mid:
            i += 1

        while j <= right and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

    def moveZeroesPivot(self, nums):
        """遍历"""
        left = -1
        for i in xrange(len(nums)):
            if nums[i] != 0:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]

    def moveZeroes(self, nums):
        """in place exchange"""
        i = 0
        for element in nums:
            if element != 0:
                nums[i] = element
                i += 1

        for j in xrange(i, len(nums)):
            nums[j] = 0


if __name__ == '__main__':
    Solution().moveZeroesDC([4,2,4,0,0,3,0,5,1,0])


