list1=[1,2,3,1,2,3,1,2,3]
list2=[]
list3=[]
for i in range(0,len(list1),2):
    list2.append(list1[i])
print(list2)
for j in range(1,len(list1),2):
    list3.append(list1[j])
print(list1,list2,list3,sep="\n")

list4=[]
list4.append(list2)
list4.append(list3)
print(list4)

print()

s1=0
list5=[]
for i in range(len(list4)):
    for j in range(len(list4[i])):
        s1=s1+list4[i][j]
    list5.append(s1)
    print(list5)
    
    
    
