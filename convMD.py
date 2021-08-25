#!/usr/bin/env python3
"""
Convert Markdown to TXT
A very simple converter from .md to .txt

Copyright (C) 2019 - Fred Rique (farique)
https://github.com/farique1/ConvertMD

convmd.py <source> <destination>
<source>.txt is used if <destination> is ommited.

Remove '# ', '## ', '### ' and add '------' underneath; also blank lines before and after if needed.
Lone '#'s to blank line.
Remove all '*...*' formatting.
'- - ' and '- - - ' to '  - ' and '    - '
Option (commented out) to keep indent after '- '
'>' to '-> '
Backtick to single quote
Fence code between '~' adding blank line before and after if needed.
Strip image tags '![#...'
Remove '[]' from link Names (keep the links between '()')
Do not allow more than one consecutive blank line.
"""

import re
import argparse

# Config
fileeLad = ''       # Source file
fileeSve = ''       # Destination file

# Variables
image = False
bullet = False
code = False
prev_blank = False

# Set command line
parser = argparse.ArgumentParser(description='Convert .md to .txt')
parser.add_argument("input", nargs='?', default=fileeLad, help='Source file')
parser.add_argument("output", nargs='?', default=fileeSve, help='Destination file ([source].txt) if missing')
args = parser.parse_args()

# Apply chosen settings
fileeLad = args.input
fileeSve = args.output
if args.output == '':
    fileeSve = re.sub(r'(.*\.).*', r'\1txt', fileeLad)


# If there is a file to be oppened after all this
if fileeLad:
    file = open(fileeLad, 'r')
    source = file.readlines()
    file.close()
else:
    parser.error('Source file not found')
    raise SystemExit(0)

buffercode = ['** This file was auto converted from a .md\n', '** Read the .md for a cleaner version\n', '\n']
for line in source:
    line_new = line.rstrip() + '\n'
    dashes = False
    add_blank_before = False
    add_blank_after = False

    if line_new == '\n' and image:
        image = False
        continue
    image = False

    if '![#' in line_new[:3]:
        image = True
        continue

    if re.search(r'^\s*```', line_new):
        code = not code
        if code:
            line_new = '~\n'
            if not prev_blank:
                add_blank_before = True
        else:
            line_new = '~\n'
            add_blank_after = True

    if not code:
        hasht = re.search(r'^#{1,3} ', line_new)
        if hasht:
            line_new = line_new[len(hasht.group(0)):]
            dashes = True
            add_blank_after = True
            add_blank_before = True

        while line_new.count('*') > 1:
            star = re.search(r'\*\S.*?\S\*', line_new)
            if star:
                line_new = line_new.replace(star.group(0), star.group(0)[1:-1])
                # print line_new.count('*')
                # print star.group(0), star.group(0)[1:-1]
                # print line_new
            else:
                break

        links = re.search(r'\[.+?\]\(.+?\)', line_new)
        while links:
            links_sub = links.group(0).replace('[', '')
            links_sub = links_sub.replace(']', ' ')
            line_new = line_new.replace(links.group(0), links_sub)
            links = re.search(r'\[.+?\]\(.+?\)', line_new)

        if re.search(r'^\s*#+', line_new):
            line_new = '\n'

        line_new = line_new.replace('`', "'")

        line_new = re.sub(r'^>', r'-> ', line_new)

        bullett = re.search(r'((- )+)\w', line_new)
        # if line_new != '\n' and not bullett and bullet:
        #   line_new = (' '*bullet_len) + line_new
        # elif line_new == '\n':
        #   bullet = False

        if bullett:
            # bullet = True
            bullet_len = len(bullett.group(1))
            line_new = (' ' * (bullet_len - 2)) + line_new[bullet_len - 2:]

    if line_new == '\n':
        if not prev_blank:
            buffercode.append('\n')
            prev_blank = True
    else:
        if add_blank_before and not prev_blank:
            buffercode.append('\n')
            add_blank_before = False
        buffercode.append(line_new)
        prev_blank = False
        if dashes:
            buffercode.append('-' * (len(line_new) - 1) + '\n')
        if add_blank_after:
            buffercode.append('\n')
            add_blank_after = False
            prev_blank = True

    # print line_new.rstrip()
    # if dashes:
    #   print '-'*len(line_new.rstrip())
    # if add_blank:
    #   print

save = open(fileeSve, 'w')
for line in buffercode:
    save.write(line)
save.close()
