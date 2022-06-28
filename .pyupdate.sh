#!/bin/bash

function pyupd() {
    sudo python3 /Users/.usr/.pyupdate.py
}

function pyupdate() { #this is for future custom contexts
    pyupd $1
}