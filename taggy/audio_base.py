class audio_base:
    """Base class to be inherited by other audio types (e.g. mp3 or flac types).

    Includes a number of methods to be overwritten by inheriting classes:
    get_tags():      Return a dictionary of the tags embedded within a given
                     file, titled in a friendly way.
                     e.g. ['Title': 'Money', 'Artist': 'Pink Floyd']
    get_tags_raw():  Return a dictionary of the tags embedded within a given
                     file titled as they are in their individual specs.
                     e.g. ['TIT2': 'Money', 'TPE2': 'Pink Floyd'] (for ID3)
    clear_tags()     Delete all tags and metadata from the file.
    """
    def __init__(self, file_path):
        """Establishes the filename"""
        self.file_name = file_path
    
    def get_tags():
        raise NotImplementedError("Function undefined")

    def get_tags_raw():
        raise NotImplementedError("Function undefined")

    def clear_tags():
        raise NotImplementedError("Function undefined")
