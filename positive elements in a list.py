list1=[]
n=int(input('enter the number of elements in the list:'))
for i in range(0,n):
    x=int(input())
    list1.append(x)
pos_list=[]
for i in list1:
    if i>0:
        pos_list.append(i)
print(pos_list)
