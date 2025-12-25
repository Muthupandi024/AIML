phone = {"muthu":{"phone":8015899931,"age":20}, #Data Analytics
         "raghul":{"phone":9150117404,"age":19},
         "vijay":{"phone":90982983389,"age":20},
         "ajay":{"phone":9866352883,"age":19}

         }

name = input("enter the name : ")
if name in phone:
    print(f'{name} is found ' , phone[name])
else :
    print(f'{name} is not found')

mark = {"muthu":80,"raghul":96,"ajay":89,"vijay":87  #STUDENT MARKS AVERAGE
}
add = 0
for i in mark:
    add += mark[i]
print("Total :" ,add)
num = 0
for i in mark:
    num += count(mark)
print("Total num of student :" ,num)
avg = add/num
print("Avg value : ",avg)

string = str(input("Enter the steing : ")) #WORD FREQUENCY
word = string.split(' ')
print(word)
feq = {}

for i in word:
   if i in feq:
       feq[i]=feq[i]+1
   else:
       feq[i]=1
print(feq)

mark = {"maths":89,"OOPS":83,"fds":65,"dpco":76,"ds":75} #high mark
max_subject = ""
max_mark = 0
for i in mark:
    if max_mark < mark[i]:
        max_mark=mark[i]
        max_subject=i
print(f'{max_subject} is a high mark {max_mark}')

dupli={"a":1,"b":3,"c":6,"d":1,"e":2,"f":2} #remove duplicate values
dic={}
for i in dupli:
    if dupli[i] not in dic.values() :
        dic[i]=dupli[i]
    else:
        print("skip")
print("removed duplicate value : ",dic)