list =[] #QUESTION 1 – ADD & COUNT
n = int(input("Enter the no of task : "))
for i in range(n):
    task=input("Enter the task :")
    list.append(task)
print("User list : " , list)
print("length of the task :" ,len(list))

list1 = ["phone","laptop","iphone","Samsang","Oppo","Redmi"] #REMOVE SAFELY
print(list1)
Remove_task = input("Enter the remove task : ")
if Remove_task in list1 :
    list1.remove(Remove_task)
    print(list1)
else:
    print("Ener the wrong product")

task = [] #TODO APP
n = int(input("Enter the no of task : "))
for i in range(n):
    task_name = input("Enter the task : ")
    task.append(task_name)
    print("View task : " , task)
task_remove = input("Enter the Remove task : ")
if task_remove in task :
    task.remove(task_remove)
    print(f'Sucessfully Remove {task_remove}')
    print("Remaing tasks : ",task)
else:
    print(f'Does not insert this task : {task_remove}')

mark = [10,34,23,98,2,12,45]
print("maximum element of given list : ",max(mark))
max_value = mark[0]
for i in mark :
    if i > max_value :
        max_value = i
print("maximum value of given list : ",max_value)

list2 = [1,2,2,3,4,5,5,6]
modifed_list2=[]
for i in list2 :
    if i not in modifed_list2 :
        modifed_list2.append(i)
    else:
        print("skip the element")
print("Modified element : ", modifed_list2)

