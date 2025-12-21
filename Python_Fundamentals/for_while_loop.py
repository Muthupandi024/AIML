start = int(input("Enter the start number : ")) #TASK 1 – Number Range Printer
end = int(input("Enter the end number : "))
for i in range(start,end+1) :
    print(i)

i=0 #TASK 2 – Even & Odd Counter (WHILE LOOP)
even = 0
add =0
while i < 50 :
    if i%2==0:
        print(f'{i} is even values ')
        even = even+1
    else:
        print(f'{i} is odd values')
        add=add+1
    i+=1

num = int(input("Enter the number : ")) #TASK 3 – Multiplication Table Generator
for i in range(1,11) :
    print(f'{num}*{i}={num*i}')

password = 'Python123' #user password
user_password = ""
while user_password != password :
    user_password=input("Enter the password : ")
    if password == user_password :
        print("user login")
    else:
        print("wrong password")

number = int(input("Enter the Number : "))
for i in range(1,number+1):
    for j in range (i+3,9):
        print("*" , end="")
    print()

for i in range(1,20):
    if i==5:
        continue
    elif i==15:
        break
    print(i)



