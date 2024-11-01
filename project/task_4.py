import os 
class TextFileReader():
    def __init__(self,file_path):
        #Initialize the file_path attribute.
        self.file_path = file_path
    def read_file(self): 
        #This method should open the file, read its contents, and store the contents in an attribute named content.
        input_file = open(self.file_path,'r')
        self.content= input_file.read().strip()
        input_file.close()
    def count_lines(self):
        #This method should return the number of lines in the file.
        lines = self.content.split('\n')
        print(len(lines))
    def count_words(self):
        #This method should return the total number of words in the file.
        content = self.content.replace('\n',' ')
        words = content.split(' ')
        print(len(words))
    def count_characters(self):
        #This method should return the total number of characters in the file.
        print(len(self.content.replace('\n','').replace(' ','')))
    def display_content(self):
        #This method should print the content of the file.
        print(self.content)
if __name__ == "__main__":
    path = r'C:\Users\Lenovo\Desktop\amit\advanced_machine_learning_course_amit\project\task_6.txt'
    f = TextFileReader(path)
    f.read_file()
    f.count_lines()
    f.count_words()
    f.count_characters()
    f.display_content()