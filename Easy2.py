a=input('Enter edge of A:')
a=int(a)

b=input('Enter edge of B:')
b=int(b)

Gate=True
while(Gate==True):
    c=input('Enter edge of C:')
    c=int(c)
    if(c<=a+b):
        if(c>=a-b):
            Gate=False

if(a>b):
    if(b>c):
        print(f'{a}>{b}>{c}')
    elif(b==c):
        print(f'{a}>{b}={c}')
    elif(a>c):
        print(f'{a}>{c}>{b}')
    elif(c>a):
        print(f'{c}>{a}>{b}')
    else:
        print(f'{a}={c}>{b}')
elif(b>a):
    if(a>c):
        print(f'{b}>{a}>{c}')
    elif(a==c):
        print(f'{b}>{a}={c}')
    elif(b>c):
        print(f'{b}>{c}>{a}')
    elif(b==c):
        print(f'{b}={c}>{a}')
    else:
        print(f'{c}>{b}>{a}')


else:
    if(a>c):
        print(f'{a}={b}>{c}')
    elif(c>a):
        print(f'{c}>{a}={b}')
    else:
        print(f'{a}={b}={c}')