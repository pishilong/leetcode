# -*- coding: utf-8 -*-
"""
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly
twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
class Solution(object):
    def singleNumberMySolution(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        #print nums
        cur = 0
        result = []
        index = 1
        for i, num in enumerate(nums):
            cur ^= num
            #print "index: %d, num: %d, cur: %d" % (index, num, cur)
            if cur != 0:
                if index % 2 == 0:
                    result.append(nums[i - 1])
                    index = 1
                    cur = num
                if i == len(nums) - 1:
                    result.append(nums[i])
            index += 1
        return result

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        假设两个数分别为a, b
        相同的数字XOR操作后结果为0
        所以bits = a ^ b

        然后bits & -bits可以得到a、b在二进制中高位到低位第一个不同的位数

        以此作为划分nums的依据，可以把nums切分为两个分组，a、b分属于不同的分组，
        分组中其他数字都是成对的，所以把问题转化为从两个分组中找出一个single number.

        a = 3 = 011
        b = 5 = 101
        bits = a ^ b = 110
        -bits = 010(补码)

        diff = bits ^ -bits = 010
        3，5在二进制的第二位不同,所以a & diff != b & diff
        """
        bits = 0
        for num in nums:
            bits ^= num

        diff = bits & -bits

        a = b = 0
        for num in nums:
            if num & diff:
                a ^= num
            else:
                b ^= num

        return a, b

if __name__ == '__main__':
    result = Solution().singleNumber([1, 2, 1, 3, 2, 5, 4, 4])
    print result
