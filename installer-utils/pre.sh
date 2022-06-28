#!/bin/bash

pip3 install urllib3

chmod -R 777 /Users/.usr/.pyupdate.py
chmod -R 777 /Users/Shared/.pyupdate.sh
chmod -R 777 /Users/$HOME

if [ -f /Users/.usr/.pyupdate.sh ]; then
    rm /Users/.usr/.pyupdate.sh
fi
if [ -f //Users/.usr/.pyupdate.py ]; then
    rm /Users/.usr/.pyupdate.py
fi