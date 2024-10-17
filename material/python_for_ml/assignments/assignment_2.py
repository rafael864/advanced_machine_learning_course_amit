##task1

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
        return numb_input()
    
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
        return new_op(final_number)
    
    elif oper == 'subtraction':
        final_number=frist_n - sec_n
        print(f'The result of subtracting {frist_n} and {sec_n} is {final_number}.')
        return new_op(final_number)
    
    elif oper == 'multiplication':
        final_number=frist_n * sec_n
        print(f'The result of multiplying {frist_n} by {sec_n} is {final_number}.')
        return new_op(final_number)
    
    elif oper == 'division':
        while sec_n == 0:
            print('The second number can\'t be zero in division\n')
            sec_n=numb_input()   
            
        final_number=frist_n / sec_n
        print(f'The result of dividing {frist_n} by {sec_n} is {final_number}.')
        return new_op(final_number)
    
    elif oper == 'exit':
        print('Thank you for using R Calculator')
        
    else:
        print('Invalid choice')
        return calc_process(a,b,calc_oper())
        
    
def new_op(final_number):
    
    #function description: it complete the calculator operations with the last result 
    #function parameters: oper: the operation
    #function parameters type: final_number: float
    #function return: new_op function to continue or calc_process function to start new operation or print good bye message or repeat because of invalid operation
    #function return type: function or nothing
    
    op=input('Continue with the final answer or Enter two new numbers\n- continue\n- New operation\n- Exit\n').lower()
    
    if op == 'continue':
        frist_n = final_number
        return calc_process(final_number,numb_input(),calc_oper())
    
    elif op == 'new operation':
        f = 0
        return calc_process(numb_input(),numb_input(),calc_oper())
    
    elif op == 'exit':
        print('Thank you for using R Calculator')
        
    else:
        print('Invalid choice')
        return new_op(final_number)
    


##task2
import os,  random
def create_folder():
    
    #function description: it create folder by asking for the pass and the folder name and check if that folder exit or no
    #function parameters: non
    #function return: the path of the folder and added to it its name
    #function return type: string
    
    user_folder_path = input('enter folder path\n')
    user_folder_name = input('enter folder name\n')
    path1=os.path.join(user_folder_path, user_folder_name)
    
    if  not(os.path.exists(path1)):
        os.makedirs(path1)
        
    else:
        print("Directory already exists:", path1)
        
    return path1


def create_files(path1):
    
    #function description: it creates files after checking of their existing one by one using for loop 
    #function parameters: path1: the path of the folder where the function creates the files
    #function parameters type: path1: string
    #function return: list of the created files
    #function return type: list
    
    for i in range(4):
        if not os.path.exists(os.path.join(path1, f"file{str(i)}.txt")):
            with open(os.path.join(path1, f"file{str(i)}.txt"), "a+") as file: 
                file.write(f"file{str(i)}.txt")
                
    created_files=os.listdir(path1)
    print('the number of created files is ',len(created_files))
    
    return created_files

def remove_r(path1,created_files):
    
    #function description: it chooses half the numbr of files randomly and remove them 
    #function parameters: path1: the path of the folder where the function remove the files, created_files: the files to choose among them
    #function parameters type: path1: string, created_files:list
    #function return: non
    
    chosen_created_files=random.sample(created_files, k=int(len(created_files)/2))
    
    for i in chosen_created_files:
        os.remove(os.path.join(path1, i))
        
    print('the number of remaining files is ',len(os.listdir(path1)))


def display():
    #function description: to use the other function easily and display the result
    # no parameters and no return value
    cr_fd = create_folder()
    cr_fl = create_files(cr_fd)
    remove_r(cr_fd,cr_fl)

#execution
#pre_defined_path = "C:\Users\Lenovo\Desktop\amit"
#folder_ name = "t2"
calc_process(numb_input(),numb_input(),calc_oper())
display()
