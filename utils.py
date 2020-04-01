def test(solution, cases):
    for case in cases:
        args = case['input']
        if isinstance(args, list):
            result = solution(*args)
        else:
            result = solution(args)
        if result == case['result']:
            print('Passed')
        else:
            msg = 'Failed! input: {input}, result: {result}, expected: {expected}'.format(
                input=case['input'],
                result=result,
                expected=case['result']
            )
            print(msg)