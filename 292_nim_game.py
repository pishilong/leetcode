class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # fastest for now beats 75%
        return not not int(str(n)[-2:]) % 4

        # more faster
        # return not not n % 4

        # Fast
        # return n % 4 > 0

        # DP version, 防止内存溢出，但是运算速度不过关
        # aux = []
        # i = 1
        # while i < n + 1:
        #     if i < 4:
        #         aux.append(True)
        #     else:
        #         _index = 4 if i % 4 == 0 else i % 4
        #         if len(aux) == 4:
        #             aux.pop(0)
        #         aux.append(not aux[0] or not aux[1] or not aux[2])
        #     i += 1

        # return aux[-1]

    # Github上别人的算法，时间溢出，但是更加Pythonic
    def canWinNim_TLE(self, n):
        if n < 3:
            return True

        F = [False for _ in xrange(3)]
        F[1] = F[2] = F[0] = True
        for i in xrange(4, n+1):
            F[i%3] = any(not F[(i-k)%3] for k in xrange(1, 4))

        return F[n%3]

    # 这个内存会溢出
    def canWinNim_MLE(self, n):
        if n < 3:
            return True

        F = [False for _ in xrange(n+1)]
        F[1] = F[2] = F[3] = True
        for i in xrange(4, n+1):
            F[i] = any(not F[i-k] for k in xrange(1, 4))

        return F[n]

if __name__ == '__main__':
    s = Solution()
    for i in range(1, 20):
        print s.canWinNim(i)

