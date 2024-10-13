###task 1###
address = 'Amit_ml@gmail.edu'
#spliting user name, domain and domain ending
x = address.split('@')
y=x[1].split('.')

#check if the domain is valid number of @ and .
check_at = len(x)==2
check_dotes = len(y)>=2

if check_at and check_dotes :
    #assigning values to variables
    user_name = x[0]; domain = y[0]; domain_ending = y[1]
    print('valid email\nUser name is {}\nDomain is {}'.format(user_name,domain))
    if domain_ending=='.com':
        print('Commercial Domain')
    elif domain_ending=='edu':
        print('Educational Domain')
    else:
        print('other domain')
else:
    print('invalid email')


###task 2,3,4###
t=''
answer_list=[]
encoded_word_list=['###!!@mocleW EPGTQ!!!6789','&&&**$gnirtS PLIO!!@1234','##$$$@!yalpstcejorp EPUVT****9887']
for encoded_word in encoded_word_list:
    for i in encoded_word:
        if i.isalpha():
            t+=i
        elif i == ' ':
            first_word=t
            t=''
    second_word=t
    
    t=''
    first = first_word[::-1]
    
    if second_word == 'EPGTQ':
        second = second_word.replace('E','')
    elif second_word == 'PLIO':
         second = second_word.replace('IO','EU')
    else:
         second = second_word.replace('EPU','APO')
         
    word=first+' '+second
    answer_list.append(word)
print(answer_list)

###task 2###
encoded_word='###!!@mocleW EPGTQ!!!6789'
first = encoded_word[encoded_word.index('m'):encoded_word.index(' ')][::-1]
second = encoded_word[encoded_word.index(' ')+1:encoded_word.index('Q')+1].replace('E','')
print(first+' '+second)

#anthor way
words=encoded_word.lstrip('!@#$%').rstrip('!@#$%6789').split()
first_word=words[0][::-1]
second_word=words[1].replace('E','')
print(first_word+' '+second_word)

###task 3###
encoded_word='&&&**$gnirtS PLIO!!@1234'
first = encoded_word[encoded_word.index('g'):encoded_word.index(' ')][::-1]
second = encoded_word[encoded_word.index(' ')+1:encoded_word.index('O')+1].replace('IO','EU')
print(first+' '+second)

#anthor way
words=encoded_word.lstrip('!@#$&*').rstrip('!@#1234').split()
first_word=words[0][::-1]
second_word=words[1].replace('IO','EU')
print(first_word+' '+second_word)


###task 4###
encoded_word='##$$$@!yalpstcejorp EPUVT****9887'
first = encoded_word[encoded_word.index('y'):encoded_word.index(' ')][::-1]
second = encoded_word[encoded_word.index(' ')+1:encoded_word.index('T')+1].replace('EPU','APO')
print(first+' '+second)

#anthor way
words=encoded_word.lstrip('!@#$&*').rstrip('!@#*987').split()
first_word=words[0][::-1]
second_word=words[1].replace('EPU','APO')
print(first_word+' '+second_word)
