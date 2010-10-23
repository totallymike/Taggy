import sys
from mutagen.mp3 import MP3
from mutagen import id3
from taggy.taggy_base import TaggyBase

class TaggyMp3(TaggyBase):
    """Class for dealing with tags in MP3 files.

    Inherits its primary functions from audio_base; the basic
    documentation for many of the functions herein are described
    in the documentation for audio_base, with differences
    noted here.
    """
    def __init__(self, file_path):
        """
        Generate mutagen.id3.ID3 object from file.  Failing that,
        generate mutagen.mp3.MP3 object to populate with "ID3" object.
        """
        try:
            self.audio = MP3(file_path)
        except IOError:
            print "File " + file_path + " not found.  Exiting."
            sys.exit(1)
        
