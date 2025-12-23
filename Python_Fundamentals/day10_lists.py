menu = ["pencil","pen","watch","phone","laptop","car"]
print(menu)
user_list = []
number= int(input("Enter the add number of items :"))
for i in range(number):
    m=input("add item : ")
    user_list.append(m)
    print("User list : " ,user_list)
n= input("enter the remove items : ")
if n in user_list:
    user_list.remove(n)
    print("After removing:", user_list)
else:
    print("Item not found in list")

