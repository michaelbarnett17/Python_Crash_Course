from pathlib import Path
from os import getcwd

class MyFileWriter:

    def __init__(self):
        pass

    def write_message_to_file(self, message, file_location):

        Path(file_location).write_text(message)















    def print_current_directory(self):

        print(getcwd())