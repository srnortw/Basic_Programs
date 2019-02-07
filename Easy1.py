gate=1
while(gate==1):
    num=input('Please enter a Number')
    num=int(num)
    if (num<99):
        if(num>10):
            gate=0


fir_dig=num%10
sec_dig=(num-fir_dig)/10



if (fir_dig==7):
    print(num)
    print(f'First digit={fir_dig}')
elif(fir_dig==4):
    print(num)
    print(f'First digit={fir_dig}')
else:
    print('First digit of number is not 7 or 4')


if (sec_dig==7):
    print(num)
    print(f'Second Digit={sec_dig}')
elif(sec_dig==4):
    print(num)
    print(f'Second Digit={sec_dig}')
else:
    print('Second digit of Number is not 4 or 7')
