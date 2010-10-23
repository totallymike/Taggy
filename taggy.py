#!/usr/bin/env python
# A command-line ID3 tagger for various audio file formats.  extremely incomplete.

import os.path
from glob import glob
from optparse import OptionParser
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen import id3
def main():

##             Option parsing.
    usage = u"taggy.py [options] filename(s)"
    parser = OptionParser(usage=usage)
    parser.add_option("-l", "--list", action="store_const", const="list",
                      help="list tags embedded in a file", dest="command", default=False)
    (options, args) = parser.parse_args()

    
if __name__ == "__main__":
    main()
