#!/ust/bin/env
#Thanks to Innovative Inventor for this piece of code
#IMPORTANT MESSAGE:
#Python3 loves to save .json files in ASCII, so you need to encode it manually.
#Update: fixed it with using ENSURE_ASCII = false
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
    print(json.dumps(json_words, indent = 4, ensure_ascii = False).decode('utf-8'))
#Just append u - for unicode, or .encode('cp1251') for windows-1251