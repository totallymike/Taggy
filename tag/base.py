class Base:
    """Base class to be inherited by other audio types (e.g. mp3 or flac types).

    Includes a number of methods to be overwritten by inheriting classes:
    print_tags():
        Print tags embedded in file in a human-readable fashion, e.g.:
            Title: Money
            Artist: Pink Floyd
    print_tags_raw():
        Print tags embedded in file as labelled in specification, e.g.:
            TIT2: Money
            TPE2: Pink Floyd
        for ID3 format.
    clear_tags():
        Delete all tags and metadata from the file.
    set_title(value):
    set_album(value):
    set_artist(value):
    set_album_artist(value):
    set_genre(value):
    set_track_number(value):
    set_year(value):
        Define corresponding tag with specified value.
    """
    def __init__(self, file_path):
        """Establishes the filename"""
        self.file_name = file_path
    
    def print_tags(self):
        pass
    def print_tags_raw(self):
        pass
    def clear_tags(self):
        pass
    def set_title(self):
        pass
    def get_title(self):
        pass
    def set_album(self):
        pass
    def get_album(self):
        pass
    def set_artist(self):
        pass
    def get_artist(self):
        pass
    def set_album_artist(self):
        pass
    def get_album_artist(self):
        pass
    def set_genre(self):
        pass
    def get_genre(self):
        pass
    def set_track_number(self):
        pass
    def get_track_number(self):
        pass
    def set_year(self):
        pass
    def get_year(self):
        pass;
