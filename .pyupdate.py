import sys, os, subprocess, requests, time
from turtle import down
from bs4 import BeautifulSoup as bs4
from os import system, name

def install(pkg):
    def loader():
        print('Downloading package...')
        bar = [
            " [=     ]",
            " [ =    ]",
            " [  =   ]",
            " [   =  ]",
            " [    = ]",
            " [     =]",
            " [    = ]",
            " [   =  ]",
            " [  =   ]",
            " [ =    ]",
        ]
        i = 0

        def clear(): #This function clears the screen
            if name == 'nt':
                _ = system('cls')
            else:
                _ = system('clear')
        while i<30:
            print(bar[i % len(bar)], end="\r")
            time.sleep(.2)
            i += 1
        clear()

    loader()
    os.system('sudo installer -pkg ' + pkg + ' -target /usr/local/bin/python3')

def download():
    r = requests.get('https://www.python.org/downloads/')
    soup = bs4(r.text, 'html.parser')
    soup = soup.find('div', {'class': "download-for-current-os"}).find('a').get('href')
    r = requests.get(soup)
    with open('python3.pkg', 'wb') as f:
        f.write(r.content)

def update():
    download()
    install('python3.pkg')
    os.remove('python3.pkg')
    sys.stdout.write('Python 3 has been successfully updated!\nRestart the terminal to have the update take effect.')

    sys.exit()

update()