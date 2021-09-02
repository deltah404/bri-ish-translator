import json
import pkg_resources
import sys
import subprocess
import keyboard
from subprocess import Popen

with open('./config.json') as ifile:
    idict = json.load(ifile)
    name = idict['name']
    version = idict['version']
    mhk = idict['modulehotkeys']

required = {'keyboard'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print(f'Thanks for supporting {name}. As this is your first time, please wait while everything gets set up.')
    python = sys.executable
    for m in missing:
        subprocess.check_call(['pip', 'install', m], stdout=subprocess.PIPE)
    
print(f'{name} v{version}\n\nSelect a module:')

for m in mhk:
    print(f'Press {mhk[m]} for {m}')

while True:
    try:
        if keyboard.is_pressed('1'):
            subprocess.call('start /wait py -3 ./modules/translator.py', shell=True)
            sys.exit()
    except:
        break