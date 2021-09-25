import json
import sys
import subprocess
import pkg_resources
import string
from random import randint, choice
from datetime import datetime
from random import choice



def translate_german(text: str, raw_translator=False, save_history=False):
    '''
    Translates an English string into a lowercase stereotypical interpretation of the German langugae.
        `str` `text` : The English text string that DBT should translate.
        `bool` `rawTransator` : Whether DBT should print basic information found in the raw translator such as the DBT title.
        `bool` `saveHistory` : Whether DBT should save translation history into the history/translator directory inside DBT.
    '''

    text = text.lower()
    with open('././resources/config.json') as ifile:
        idict = json.load(ifile)
        name = idict['name']
        version = idict['version']
        
    required = {'wn', 'nltk'}
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        if missing == required and raw_translator:
            print(
                f'Thanks for supporting {name} v{version}. As this is your first time, please wait while everything gets set up.')
        elif missing != required and raw_translator:
            print(f'You don\'t have all the required files for DBT. Please wait while the missing items are installed.')
        for m in missing:
            subprocess.check_call(['pip', 'install', m],
                                  stdout=subprocess.PIPE)

    import wn
    import nltk

    try:
        nltk.data.find('wordnet', quiet=True)
    except:
        nltk.download('wordnet', quiet=True)
    
    combined = ''

    suffixes = ['eider', 'ein', 'en']

    alphabet = string.ascii_lowercase
    filteredalphabet = []
    for char in alphabet:
        if char not in ['x', 'z']:
            filteredalphabet.append(char)

    for word in text.split(' '):
        # remove unsuitable characters from word
        result = ''
        for char in word:
            if char.isalpha():
                result += char
        word = result

        # get all unique letters in word and add to array of common german sounds
        letters = ['sch', 'ch', 'en']
        for char in word:
            if char not in letters:
                letters.append(char)
                
        # scramble letters in word until a random length and append suffix
        length = randint(1,2)*len(word)
        result = word
        last = ''
        for _ in range(length):
            if randint(1,50) != 1:
                while True:
                    new = choice(letters)
                    if new != last:
                        break
                result += new
                last = new
            else:
                while True:
                    new = choice(filteredalphabet)
                    if new != last:
                        break
                result += new
                last = new
        result+=choice(suffixes)
        combined+=result+' '
        
    if save_history:
        now = datetime.now()
        with open(f'././history/german/{now.strftime(r"%b-%d-%Y-%H-%M-%S")}.txt', 'w+') as hf:
            hf.write(combined.lower())
    
    return combined

if __name__ == "__main__": # checks if the original file is being run : runs normally as the default translator
    print('THE GERMAN TRANSLATOR IS STILL IN BETA. YOU WILL COME ACROSS UNPRONOUNCEABLE WORDS. I AM ACTIVELY TRYING TO FIX THIS. PLEASE BE PATIENT.')
    with open('././resources/menu-title.txt', 'r') as tfile:
        title = tfile.read()
        print(title)
    str_to_translate = input('>> ').lower()
    print('...')
    print(translate_german(str_to_translate, True, True))
    print('\nPress enter to exit.')
    input()