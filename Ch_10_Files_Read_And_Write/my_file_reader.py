from pathlib import Path
from os import getcwd

class MyFileReader:

    def __init__(self, file_location=""):

        self.file_location = file_location


    def process_pi(self):

        path = Path(self.file_location)
        contents = path.read_text().rstrip()
        print(contents)


    def process_pi_single_line(self):

        path = Path(self.file_location)

        contents = path.read_text()
        lines = contents.splitlines()

        pi_single_line = ""

        for line in lines:
            pi_single_line += line.lstrip()

        print(pi_single_line)


    def process_pi_million_digits(self):

        path = Path(self.file_location)

        contents = path.read_text()
        lines = contents.splitlines()

        pi_million = ""

        for line in lines:
            pi_million += line.lstrip()

        print(pi_million[:100])
        print(len(pi_million))


    def process_birthday_in_pi(self, birthday):

        path = Path(self.file_location)

        contents = path.read_text()
        lines = contents.splitlines()

        pi_million = ""

        for line in lines:
            pi_million += line.lstrip()


        if str(birthday) in pi_million:
            print("Your birthday is in the first million digits of pi")
        else:
            print("Your birthday is not in the first million digits of pi")


    def print_current_directory(self):

        print(getcwd())