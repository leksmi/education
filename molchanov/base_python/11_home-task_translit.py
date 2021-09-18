# Character base from Russian to translit
char_base = {
'а': 'a',
 'б': 'b',
 'в': 'v',
 'г': 'g',
 'д': 'd',
 'е': 'e',
 'ё': 'yo',
 'ж': 'zh',
 'з': 'z',
 'и': 'i',
 'й': 'y',
 'к': 'k',
 'л': 'l',
 'м': 'm',
 'н': 'n',
 'о': 'o',
 'п': 'p',
 'р': 'r',
 'с': 's',
 'т': 't',
 'у': 'u',
 'ф': 'f',
 'х': 'kh',
 'ц': 'ts',
 'ч': 'ch',
 'ш': 'sh',
 'щ': 'shch',
 'ъ': "'",
 'ы': 'y',
 'ь': "'",
 'э': 'e',
 'ю': 'iu',
 'я': 'ia'
}

# Input your word and make it with lower register
your_word = input('Enter word to be translited: ').lower()
# Make empty list
new_word_list = []
# Iterate your word looking for interesting character
for word in your_word:
    # Compare word with dict's keys
    if word in char_base.keys():
        # If word is in the dict it adds to word list
        new_word_list.append(char_base[word])
# Make string with list and print it
print('Your word in translit: ', ''.join(new_word_list).capitalize())
