#!/usr/bin/env python
# A command-line ID3 tagger for various audio file formats.  Extremely incomplete.

import sys
import os.path
from tag import ID3
from glob import glob
from optparse import OptionParser


def list(options, files):
    """List the files."""
    if options.raw:
        
def main():

## Option parsing.
    usage = u"taggy.py [options] filename(s)"
    parser = OptionParser(usage=usage)
    parser.add_option("-l", "--list", action="store_const", const="list",
                      help="list tags embedded in a file", dest="command")
    parser.add_option('-r', '--raw', action="store_true", dest='raw', default=False)
    (options, args) = parser.parse_args()

    # Generate files list.
    files = []
    for item in args:
        if os.path.exists(item):
            files.append(item)
        else:
            print "File " + item + " not found."
            sys.exit(1)
    
    options.command(options, files)

    
if __name__ == "__main__":
    main()
