num1=input("Enter first number1:")
num1=int(num1)
num2=input("Enter Second number2:")
num2=int(num2)
gcd=1

if(num2>num1):
    small_num=num1
elif(num2<num1):
    small_num=num2
else:
    small_num=num1 #You can write num2 equals small_num


for a in range(small_num,1,-1):
    if(num1%a==0):
        if(num2%a==0):
            if(gcd<a):
                gcd=a
                print(f'Greatest Common Divisor is {gcd}')

if(gcd==1):
    print(f'Greatest Common Divisor is {gcd}')