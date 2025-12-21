
num = int(input("Enter the number :")) #positive or Nagative Number
if num > 0:
    print(f'{num} is Postive Number')
elif num == 0 :
    print(f'{num} is equal to zero ')
else:
    print(f'{num} is nagative number ')
num1 = int(input("Enter the number 1"))#add or even number
if (num1 % 2) == 0:
    print(f'{num1} is a even number')
else:
    print(f'{num1} is odd number ')
age = int(input("Enter the age :"))# age
if age <= 18 :
    print("your not eligiable for voting ")
elif age == 18 :
    print(" your apply the vode")
else :
    print("You are eligible for voting ")
number1 = int(input("Enter the number 1 :"))# among three number
number2 = int(input("Enter the number 2 :"))
number3 = int(input("Enter the number 3 :"))
if number1 > number2 and number1 > number3 :
    print(f'{number1} is among number ')
elif number2 > number1 and number2 > number3 :
    print(f'{number2} is among number ')
else:
    print(f'{number3} is among number ')
Maths = int(input("Enter the Maths mark :"))# grade
if Maths >= 90 and  Maths == 100 :
    print(f'{Maths} grade is O')
elif Maths >= 80 :
    print(f'{Maths} grade is A+')
elif Maths >= 70 :
    print(f'{Maths} grade is A')
elif Maths >= 60 :
    print(f'{Maths} grade is B+')
elif Maths >= 50 :
    print(f'{Maths} grade is B')
elif Maths >= 45 :
    print(f'{Maths} grade is C')
else:
    print(f'{Maths} grade is U (Arrear)')



