#!/usr/bin/env python
# A command-line ID3 tagger for various audio file formats.  Extremely incomplete.

import sys
import os.path
from tag import ID3
from glob import glob
from optparse import OptionParser


def list(options, files):
    """List the files."""
    for audio_file in files:
        if options.raw:
            audio_file.print_tags_raw()
        else:
            audio_file.print_tags(options.verbose)

def clear(options, files):
    """Clear all metadata from a file"""
    for audio_file in files:
        audio_file.clear()
commands = {
    'list' : list
}

def main():

## Option parsing.
    usage = u"taggy.py [options] filename(s)"
    parser = OptionParser(usage=usage)
    parser.add_option("-l", "--list", action="store_const", const="list",
                      help="list tags embedded in a file", dest="command")
    parser.add_option('-r', '--raw', action="store_true", dest='raw', 
                      help='For --list, print raw tags.', default=False)
    parser.add_option('-v', '--verbose', action='store_true', dest='verbose', default=False,
                      help='Verbose output.  In the case of list, print all other tags.')
    parser.add_option('-C', '--clear', action='store_const', const='clear',
                      help='Clear all tags and metadata froma file.', dest='command')
    (options, args) = parser.parse_args()

    # Generate files list.
    files = []
    for item in args:
        if os.path.exists(item):
            (root, ext) = os.path.splitext(item)
            if ext.lower() == '.mp3':
                audio_file = ID3(item)
                files.append(audio_file)
            else:
                sys.stdout.write('Cannot determine filetype: ')
                print item
        else:
            print "File " + item + " not found."
            sys.exit(1)
    
    commands[options.command](options, files)

    
if __name__ == "__main__":
    main()
