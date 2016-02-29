class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int

        idea : 数根的考察
        num = a_0 * 10^0 + a_1 * 10^1 ...
        digit_root = num % 9 == sum{i=0 to n}{a_i} % 9
        """
        return 9 if num % 9 == 0 and num != 0 else num % 9
