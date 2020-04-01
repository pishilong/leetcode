import utils


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0

        if s == s[::-1]:
            return 1
        else:
            return 2


cases = [
    {
        'input': "ababa",
        'result': 1,
    },
    {
        'input': "abb",
        'result': 2,
    },
    {
        'input': "baabb",
        'result': 2,
    },
    {
        'input': "",
        'result': 0,
    }
]

utils.test(Solution().removePalindromeSub, cases)