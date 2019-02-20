def centered_average(nums):
    oldnums=nums

    mx=max(nums)
    mn=min(nums)
    t=0
    out=0
    out1=0
    for x in nums:
        if mx==x:
            if out<2:
                out+=1
                nums.pop(nums.index(x))
                continue
        if mn==x:
            if out1<2:
                out1+=1
                nums.pop(nums.index(x))
                continue
        t=t+x


    avrg=t/(len(nums))
    smalldiff=max(map(abs,oldnums))


    for x in nums:
        diff=abs(avrg-x)
        if diff<smalldiff:
            smalldiff=diff
            y=x

    return nums[nums.index(y)]

"""
    This function calculates average of list and displays nearest value of average in that list
    If you enter same 2 times max numbers.Those don't effect the value of average.
same with same 2 times min numbers
    Third ones effect the value of average.
"""
print(centered_average([95,95,95,1,1,0]))
#Output is 1
#(95+1+1)/3=32.3
#32.3 is nearest to 1