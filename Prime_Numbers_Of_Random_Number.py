
def Prime_Numbers_Of_Random_Number(min,max):
    import random
    a = random.randint(min,max)
    old_a = a
    c = set()
    for x in range(a-1,2,-1):
        if a%x==0:
            b=a//x


            gate = True

            for p in range(x-1,2,-1):
                if x%p==0:
                    a=x
                    gate=False
                    break
            if gate==True:
                c.add(x)




            gate = True

            for p in range(b-1,2,-1):
                if b%p==0:
                    a=x
                    gate=False
                    break

            if gate==True:
                c.add(b)



    if c==set():
        return print(f"This is a prime number:{old_a}")
    else:
        return print(f"This is not a prime number:{old_a}.And prime elements of That number is {c}")

Prime_Numbers_Of_a_Random_Number(20000,2000000)

#Enter max and min value(There's no limit by the way).
#Function chooses a number between min and max.And shows prime numbers of That Number.
#For ex: 81 = 3*3*3*3 --- it displays 3
#It doesn't display same prime numbers.