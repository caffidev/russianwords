##POST /json/word-mask.json HTTP/2
##Host: wordsonline.ru
##Cookie: __gads=ID=9a3c5a4137e7af1a-221e53701bc800be:T=1621759037:RT=1621759037:S=ALNI_MbD1U4WV8HLIa9Ybc4CGHrGPu8nrA
##Content-Length: 55
##Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="90"
##Accept: */*
##X-Requested-With: XMLHttpRequest
##Sec-Ch-Ua-Mobile: ?0
##User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36
##Content-Type: application/x-www-form-urlencoded; charset=UTF-8
##Origin: https://wordsonline.ru
##Sec-Fetch-Site: same-origin
##Sec-Fetch-Mode: cors
##Sec-Fetch-Dest: empty
##Referer: https://wordsonline.ru/search/
##Accept-Encoding: gzip, deflate
##Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
##Connection: close

##word_mask=%D0%B2%D0%B2%2B&word_length=0&word_register=0

##This program finds words from wordsonline.ru site and downloads them

import requests
import json
import sys

url = "https://wordsonline.ru/json/word-mask.json"
payload = {'word_mask': '', 'word_length': 0, 'word_register': 0}
headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
alphabetChr = []
attlen = 1
wordlen = 0

#Opens file for writing
f = open("words.txt", "w")

def get(mask, c_wave):
    '''
    Gets a word from site using a mask
    '''
    payload['word_mask'] = mask + '+'
    print(('  '*(c_wave-1)) + 'Used mask: ', end = '')
    print(payload['word_mask'])
    return requests.post(url, payload, headers = headers)

def wave(mask, c_wave, previous):
    '''
    Starts a so-called wave of a char (3 main waves, and additional)
    '''
    global alphabetChr, attlen, f, wordlen
    print(('  '*(c_wave-1)) + 'Starting wave ' + str(c_wave))
    attempt = 0
    for i in alphabetChr:
        c_mask = mask + i
        attempt += 1
        #There are no words starting with -
        if c_wave == 1 and i == '-':
            continue
        #It could be faster without using this or not, it still needs to be tested
        if c_wave < 3:
            wave(c_mask, c_wave+1, previous + str(attempt) + ':')
            continue
        print(('  '*(c_wave-1))+ '-'*20)
        print(('  '*(c_wave-1)) +'Attempt ' + previous + str(attempt) + ' of ' + str(attlen))
        x = get(c_mask, c_wave)
        obj = json.loads(x.text)
        try:
            words = obj["words"]
            if len(words) > 99:
                #Hard expressions
                print(('  '*(c_wave-1)) + 'Hard expression detected. Starting new wave.')
                attlen += len(alphabetChr)
                wave(c_mask,c_wave+1,previous + str(attempt) + ':')
            else:
                wordlen += len(words)
                for word in words:
                    print(('  '*(c_wave-1)) + word+ ' ', end='')
                    f.write(word + "\n")
                    print('')
        except KeyError:
            print(('  '*(c_wave-1)) + "No words found")
            
    print('Saving...')
    f.close()
    f = open("words.txt", "a")
    return
        
def main():
    global alphabetChr,f, attlen
    #Alphabet counter
    print("Starting extracting words from " + url)
    alphabet = list(range(ord('а'), ord('я') + 1))
    alphabetChr = [chr(n) for n in alphabet]
    alphabetChr += '-'
    print('Используемый алфавит: ')
    print(alphabetChr)
    attlen = pow(len(alphabetChr), 3)
    try:
        #Main script
        #Using fileStream as implementation of wave()
        wave('', 1, '')
        print('Execution completed..')
        print('Length: ' + str(wordlen))
    except:
        print('возникла ошибка: ' + sys.exc_info()[0])
    finally:
        f.close()
            
if __name__ == "__main__":
    main()
