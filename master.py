import pkg_resources
import sys
import subprocess
import json
from time import sleep as s

with open('./resources/config.json', 'r') as ifile:
    idict = json.load(ifile)
    name = idict['name']
    version = idict['version']
    mhk = idict['modulehotkeys']
    alsolist = idict['alsolist']

with open('./resources/menu-title.txt', 'r') as tfile:
    print(f'====================================\n{tfile.read()}v{version}\n\n====================================')
    
required = {'keyboard','pandas'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

print()

if missing:
    if missing == required:
        print(f'Thanks for supporting {name}. As this is your first time, please wait while everything gets set up.')
    else:
        print(f'You don\'t have all the required files for {name}. Please wait while the missing items are installed.')
    python = sys.executable
    for m in missing:
        subprocess.check_call(['pip', 'install', m], stdout=subprocess.PIPE)

# new library imports
import keyboard
from pandas.io import clipboard
    
print(f'{name}\n\n~~MENU~~\nModule select:')

for m in mhk:
    print(f'Press {mhk[m]} for {m}')
print(alsolist)

while True:
    # cooldown to stop spam glitches
    s(0.1)
    try:
        if keyboard.is_pressed('1'):
            subprocess.call('start /wait py -3 ./modules/translator.py', shell=True)
        elif keyboard.is_pressed('g'):
            clipboard.copy('https://github.com/deltah404/bri-ish-translator')
            print('Copied!')
        elif keyboard.is_pressed('h'):
            print('\n~~MENU~~\nModule select:')
            for m in mhk:
                print(f'Press {mhk[m]} for {m}')
            print(alsolist)
        elif keyboard.is_pressed('q'):
            print('Closing...')
            sys.exit()
    except:
        break