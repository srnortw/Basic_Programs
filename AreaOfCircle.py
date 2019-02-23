from math import pi as pie

def area_of_pie(r):
    Area=2*pie*(r**2)
    return Area

m=int(input('please enter radius of circle'))
print(f'area of circle is {area_of_pie(m)}')