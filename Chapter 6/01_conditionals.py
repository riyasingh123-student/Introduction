a = int(input("Enter your age: "))

# If else statement
if(a>=20):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("Your are entering an invalid negative age")

elif(a==0):
    print("Your are entering 0 which in not an valid case")

else:
    print("You are below the age of consent")

print("End of program")