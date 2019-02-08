input('Hello I made this program for learn your age.Ok lets start with enter a key.')

Months_Name=['Jan','Feb','Mar','May','Apr','Jun','July','Aug','Sep','Oct','Nov','Dec']

birth_of_year=input("please enter your year")
birth_of_month=input('please enter your month')

for index in range(0,12):
    if(Months_Name[index]==birth_of_month):
        x=index

current_year=input('what year is this year')
current_mount=input('what month is this month')

for index in range(0,12):
    if(Months_Name[index]==current_mount):
        y=index

month=y-x

year=int(current_year)-int(birth_of_year)
print("Your year is {} Year".format(year))
print("Your month is {} Month".format(month))

