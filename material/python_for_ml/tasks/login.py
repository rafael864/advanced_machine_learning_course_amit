import random
#username
X = 'kal'
#password
P = '2222'

def validation():
    while True:
        x = input('name: ')
        if x == X:
            p = input('password: ')
            if p == P :
                s= random.randrange(10000,100000)
                print('variviction code is: ',s)
                while True:
                    l = input('enter varivication code: ')
                    if l == str(s):
                        print('welcome')
                        break
                    else:
                        print('incorrect varification code, try again')
                break
            else:
                print('invalid password, try again')
        else:
            print('invalid name, try again')
            