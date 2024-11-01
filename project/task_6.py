import os
def read_txt_file(file_path):
    #reads the contents of a specified text file and returns it as a string.
    if os.path.exists(file_path):
        try:
            input_file = open(file_path,'r')
            content = input_file.read()
            input_file.close()
            return content
        except:
            print('os error')
    else:
        print('the file doesn\'t exist')


class UserExtractor():
    def __init__(self,file_path):
        #- file_path: The path to the text file.
        #- usernames: A dictionary to store usernames.
        #self.file_path = input('The path to the text file.')
        self.file_path = file_path
        self.usernames = dict()
    def extract_usernames(self):
        if read_txt_file(self.file_path):
            content = read_txt_file(self.file_path).split('\n')
            for i in content:
                line = i.split(':')
                self.usernames[line[0]] = line[1]
            return self.usernames
        else:
            return 'an error happened'
if __name__ == "__main__":
    file=UserExtractor(r'C:\Users\Lenovo\Desktop\amit\advanced_machine_learning_course_amit\project\task_6.txt')
    print(file.extract_usernames())
    