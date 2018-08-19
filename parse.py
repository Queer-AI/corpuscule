#!/usr/bin/env python3

import re
import sys

corpus = ""
current_speaker = None
prev_speaker = None
prev_line = ""

if len(sys.argv) < 2:
    raise "Please provide the path to a play."

def end_conversation():
    global corpus
    corpus += "===\n"
    #corpus += "{} <-> {}\n".format(prev_speaker, current_speaker)

def get_line(file):
    line = file.readline()
    if line == "":
        return None
    else:
        return line.strip()

def is_speaker(line):
    if re.match('ACT', line):
        return False
    return re.fullmatch(r'[A-Z]+', line)

def is_stage_direction(line):
    return re.match(r'[A-Z]{3,}', line)

def next_line(file):
    global prev_speaker
    global current_speaker
    global prev_line
    global corpus

    line = get_line(file)
    if line == None:
        return None
    # line has now been stripped, so a blank line looks like this:
    if line == "":
        return True
    if is_speaker(line):
        if prev_speaker and prev_speaker != line:
            end_conversation()
            prev_speaker = None
            current_speaker = None
        prev_speaker = current_speaker
        current_speaker = line
        if not is_stage_direction(prev_line):
            corpus += prev_line + "\n"
    prev_line = line
    return True

def parse(file):
    count = 0
    while(next_line(file)):
        count += 1

with open(sys.argv[1]) as f:
    parse(f)
    print(corpus)
