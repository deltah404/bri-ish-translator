import wn
import json
from random import choice

print('Anything within this section is simply setup. Please wait.\n----------')
try:
    wn.data.find('goodmami/wn')
except:
    wn.download('ewn:2020')
print('----------')

with open('./config.json') as ifile:
    idict = json.load(ifile)
    name = idict['name']
    version = idict['version']
    noun_exceptions = idict['nexceptions']
    endings = idict['phraseendings']
    word_replacements = idict['wordreplacements']
    
toTranslate = input(f'{name} v{version}\n>> ').lower()

# individual rules -----
# word replacements
wordReplaced = ''
for word in toTranslate.split(' '):
    if word in word_replacements.keys():
        newword = word_replacements[word]
    else:
        newword = word
    wordReplaced += newword+' '

# universal rules -----
# insert fuckin' before each noun
nounCussing = ''
for word in wordReplaced.split(' '):
    if word in ['fucking','fuckin\'']:
        word = ''
        
    try:
        tmp = wn.synsets(word)[0].pos
    except:
        tmp = '.'
        
    newword = f'fuckin\' {word}' if tmp == 'n' and word not in noun_exceptions else word
    nounCussing += f'{newword} '

# -replace t with '
tSilencing = ''
for c in nounCussing:
    tSilencing += '\'' if c == 't' else c
    
res = tSilencing[:-2]+choice(endings)

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
print(filteredText)
print('^\nPress enter to exit.')
input()