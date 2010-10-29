import sys
from mutagen.mp3 import MP3
from mutagen import id3
from tag import Base

_tag_types = {
    'TIT2': 'Title',
    'TALB': 'Album',
    'TPE2': 'Album Artist',
    'TPE1': 'Artist',
    'TRCK': 'Track Number',
    'TCON': 'Genre',
    'TPOS': 'Disc',
}

class ID3(Base):
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
        Base.__init__(self, file_path)

    def print_tags(self, verbose=False):
        """Print id3 tags in plain english.  One per line."""
        for tag in self.audio:
            if tag in _tag_types:
                # stdout.write to suppress newline.
                sys.stdout.write(_tag_types[tag] + ': ')
                print self.audio[tag]
            elif verbose:
                if tag.startswith('PRIV'):
                    print 'PRIV: ' + self.audio[tag].owner
                    print self.audio[tag].data
                else:
                    sys.stdout.write(tag + ': ')
                    print self.audio[tag]
    
    def print_tags_raw(self):
        """Print raw id3 tags.  One per line."""
        print self.audio.pprint()
    
    def clear_tags(self):
        """Remove all tagging and metadata from a file."""
        self.audio.clear()
        self.audio.save()

    
