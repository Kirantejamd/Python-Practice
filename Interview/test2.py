list1=[[1,1,1],[2,2]]
#output=[3,4]
sum=0
list2=[]
for i in range(len(list1)):
    for j in range(len(list1[i])):
        sum=sum+list1[i][j]
    list2.append(sum)
print(list2)



list1=[1,2,3,1,2,3,1,2,3]
list2=[]
value=0
for i in range(len(list1)):
    value=value+list1[i]
    list2.append(value)
print(list2)
