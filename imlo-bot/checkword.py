
from uzwords import  words
from difflib import get_close_matches

def check_word(word,words=words):
    word=word.lower()
    matches=set(get_close_matches(word,words))
    available=False

    if word in matches:
        available=True
        matches=word
    elif "ҳ" in word:
        word=word.replace('ҳ', 'x')
        matches.update(get_close_matches(word,words))
    elif 'x' in word:
        word = word.replace('x','ҳ')
        matches.update(get_close_matches(word, words))

    return {'available': available, 'matches' : matches}

if __name__=='__name__':
    print(check_word('орма'))
    print(check_word('тарих'))
    print(check_word('китоб'))
    print(check_word('салик'))
    print(check_word('чумоле'))