import sys, os, time, ssl
from urllib.request import urlretrieve
from os import system, name
from sys import argv, exit

def loader():
        print('Downloading package...')
        bar = [" [=     ]", " [ =    ]", " [  =   ]", " [   =  ]", " [    = ]", " [     =]", " [    = ]", " [   =  ]", " [  =   ]", " [ =    ]", " [=     ]"]
        i = 0

        def clear():
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
        while i<33:
            print(bar[i % len(bar)], end="\r")
            time.sleep(.2)
            i += 1
        clear()

def install(pkg, log=True):
    if log:
        os.system('sudo installer -pkg ' + pkg + ' -target /usr/local/bin/python3 -dumplog')
    else:
        os.system('sudo installer -pkg ' + pkg + ' -target /usr/local/bin/python3')
    os.remove('python3.pkg')

def download():
    ssl._create_default_https_context = ssl._create_unverified_context
    urlretrieve("https://pyupdate-server.rishaandesai.repl.co/static/python3.pkg", "python3.pkg")

def update():
    loader()
    download()
    install('python3.pkg')
    sys.stdout.write('Python 3 has been successfully updated.\nRestarting terminal.')
    time.sleep(1)
    os.system('reset')
    sys.exit()

try:
    if argv[1] == '--help':
        print('usage: pyupd [--update] [--version] [--help]')
        exit()
    elif argv[1] == '--version':
        print('pyupdate v1.0.1s[patch]')
        exit()
    elif argv[1] == '--update':
        update()
    elif argv[1] == '':
        update()
    else:
        print('usage: pyupd [--update] [--version] [--help]')
        exit()
except:
    print('usage: pyupd [--update] [--version] [--help]')
