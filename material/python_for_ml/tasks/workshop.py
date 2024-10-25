import random
class factorial():
    def __init__(self,n1):
        self.n1 = n1
    def fac(self):
        if self.n1==1 or self.n1==0: return self.n1
        elif self.n1>1: return factorial(self.n1-1).fac()*self.n1
#print(factorial(4).fac())

class calculator1():
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def sumation(self): return self.n1+ self.n2
    def subtraction( self): return  self.n1- self.n2
    def muliplication( self): return  self.n1* self.n2
    def division( self): return  self.n1/ self.n2
    def power( self): return  self.n1** self.n2
class is_prime():
    def __init__(self,n):
        self.n = n
    def isPrime(self):
        for i in range(2,int(self.n/2)+1):
            if self.n % i == 0:
                return False
            return True
#print(is_prime(59).isPrime())

def dividors(n1,n2):
    mn = min(n1,n2)
    c_d =[]
    for i in range(1,mn+1):
        if n1 % i == 0 and n2 % i == 0:
            c_d.append(i)
    return c_d        
'''class longest_string():
    str1 = input('first string\n')
    str2 = input('second string\n')
    
    def l_s(self):
        res=''
        for i in range(len(self.str1)):
            for j in range(i,len(self.str1)):
                sub_str = self.str1[i:j+1]
                if sub_str in self.str2:
                    if len(sub_str)>len(res):
                        res=sub_str
        return res'''

charachters = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIASDFGHJKLZXCVBNM!@$%&#^*"
class password():  
    def __init__(self,length):
        self.length = length
    def g_p(self):
        pass_word = ""
        for i in range(self.length):
            pass_word += random.choice(charachters)
        return pass_word
import os
def read_file(path,e_path):
    input_file = open(path,'r')
    text = input_file.read()
    input_file.close()
    text=text.replace('\n',' ')
    text=text.replace('\'',' ')
    text=text.replace(':',' ')
    text=text.replace('(',' ')
    text=text.replace(')',' ')
    text=text.replace('=',' ')
    text=text.replace('.',' ')
    words = text.split(' ')
    unique_words= set(words)
    word_counts = dict()
    for i in unique_words:
        word_counts[i] = words.count(i)
        output_file=open(e_path,'w')
    for i in word_counts:
        output_file.write('{}:{}\n'.format(i,word_counts[i]))
    output_file.close()
read_file(r'C:\Users\Lenovo\Desktop\amit\advanced_machine_learning_course_amit\material\python_for_ml\tasks\workshop.py',r'C:\Users\Lenovo\Desktop\amit\advanced_machine_learning_course_amit\material\python_for_ml\tasks\work_shop.txt')
if __name__=='__main__':
    print( password(10).g_p())