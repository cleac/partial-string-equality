def strcmp(first, second):
    same_chars = 0
    sign = 1
    mark = False
    checkpoints = []
    prev_char = ''
    if len(first) > len(second):
        sign = -1
        first, second = second, first
    for to_chr in second:
        found = False
        if prev_char == to_chr:
            continue
        prev_char = to_chr
        # Problem in this part.
        # The position of current element should be saved and checked
        for from_chr in first:
            if to_chr == from_chr:
                found = True
                mark = True
                same_chars += 1
                break
        if mark and not found:
            mark = False
            same_chars -= 1
    return sign * (1 - float(same_chars) / len(second))
        
if __name__ == '__main__':
    
    tests = (
        (('a', 'a'), 0),
        (('a', 'aa'), 50),
        (('ab', 'ab'), 0),
        (('ab', 'aaab'), 50),
        (('ba', 'abcd'), 100),
        (('ba', 'babc'), 50),
        (('aa', 'baab'), 50),
        (('babc', 'ab'), -50),
    )

    for strs, assertion in tests:
        try:
            assert round(100*strcmp(*strs)) == assertion
        except AssertionError:
            print('Error for values {}: expected {}, got {}'.format(
                strs,
                assertion,
                round(100*strcmp(*strs)))
            )
