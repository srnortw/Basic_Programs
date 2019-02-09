fibonacci_number=[0,1]

my_quantity=input('How many fibonacci numbers Do you need:')
my_index_of_number=input('what index of fibonacci numbers Do you want:')

my_quantity=int(my_quantity)
my_index_of_number=int(my_index_of_number)


for a in range(0,my_quantity-2):
    new_number=fibonacci_number[a]+fibonacci_number[a+1]
    fibonacci_number.append(new_number)



if(my_quantity<my_index_of_number):
    print(f'Wrong! There is not {my_index_of_number}th number')



print(f'That number is \n{fibonacci_number[my_index_of_number-1]}')


fibonacci_number[my_index_of_number-1]=str(fibonacci_number[my_index_of_number-1])
print(f'That number has \n{len(fibonacci_number[my_index_of_number-1])} digits')