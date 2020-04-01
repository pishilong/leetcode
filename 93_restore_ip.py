from typing import List
import utils


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def backtrace(count, ip, s):
            if count == 4:  # 回溯点，已经有三个分隔符，并且刚好结束
                if s == '':
                    ans.append(ip[:-1])
                return
            if len(s) > 0:
                backtrace(count + 1, ip + s[0] + '.', s[1:])
            if len(s) > 1 and s[0] != '0':
                backtrace(count + 1, ip + s[:2] + '.', s[2:])
            if len(s) > 2 and s[0] != '0' and int(s[0:3]) < 256:
                backtrace(count + 1, ip + s[:3] + '.', s[3:])

        backtrace(0, '', s)
        return ans


cases = [
    {
        'input':  ["25525511135"],
        'result': ["255.255.11.135", "255.255.111.35"]
    }
]

utils.test(Solution().restoreIpAddresses, cases)