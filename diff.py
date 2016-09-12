def strcmp(first, second):
    same_chars = 0
    sign = 1
    mark = False
    checkpoints = []
    prev_char = ''
    for to_chr in second:
        found = False
        for from_chr in first:
            prev_char = from_chr
            if to_chr == from_chr:
                found = True
                mark = True
                same_chars += 1
                break
        if mark and not found:
            mark = False
            same_chars -= 1
    print(same_chars)
    return sign * (1 - float(same_chars) / len(second))
        
if __name__ == '__main__':
    
    tests = (
        (('a', 'a'), 0),
        (('a', 'aa'), 0),
        (('ab', 'ab'), 0),
        (('ab', 'aab'), 33),
        (('ba', 'ab'), 1),
        (('ba', 'bab'), 33),
        (('aa', 'bab'), 67),
        (('bab', 'a'), -67),
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
