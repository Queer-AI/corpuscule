#!/usr/bin/env bash

OUTPUT_FILE=plays.txt

echo '' > $OUTPUT_FILE

for text in ./scripts/*.txt; do
    ./parse.py $text >> $OUTPUT_FILE
done
