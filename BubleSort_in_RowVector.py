quantity=input('Please enter quantity')
quantity=int(quantity)

numbers=[0]*quantity

for index in range(0,quantity):
    numbers[index]=input(f'{index} column:')
    numbers[index]=int(numbers[index])



for index in range(0,quantity-1):

 for index in range(0,quantity-1):

    if(numbers[index]<numbers[index+1]):
        copy=numbers[index]
        numbers[index]=numbers[index+1]
        numbers[index+1] = copy



print(numbers)