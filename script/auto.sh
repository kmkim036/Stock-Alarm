#!/bin/sh

python3 /home/kmkim/Projects/git/kmkim036/Stock-Alarm/src/main.py

sleep 5

rm -r /home/kmkim/Projects/git/kmkim036/Stock-Alarm/src/__pycache__

git commit -am "Update: $(date +"%Y-%m-%d")"

git push