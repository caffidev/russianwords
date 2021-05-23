#!/ust/bin/env
#Thanks to Innovative Inventor for this piece of code

import sys
import json

if len(sys.argv) < 2:
    print('Usage: python3 json_dictionary.py filename(*.txt format)')
else:
    words = open(sys.argv[1])
    word_list = words.readlines()
    json_words = {}
    for count in range(len(word_list)):
        json_words[word_list[count].rstrip()] = '1'
    print(json.dumps(json_words, indent = 4))
