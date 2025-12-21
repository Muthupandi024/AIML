def arthimrtic(num1 ,num2) :
    return num1 + num2 ,num1 - num2,num1 * num2,num1 / num2,num1 % num2

def comparesion(num1 , num2):
    return num1 < num2,num1 > num2,num1 <= num2,num1 >= num2,num1 != num2

def logical (num1 , num2):
    return num1 and num2,num1 or num2,not num2

num1 = int(input("Enter the number 1 :"))
num2 = int(input("Enter the number 2 :"))
print(arthimrtic(num1,num2))
print(comparesion(num1,num2))
print(logical(num1,num2))



