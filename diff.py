def strcmp(first, second):
    same_chars = 0
    sign = 1
    processing_index = -1
    current_count_progress = 0
    if len(first) > len(second):
        sign = -1
        first, second = second, first
    first_len = len(first)
    for to_chr in second:
        if processing_index < 0: 
            for j, from_chr in zip(range(first_len), first):
                if to_chr == from_chr:
                    current_count_progress = 1
                    processing_index = j
                    break
        else:
            processing_index += 1
            if processing_index >= first_len:
                break
            if to_chr == first[processing_index]:
                current_count_progress += 1
            else:
                if current_count_progress > 1:
                    same_chars += current_count_progress
                processing_index = -1
                current_count_progress = 0
    if current_count_progress:
        same_chars += current_count_progress
    return sign * (1 - float(same_chars) / len(second))
        
if __name__ == '__main__':
    
    tests = (
        (('a', 'a'), 0),
        (('a', 'aa'), 50),
        (('ab', 'ab'), 0),
        (('ab', 'aaab'), 50),
        (('ba', 'gjhghj'), 100),
        (('ba', 'babc'), 50),
        (('aa', 'baab'), 50),
        (('babc', 'ab'), -75),
    )

    print(len(tests))
    for strs, assertion in tests:
        try:
            assert round(100*strcmp(*strs)) == assertion
        except AssertionError:
            print('Error for values {}: expected {}, got {}'.format(
                strs,
                assertion,
                round(100*strcmp(*strs)))
            )
