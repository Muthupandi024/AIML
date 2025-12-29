note = input("Enter your note : ")
file = open("hii.txt",'a')
file.write(note + "\n")
file.close()
print("file successfully saved")

file = open("hii.txt",'r')
f=file.read()
print(f)
file.close()

stu={}
n=int(input("Enter the no of students : "))
for i in range(n):
    name = str(input("Enter the name : "))
    mark = int(input("Enter the mark : "))
    stu[name]=mark
file = open("hii.txt",'a')
file.write(str(stu))
file.close()
print("file successfully updated ...")

student = {}
file = open("hii.txt",'r')
lines = file.readlines()
file.close()
for line in lines :
    line= line.strip()
    name,mark = line.split(":")
    student[name]=int(mark)
print("Students : ",student)
add = 0
for i in student:
    add +=student[i]
print("Total mark :",add)
count = len(student)
print("Total no of student :",count)
if count == 0:
    print("count value has zero")
else:
    avg = add/count
    print("avg value : ",avg )
if avg >45 :
    print("pass")
else:
    print("fail")

