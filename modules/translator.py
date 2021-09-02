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
    print(f'Thanks for supporting {name}. As this is your first time, please wait while everything gets set up.')
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

# insert fuckin' before each noun
nounCussing = ''
for word in toTranslate.split(' '):
    if word in ['fucking','fuckin\'']:
        word = ''
        
    try:
        tmp = wn.synsets(word)[0].pos
    except:
        tmp = '.'
        
    newword = f'fuckin\' {word}' if tmp == 'n' and word not in noun_exceptions else word
    nounCussing += f'{newword} '

# individual rules -----
# word replacements
wordReplaced = ''
for word in nounCussing.split(' '):
    if word in word_replacements.keys():
        newword = word_replacements[word]
    else:
        newword = word
    wordReplaced += newword+' '

# universal rules -----
# -replace t with ' except at beginning of word
transformBlock = ''
tSilencing = ''
for w in wordReplaced.split(' '):
    if w.startswith('t'):
        transformBlock += w.capitalize()+' '
    else:
        transformBlock += w+' '
        
for c in transformBlock:
    tSilencing += '\'' if c == 't' else c
    
res = tSilencing[:-3]+choice(endings)

# grammatical resolving -----
# remove duplicate punctuation
last = ''
filteredText = ''
for c in res:
    if c in ['\'',' '] and c == last:
        char = ''
    else:
        char = c
    last = char
    filteredText += char

print('\n')
print(filteredText.lower())
print('^\nPress enter to exit.')
input()