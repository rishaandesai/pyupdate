#!/bin/bash

function pyupd() {
    sudo python3 /Users/.usr/.pyupdate.py
}

function --help() {
    echo "usage: pyupd [--version] [--help]"
}

function pyupdate() {
    if [ -z "$1" ]; then
        pyupd
    elif [ "$1" == "--help" ]; then
        --help
    elif [ "$1" == "--version" ]; then
        echo "pyupdate v1.0s"
    else
        echo "Unknown option: $1"
        echo "Try 'pyupdate --help' for more information."
    fi
}