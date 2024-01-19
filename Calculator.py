print(" ***** CALCULATOR USING PYTHON *****")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Enter 1 for 'Addition' \n Enter 2 for 'Subtraction' \n Enter 3 for 'Multiplication' \n Enter 4 for 'Division'")

Entered_number=int(input(" choose from 1 till 4 "))

if Entered_number == 1:
    print(num1+num2)

elif Entered_number == 2:
    print( num1-num2)

elif Entered_number == 3:
    print(num1*num2)   

elif Entered_number == 4:
    print(num1/num2)

else:
    print("Invalid Input")    







