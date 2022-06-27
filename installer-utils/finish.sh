#!/bin/bash

if [ -f /Users/.bashrc ]; then
    #write 'source /Users/'$USER'/pyupdate.sh' to .bashrc
    #echo export source $HOME/pyupdate.sh >> $HOME/.bashrc
    #echo export source $HOME/pyupdate.sh >> $HOME/.bash_profile
    echo alias pyupdate='"python3 /Users/.usr/.pyupdate.py"' >> $HOME/.bashrc
else
    #echo export source $HOME/pyupdate.sh >> $HOME/.zshrc
    echo alias pyupdate='"python3 /Users/.usr/.pyupdate.py"' >> $HOME/.zshrc
fi

osascript -e 'tell application "Terminal" to quit'
