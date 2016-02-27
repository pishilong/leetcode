class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for index in xrange(0, len(nums), 2):
            if len(nums) == index + 1:
                return nums[index]
            if nums[index] != nums[index + 1]:
                return nums[index]

    def singleNumber_XOR(self, nums):
        """
        Cannot use hash table since extra memory
        Use XOR instead

        Algorithm:
        Concept of RAID
        XOR
        bits:
        consider a list of 4-bit number:
        0000
        0001
        0010
        ...
        1111

        appear twice:
        num^num is 0
        storage ^= (num^num) is storage ^= 0, which is storage itself

        if only appear once:
        storage ^= num is the num, since the storage is 0 initially
        :param A: a list of integer
        :return: int
        """
        storage = 0
        for element in nums:
            storage ^= element
        return element


if __name__ == '__main__':
    list1 = list(xrange(1, 100000))
    list2 = list(xrange(1, 99999))
    list1.extend(list2)
    print Solution().singleNumber(list1)
