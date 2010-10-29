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
    
    def print_tags():
        pass
    def print_tags_raw():
        pass
    def clear_tags():
        pass
    def set_title():
        pass
    def get_title():
        pass
    def set_album():
        pass
    def get_album():
        pass
    def set_artist():
        pass
    def get_artist():
        pass
    def set_album_artist():
        pass
    def get_album_artist():
        pass
    def set_genre():
        pass
    def get_genre():
        pass
    def set_track_number():
        pass
    def get_track_number():
        pass
    def set_year():
        pass
    def get_year():
        pass;
