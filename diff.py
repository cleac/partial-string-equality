

def strcmp(first, second):
    sign = 1
    comp_to_str = second
    comp_from_str = first
    if len(second) < len(first):
        sign = -1
        comp_to_str, comp_from_str = comp_from_str, comp_to_str
    total_length = len(comp_to_str)
    
    same_chars = 0
    mark = 0
    add_mark = False
    for i in range(total_length):
        to_chr = comp_to_str[i]
        for k in range(len(comp_from_str)):
            print(same_chars)
            from_chr = comp_from_str[k]
            print('{} == {}  ==>  {}'.format(from_chr, to_chr, to_chr == from_chr))
            if mark:
                print('mark ==> {}'.format(mark))
            if to_chr == from_chr:
                if mark:
                    same_chars += 1
                else:
                    mark = i
                    same_chars += 1
            else:
                if mark: 
                    if not add_mark:
                        add_mark = True
                    else:
                        add_mark = False
                        mark = 0
                        same_chars -= 1
                        break
                    continue
                else:
                    mark = 0


    return sign * same_chars / total_length
        
