class TaggyBase:
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
    set_raw_tag(tag, value):
        Define given raw tag (e.g. TIT2 for ID3) with value.
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
    
    def set_raw_tag():
        raise NotImplementedError("Function undefined.")
    def print_tags():
        raise NotImplementedError("Function undefined.")
    def print_tags_raw():
        raise NotImplementedError("Function undefined.")
    def clear_tags():
        raise NotImplementedError("Function undefined.")
    def set_title():
        raise NotImplementedError("Function undefined.")
    def set_album():
        raise NotImplementedError("Function undefined.")
    def set_artist():
        raise NotImplementedError("Function undefined.")
    def set_album_artist():
        raise NotImplementedError("Function undefined.")
    def set_genre():
        raise NotImplementedError("Function undefined.")
    def set_track_number():
        raise NotImplementedError("Function undefined.")
    def set_year():
        raise NotImplementedError("Function undefined.")
