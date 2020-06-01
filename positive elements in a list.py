list1=[]
n=int(input('enter the number of elements in the list:'))
for i in range(0,n):
    x=int(input())
    list1.append(x)
list2=[]
for i in list1:
    if i>0:
        list2.append(i)
print(list2)
