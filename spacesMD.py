#!/usr/bin/env python3
"""
Add trailing spaces to Markdown
Prevent the GitHub Markdown format to concatenate lines

Copyright (C) 2023 - Fred Rique (farique)
https://github.com/farique1/ConvertMD

spacesMD.py [source] [destination] -ns #
-ns #       :Number of spaces to add. Default = 2
-ext ''     :Extension to load (without .) default=md (always save as .md)
-all        :Ignore source and reads all files with given extension
-gn         :Capitalize and replace spaces with _
Uses README.md if no [source] given
Save with [source] if [destination>] is omitted.
"""

import glob
import argparse
from pathlib import Path

# Config
fileeLad = ''       # Source file
fileeSve = ''       # Destination file
trailing_spaces = 2
buffercode = []

# Set command line
parser = argparse.ArgumentParser(description='Add trailing spaces to the end of lines to conform with GitHub.')
parser.add_argument("input", nargs='?', default=fileeLad, help='Source file. Uses README.md if missing.')
parser.add_argument("output", nargs='?', default=fileeSve, help='Destination file. Overwrite [source] if missing.')
parser.add_argument("-ns", default=2, type=int, help="Number of spaces to add. Default = 2")
parser.add_argument("-ext", default='md', type=str, help="Alt extension to load (will save as .md)")
parser.add_argument("-all", default=False, action='store_true', help="Do all .md on the current folder")
parser.add_argument("-gn", default=False, action='store_true', help="GitHub Name. Capitalize and _ as spaces on fine names")
args = parser.parse_args()

# Apply chosen settings
fileeLad = args.input
fileeSve = args.output

if fileeLad == '':
    fileeLad = 'README.md'
    fileeSve = fileeLad

if fileeSve == '':
    fileeSve = fileeLad

trailing_spaces = ' ' * args.ns
load_ext = args.ext
do_all = args.all
github_name = args.gn

fileeSve = [(fileeLad, fileeSve)]

if do_all:
    fileeSve = []
    for file in glob.glob(f'*.{load_ext}'):
        filename = Path(file)
        filename = filename.with_suffix('')
        if github_name:
            filename = str(filename).upper()
            filename = filename.replace(' ', '_')
            filename = Path(filename)
        filename = filename.with_suffix('.md')
        fileeSve.append((file, str(filename)))

for save in fileeSve:
    with open(save[0], 'r') as f:
        source = f.readlines()

    buffercode = []
    for line in source:
        line_alt = line
        line_alt = line_alt.rstrip()
        line_alt = line_alt + trailing_spaces + '\r'
        buffercode.append(line_alt)

    with open(save[1], 'w') as f:
        for line in buffercode:
            f.write(line)

    print(save[1])
