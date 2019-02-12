def even(a):

    for x in range(1,5):
        print(a**2*x)

    return

def odd(a):

    for x in range(1,5):
        print(a**2*x)

    return

a=int(input("Please enter number"))

if a%2==0:
    even(a)
else:
    odd(a)
