def min_number(start,finish,increment):
    if start==0:
        return print("None of numbers divided by 0.")

    mylist=range(start,finish+1,increment)
    min_number=0
    count=0
    gate = False
    while(gate==False):
        min_number+=1
        for y in mylist:
            if min_number%y==0:
                count+=1

        if count==len(mylist):
            gate=True
        else:
            count = 0

    return min_number

print(min_number(1,10,1))

#I find minumum value of divided by your array.
#Your array is evenly spaced
#First of All you should enter start finish points and increment.
#İf you increase distance of your array.Program calculate slowly.