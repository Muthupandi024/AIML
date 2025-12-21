
n= int(input("Enter the number of students :"))
for tamil in range (n):
    name = str(input("Enter the name :"))
    age = int(input("Enter a age :"))
    tamil_mark = int(input("enter the tamil mark "))
    english_mark = int(input("enter the english mark "))
    maths_mark = int(input("enter the maths mark "))
    physics_mark = int(input("enter the physics mark "))
    chemistry_mark = int(input("enter the chemistry mark "))
    avg=((tamil_mark+english_mark+maths_mark+chemistry_mark+physics_mark)/5),2
    print(f'{name}, avg is ,{avg}')

