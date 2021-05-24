# Russian Words Dictionary

## *RU*

### Откуда это все взято?

Все слова были перенесены с сайта wordsonline.ru путем брут-форса его словаря (используя маски)
Можно было сделать все в сто раз легче, но я решил по приколу написать именно так, чтобы протестировать некоторые функции requests.

Все нужные скрипты могут быть найдены в папке scripts.

### Доступные файлы

1) words.txt - содержит всевозможные русские слова без падежей. (более 150000 слов)

2) words_dictionary.json - словарь, сделанный из words.txt

3) words_names.txt - содержит всевозможные русские имена.

4) words_names.json - words_names.txt -> .json

5) words_surnames.txt - содержит всевозможные русские фамилии.

6) words_surnames.json - words_surnames.txt -> .json
Кстати, насчет этого файла есть странность - он весит меньше чем в кодировкe cp-1251.

7) Слова в падежах (words_cases) были взяты отсюда, были улучшены и переведены в .json. https://github.com/danakt/russian-words

### Нету слова в словаре?

Просто киньте мне pull request, и недостающее слово будет добавлено.

### Сбилась сортировка?

Just use this command (in /bin)
`sort -u old-file.txt -o new-file.txt`

### Авторские права?

Нахуй авторские права.
Все что здесь есть может использоваться вами как угодно.

> *Но если подьедут федералы, пеняйте на себя, мы не пересекались, лол.*

## *EN*

### Where did you get it from?

All these words were brought from wordsonline.ru
I found a POST method with using of burp suite, and then just brute-forced all words with help of the [mask.](/scripts/brute-forcer.py)

All needed scripts to repeat my steps can be found in scripts folder.

Then I just translated them into **.json**, with using of json_dictionary.py and json_list.py (not yet)

### Available files

All files are divided at sub-directories with their encoding.

1) words.txt contains all words (without cases)

2) words_dictionary.json is the same as words.txt, just translated into words.txt

3) words_names - contains all names on Russian (copy-paste from 10 sites)

4) words_surnames  - contains all surnames on Russian

5) words_cases, as words_surnames were brought and improved from
https://github.com/danakt/russian-words.

### Found a word that missing in this dictionary?

Feel free to send a pull request, and it will be fixed.

### Need to sort files?

Just use `sort -u old-file.txt -o new-file.txt`

### Is there any copyright issues with this?

Fuck copyright issues! You can use it anywhere you want.
I don't honestly care.

