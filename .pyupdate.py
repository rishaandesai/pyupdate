import sys, os, requests, time, ssl, certifi
from urllib.request import Request, urlretrieve
from os import system, name


def install(pkg, log=True):
    def loader():
        print('Downloading package...')
        bar = [" [=     ]", " [ =    ]", " [  =   ]", " [   =  ]", " [    = ]", " [     =]", " [    = ]", " [   =  ]", " [  =   ]", " [ =    ]", " [=     ]"]
        i = 0

        def clear(): #This function clears the screen
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
        while i<33:
            print(bar[i % len(bar)], end="\r")
            time.sleep(.2)
            i += 1
        clear()

    loader()
    if log:
        os.system('sudo installer -pkg ' + pkg + ' -target /usr/local/bin/python3 -dumplog')
    else:
        os.system('sudo installer -pkg ' + pkg + ' -target /usr/local/bin/python3')

def download():
    ssl._create_default_https_context = ssl._create_unverified_context
    urlretrieve("https://pyupdate-server.rishaandesai.repl.co/static/python3.pkg", "python3.pkg")

def update(log=True):
    download()
    install('python3.pkg', log=log)
    os.remove('python3.pkg')
    sys.stdout.write('Python 3 has been successfully updated!\nRestart the terminal to have the update take effect.')
    sys.exit()

update()