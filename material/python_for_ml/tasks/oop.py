'''class student():
    student_name='amit'
    studen_age='15'
    studnt_gpa='3.99'
    student_gender='male'
    
    def student_info(x):
        print('student name: {student_name}')
        print(f'student age: {studen_age}')
        print(f'student gpa: {studnt_gpa}')
        print(f'student gnder: {student_gender}')'''

'''f1=student()
f1.student_name='raf'
f1.student_info()
print(f1.student_name)'''

class person():
    name='some one'
    age='25'
    
    def print_person(self):
        print(f'good boy {self.name}')

'''d1 = person()
d2 = person()
d3 = person()
d1.print_person()
d3.name = 'anthor one'
d3.oooo = 'so'
print(person.__dict__)
print(d2.__dict__)
print(d3.__dict__)
print(d3.oooo)'''
#person().print_person()


'''class student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def student_info(self):
        print(f'student name: {self.name}')
        print(f'student age: {self.age}')
s1 = student('kk','mm')
s1.student_info()'''

class calculator1():
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    def sumation(self): return self.n1+ self.n2
    def subtraction( self): return  self.n1- self.n2
    def muliplication( self): return  self.n1* self.n2
    def division( self): return  self.n1/ self.n2
    def power( self): return  self.n1** self.n2
    
if __name__=="__main__":
    c1=calculator1(2,5)
    print(c1.sumation())
    
    
'''from abc import ABC , abstractmethod
class Animal(ABC):
    name ='kl'
    @abstractmethod
    def move(self):
        pass
class bird(Animal):
    def move(self):
        print("move from bird")
class cat(Animal):
    def move(self):
        print('move cat')
        
        
a=Animal()
a.name='lk'
#a.move()'''

'''class a():
    def f(self):
        print('i am in a')
class b(a):
    pass
class c():
    def f(self):
        print('i am in c')
class d(c,b):
    pass
x=d()
x.f()'''

'''class calculator():
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def calc_oper(): return input('you can choose an operation from the following list:\n- Addition\n- '+
            'Subtraction\n- Multiplication\n- Division\n- Exit\n').lower() 
    #function description: it asks and gets answer for which operation is wanted (easier to call)
    #function parameter: non
    #function return: which operated is wanted
    #function return type: string

    def numb_input():
        
        #function description: it asks and gets numbers for arethmatic operation and verify the number
        #function parameter: non
        #function return: number
        #function return type: flaot
        
        str_num = input('enter number\n')
        
        if str_num.isnumeric():
            return float(str_num)
        
        else:
            print('Invalid number')
            return calculator.numb_input()
        
    def calc_process(frist_n,sec_n,oper):
        
        #function description: it applys the chosen operation and varify if the operation is applicable or not
        #function parameters: oper: the operation, frist_n: first number, sec_n: second number
        #function parameters type: oper: string, frist_n: float, sec_n: float
        #function return: new_op function to continue or print good bye message  or repeat because of invalid operation
        #function return type: function or nothing
        
        a = frist_n
        b= sec_n
        
        if oper == 'addition':
            final_number = frist_n + sec_n
            print(f'The result of adding {frist_n} and {sec_n} is {final_number}.')
            return calculator.new_op(final_number)
        
        elif oper == 'subtraction':
            final_number=frist_n - sec_n
            print(f'The result of subtracting {frist_n} and {sec_n} is {final_number}.')
            return calculator.new_op(final_number)
        
        elif oper == 'multiplication':
            final_number=frist_n * sec_n
            print(f'The result of multiplying {frist_n} by {sec_n} is {final_number}.')
            return calculator.new_op(final_number)
        
        elif oper == 'division':
            while sec_n == 0:
                print('The second number can\'t be zero in division\n')
                sec_n=calculator.numb_input()   
                
            final_number=frist_n / sec_n
            print(f'The result of dividing {frist_n} by {sec_n} is {final_number}.')
            return calculator.new_op(final_number)
        
        elif oper == 'exit':
            print('Thank you for using R Calculator')
            
        else:
            print('Invalid choice')
            return calculator.calc_process(a,b,calculator.calc_oper())
            
        
    def new_op(final_number):
        
        #function description: it complete the calculator operations with the last result 
        #function parameters: oper: the operation
        #function parameters type: final_number: float
        #function return: new_op function to continue or calc_process function to start new operation or print good bye message or repeat because of invalid operation
        #function return type: function or nothing
        
        op=input('Continue with the final answer or Enter two new numbers\n- continue\n- New operation\n- Exit\n').lower()
        
        if op == 'continue':
            frist_n = final_number
            return calculator.calc_process(final_number,calculator.numb_input(),calculator.calc_oper())
        
        elif op == 'new operation':
            f = 0
            return calc_process(numb_input(),numb_input(),calc_oper())
        
        elif op == 'exit':
            print('Thank you for using R Calculator')
            
        else:
            print('Invalid choice')
            return new_op(final_number)
        
calc_process(numb_input(),numb_input(),calc_oper())'''
        