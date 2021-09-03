import wn
import json
import sys
import subprocess
import pkg_resources
from random import choice

with open('././config.json') as ifile:
    idict = json.load(ifile)
    name = idict['name']
    version = idict['version']
    noun_exceptions = idict['nexceptions']
    endings = idict['phraseendings']
    word_replacements = idict['wordreplacements']

required = {'wn'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    if missing == required:
        print(f'Thanks for supporting {name}. As this is your first time, please wait while everything gets set up.')
    else:
        print(f'You don\'t have all the required files for DBT. Please wait while the missing items are installed.')
    python = sys.executable
    for m in missing:
        subprocess.check_call(['pip', 'install', m], stdout=subprocess.PIPE)
    
print('Anything within this section is simply setup. Please wait.\n-------------------------')
try:
    wn.data.find('goodmami/wn')
except:
    wn.download('ewn:2020')
print('-------------------------')
    
toTranslate = input(f'{name} v{version}\n>> ').lower()

nounCussing = ''
for word in toTranslate.split(' '):
    if word == 'bloody':
        word = ''
        
    try:
        tmp = wn.synsets(word)[0].pos
    except:
        tmp = '.'
        
    newword = choice([f'bloody {word}',f'fuckin\' {word}']) if tmp == 'n' and word not in noun_exceptions else word
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
    if c in ['\'',' '] and c == last:
        char = ''
    else:
        char = c
    last = char
    filteredText += char

print(toTranslate)
print(filteredText.lower())
print('\nPress enter to exit.')
input()