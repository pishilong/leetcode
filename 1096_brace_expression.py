from typing import List
import utils
import re

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        states = {
            'start': {
                '{': 'buildingSet',
                'w': 'buildingWord',
            },
            'buildingWord': {
                'w': 'buildingWord',
                ',': 'buildingSet',
                '{': 'buildingSet',
            },
            'buildingSet': {
                '}': 'standby',
            },
            'standby': {
                '{': 'buildingSet',
                'w': 'buildingWord',
                ',': 'buildingSet',
            }
        }

        def input_symbol(c):
            if c.isalpha():
                return 'w'
            else:
                return c

        cur_state = 'start'

        stack = []

        for char in expression:
            cur_symbol = input_symbol(char)
            next_state = states[cur_state][cur_symbol]

            if cur_state == 'start':
                pass
            elif cur_state == 'buildingWord':
                if cur_symbol == 'w':
                    cur_word += char
                elif cur_symbol == '{':
                    stack.append(cur_word)
                    stack.

            if next_state == 'buildingWord':
                if cur_state != next_state:
                    cur_word = ''
            elif ne



cases = [
    {
        'input': ["{a,b}{c{d,e}}"],
        'result': ["acd", "ace", "bcd", "bce"],
    },
    {
        'input': ['{{a,z}, a{b,c}, {ab,z}}'],
        'result': ["a","ab","ac","z"],
    }
]

utils.test(Solution().braceExpansionII, cases)