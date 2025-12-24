def greeting(name="Muthu",age=18 , city="sivakasi"): #Greeting System
    print("Name : " ,name)
    print("Age : ",age)
    print("City : ",city)
greeting(age=20)

def student1(*mark): #STUDENT MARKS CALCULATOR
    return  mark
def total(m):
    return sum(m)
def avarge(m):
    return sum(m) / len(m)
def high(m):
    return max(m)
mark = student1(10,20,30,40)
print("Mark : ", mark)
print("Total :",total(mark))
print("Avarage :",avarge(mark))
print("Max :",high(mark))

def Muthu(**info): #USER PROFILE BUILDER
    return info
A=Muthu(Name = "Muthu ",age=20,Email="23urit024@aaacet.ac.in",city="Sivakasi",skills="Python,AIML")
print(A)

task=[] #todo list
def add_task(add):
    task.append(add)
def remove_task(rem):
    if rem in task :
       task.remove(rem)
    else:
        print("Enter the worng input")
add = input("Enter the task : ")
add_task(add)
print(task)
rem=input("Enter the Remove task : ")
remove_task(rem)
print("remaing task : ",task)

def num(n): #Count down logic 
    if n<0:
        return 0
    print(n)
    num(n-1)
n=int(input("Enter the number :"))
value = num(n)
print(value)