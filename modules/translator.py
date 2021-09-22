import os
import json
import sys
import subprocess
import pkg_resources
from datetime import datetime
from random import choice

def translate(t, rawTranslator=False, saveHistory=False):
    with open('././resources/config.json') as ifile:
        idict = json.load(ifile)
        name = idict['name']
        version = idict['version']
        noun_exceptions = idict['nexceptions']
        endings = idict['phraseendings']
        word_replacements = idict['wordreplacements']

    with open('././resources/menu-title.txt', 'r') as tfile:
        title = tfile.read()
    if rawTranslator:
        print(title)

    required = {'wn', 'nltk'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        if missing == required and rawTranslator:
            print(
                f'Thanks for supporting {name} v{version}. As this is your first time, please wait while everything gets set up.')
        elif missing != required and rawTranslator:
            print(f'You don\'t have all the required files for DBT. Please wait while the missing items are installed.')
        python = sys.executable
        for m in missing:
            subprocess.check_call(['pip', 'install', m],
                                  stdout=subprocess.PIPE)

    import wn
    import nltk

    try:
        nltk.data.find('wordnet', quiet=True)
    except:
        nltk.download('wordnet', quiet=True)

    nounCussing = ''
    for word in t.split(' '):
        if word in ['bloody', 'fuck', 'fucking', 'fuckin\'']:
            word = ''
        try:
            tmp = wn.synsets(word)[0].pos
        except:
            tmp = '.'
        newword = choice([f'bloody {word}', f'fuckin\' {word}']
                         ) if tmp == 'n' and word not in noun_exceptions else word
        nounCussing += f'{newword} '

    wordReplaced = ''
    for word in nounCussing.split(' '):
        if word in word_replacements.keys():
            newword = word_replacements[word]
        else:
            newword = word
        wordReplaced += newword+' '

    transformBlock = ''
    tSilencing = ''
    for w in wordReplaced.split(' '):
        if w.startswith('t'):
            transformBlock += w.capitalize()+' '
        elif w.startswith('h'):
            transformBlock += '\''+w[1:]+' '
        else:
            transformBlock += w+' '

    for c in transformBlock:
        tSilencing += '\'' if c == 't' else c

    res = tSilencing[:-3]+choice(endings)

    last = ''
    filteredText = ''
    for c in res:
        if c in ['\'', ' '] and c == last:
            char = ''
        else:
            char = c
        last = char
        filteredText += char

    if saveHistory:
        now = datetime.now()
        with open(f'././history/translator/{now.strftime(r"%b-%d-%Y-%H-%M-%S")}', 'w') as hf:
            hf.write(filteredText.lower())

    return filteredText


if __name__ == "__main__":
    str_to_translate = input('>> ').lower()
    print('...')
    print(translate(str_to_translate, True, True))
    print('\nPress enter to exit.')
    input()