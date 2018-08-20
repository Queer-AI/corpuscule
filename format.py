#!/usr/bin/env python3

#in some cases, names of characters exist on the same line as the corresponding dialogue. Here we preprocess such files such that names appear on the line before the dialogue begins.

import sys
import re

if len(sys.argv) < 2:
    raise "Please provide the path to a play."

play = ""

def readline(file):
    global play
    line = file.readline()
    if line == "":
        return False
    elif line == "\n":
        return True
    else:
        split = line.split(':')
        name = re.match(r'[A-Z ]+', split[0])
        if len(split) > 1 and name:
            play += name.group(0) + '\n'
            play += split[1].strip() + '\n'
        return True
 

with open(sys.argv[1]) as f:
    count = 0
    while(readline(f)):
        count += 1

print(play)
