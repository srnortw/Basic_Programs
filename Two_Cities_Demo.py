print("There are two cities.\nYou'll enter distance between them.")
print("And there are 2 bicyclist.\nEach one is in diffrent cities.")
print("You'll enter their velocity.And I'll find their meeting point.")
input("Note:Way of between 2 cities is straight.\nIf you want to start enter a key.")


question=input("What is your units of inputs km or m ? :")
question1=input("What is your units of result km or m ? :")

question=question.lower()
question1=question1.lower()


dist=float(input("What is distance between 2 cities:"))
bisc1=float(input("Please enter velocity of Biscyle-1:"))
bisc2=float(input("Please enter velocity of Biscyle-2:"))


ratio=bisc1/bisc2
coefficent=dist/(1+ratio)

fw=coefficent*ratio
sw=coefficent*1

if question=="km":
    if question1=="m":
        fw *= 1000
        sw *= 1000

elif question=="m":
    if question1=="km":
        fw *= (1 / 1000)
        sw *= (1 / 1000)

print(f'Meeting point from First city:{fw}{question1}')
print(f'Meeting point from Second city:{sw}{question1}')