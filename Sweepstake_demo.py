import random
mynumber=random.randint(100,1000)

quantity=input('enter quantity:')
quantity=int(quantity)

numbers=quantity*[10000]
index=0

while (index<quantity):
    while(mynumber<numbers[index]):
        numbers[index] = random.randint(0, 1000)
    index=index+1

print(numbers)
print(mynumber)

