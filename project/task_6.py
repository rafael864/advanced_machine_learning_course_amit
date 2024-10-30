import os
def read_txt_file(file_path):
    #reads the contents of a specified text file and returns it as a string.
    if os.file_path.exists():
        input_file = open(file_path,'r')
        content = input_file.read()
        input_file.close()
        return content
    else:
        print('the file doesn\'t exist')


class UserExtractor():
    def __init__(self):
        #- file_path: The path to the text file.
        #- usernames: A dictionary to store usernames.
        self.file_path = input('The path to the text file.')
        self.usernames = dict()