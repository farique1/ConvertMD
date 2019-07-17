"""
Add trailing spaces to Markdown
Prevente the GitHub Markdown format to concatenate lines

Copyright (C) 2019 - Fred Rique (farique)
https://github.com/farique1/ConvertMD

spacesMD.py <source> <destination> -ns #
-ns #    :Number os spaces to add. Default = 2
Overwrite <source> if <destination> is ommited.
"""

import argparse

# Config
fileeLad = ''       # Source file
fileeSve = ''       # Destination file
trailing_spaces = 2
buffercode = []

# Variables
# image = False
# bullet = False
# code = False
# prev_blank = False

# Set command line
parser = argparse.ArgumentParser(description='Convert .md to .txt')
parser.add_argument("input", nargs='?', default=fileeLad, help='Source file')
parser.add_argument("output", nargs='?', default=fileeSve, help='Destination file, overwrite [source] if missing')
parser.add_argument("-ns", default=2, type=int, help="Number os spaces to add. Default = 2")
args = parser.parse_args()

# Apply chosen settings
fileeLad = args.input
fileeSve = args.output
if args.output == '':
    fileeSve = fileeLad
trailing_spaces = ' ' * args.ns

# If there is a file to be oppened after all this
if fileeLad:
    file = open(fileeLad, 'r')
    source = file.readlines()
    file.close()
else:
    parser.error('Source file not found')
    raise SystemExit(0)

for line in source:
    line_alt = line
    line_alt = line_alt.rstrip()
    line_alt = line_alt + trailing_spaces + '\n'
    buffercode.append(line_alt)

save = open(fileeSve, 'w')
for line in buffercode:
    save.write(line)
save.close()
