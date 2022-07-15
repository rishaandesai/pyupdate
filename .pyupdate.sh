#!/bin/bash

function pyupdate() {
    if [ -z "$1" ]; then
        sudo python3 /Users/.usr/.pyupdate.py
    else
        echo "Unknown option: $1"
        echo "Try 'pyupdate --help' for more information."
    fi
}