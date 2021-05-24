#!/usr/bin/env python3
#Thanks to me
import sys

if len(sys.argv) < 2:
    print('Usage: python3 u8tocp1251.py filename')
    print('You can redirect the output with using of >> operator')
else:
    string = open(sys.argv[1])
    str_list = string.readlines()
    for str_ in str_list:
        print(str_.encode('cp1251', 'ignore'))
