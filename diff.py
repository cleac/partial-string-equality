# Copyright (C) 2016  Alexander Nesterenko
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

import sys


def strcmp(first, second):
    """A string comparsion function

    Takes two functions and calculates the percent of cunjuction between them
    represented by number.
    """
    same_chars = 0
    sign = 1
    processing_index = -1
    current_count_progress = 0
    # Swap strings and change sign if first is bigger than secodn
    if len(first) > len(second):
        sign = -1
        first, second = second, first
    first_len = len(first)
    for to_chr in second:
        # If we've got no processing character, find it
        if processing_index < 0: 
            for j, from_chr in zip(range(first_len), first):
                if to_chr == from_chr:
                    current_count_progress = 1
                    processing_index = j
                    break
        else:
            # Otherwise increase it by one
            processing_index += 1
            # Check if it is still less than first string's length
            if processing_index >= first_len:
                # Otherwise, exit loop
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


def run_tests():    
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

    for strs, assertion in tests:
        try:
            assert round(100*strcmp(*strs)) == assertion
        except AssertionError:
            print('Error for values {}: expected {}, got {}'.format(
                strs,
                assertion,
                round(100*strcmp(*strs)))
            )
        
if __name__ == '__main__':
    print(round(strcmp(sys.argv[1], sys.argv[2]) * 100) / 100)
