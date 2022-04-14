#! /usr/bin/bash

White="\033[1;37m"
Reset="\033[0m"

function prs() {
    echo -e "$White ==> $1 $Reset"
}

function checkDepends() {
    is_uvicorn=$(command -v uvicorn &> /dev/null)
    if ! $is_uvicorn ; then
        echo "Uvicorn is not installed 😥"
        exit
    fi
}

function main() {
    echo -e "$White Nexa-APIs 🌊 - Dev Mode (v0.2.1) $Reset\n\n "
    prs "Checking Dependencies 🔎..."
    checkDepends
    prs "All done ✅, Starting..."
    uvicorn api.main:app --reload
}

main