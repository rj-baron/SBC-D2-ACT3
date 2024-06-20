from random import randint

ako = input(" '0' hayang to  '1' kulob: ")
ako = int(ako)

C2 = randint(0,1)
C3 = randint(0,1)


choice = {0: "hayang", 1: "kulob"}
print(f"ako: {choice [ako]}")
print(f"C2: {choice [C2]}")
print(f"C3: {choice [C3]}")



if (ako == 0 and C2 == 1 and C3 == 1) or (ako == 1 and C2 == 0 and C3 == 0):
    print("you win")
elif (ako == 1 and C2 == 0 and C3 == 1) or (ako == 0 and C2 == 1 and C3 == 0):
    print("C2 win")
elif (ako == 1 and C2 == 1 and C3 == 0) or (ako == 0 and C2 == 0 and C3 == 1):
    print("C3 win")
else:
    print("draw1")