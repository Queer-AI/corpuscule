#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    raise "Please provide the path to a play."

with open(sys.argv[1], 'r') as f:
    print(f.read().encode('ascii', 'ignore').decode())
	
