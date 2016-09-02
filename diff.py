

def strcmp(first, second):
    same_chars = 0
    sign = 1
    mark = False
    for to_chr in first:
        found = False
        for from_chr in second:
            if to_chr == from_chr:
                found = True
                mark = True
                same_chars += 1
                break
        if mark and not found:
            mark = False
            same_chars -=1
    return sign * (1 - same_chars / len(second))
        
