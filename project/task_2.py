class calculator_processes():
    def __init__(self):
        n1 = input('enter first number\n')
        self.n1 = float(n1)    
    def addtion(self):
        n2 = float(input('enter second number\n'))
        self.n1 += n2
        return self.n1 
    def subtraction(self):
        n2 = float(input('enter second number\n'))
        self.n1 -= n2
        return self.n1
    def multiplication(self):
        n2 = float(input('enter second number\n'))
        self.n1 *= n2
        return self.n1
    def division(self):
        n2 = float(input('enter second number\n'))
        while n2 == 0:
            n2 = float(input('enter second number again it can\'t be zero in division\n'))
        self.n1 /= n2
        return self.n1 
    def exponentiation(self):
        n2 = float(input('enter second number\n'))
        self.n1 **= n2
        return self.n1 
    def process(self):
        pro = input('enter the name of process you want:\n- addition\n- subtraction\n- multiplication\n- division\n- exponentiation\n- new process\n- exit\n')
        return pro
    
if __name__=='__main__':
    calculate = calculator_processes()
    while True :
        pro = calculate.process()
        if pro == 'addition':
            print(calculate.addtion())
        elif pro == 'subtraction':
            print(calculate.subtraction())
        elif pro == 'multiplication':
            print(calculate.multiplication())
        elif pro == 'division':
            print(calculate.division())
        elif pro == 'exponentiation':
            print(calculate.exponentiation())
        elif pro == 'exit':
            print('thanks for using our calculator')
            break
        elif pro == 'new process':
            calculate.n1 = float(input('enter first number\n'))
        
        else:
            print('invalid process try again')
            