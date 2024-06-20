from random import randint

first1 = int(input("Una:"))
second2 = int(input("Ikaduha:"))
third3 = int(input("Ikatulo:"))

resulta1 = randint(0,9)
resulta2 = randint(0,9)
resulta3 = randint(0,9)

print("imong bet:", first1, second2, third3)
print("Resulta: ", resulta1, resulta2, resulta3,)

if first1 == resulta1 and resulta2 == resulta2 and resulta3 == resulta3:
    print("You win!")

elif (first1 == resulta1 and second2 == resulta3 and third3 == resulta2 ) or (first1 == resulta3 and second2 == 
resulta1 and third3 == resulta2 ) or (first1 == resulta3 and second2 == resulta2 and third3 == 
resulta3) or (first1 == resulta3 and second2 == resulta1):
    print("Partial win!")
else:
    print("Patad patad pud sig ober think nga makadaug!")
