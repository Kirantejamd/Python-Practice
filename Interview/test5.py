list1=[1,2,3,1,2,3,1,2,3]
list2=[]
#list2.append()#error
#list2.append(10,11)#error
#list2.append([10,11])
list2=list2.append(10)#None
print(list2)
#list2.append(20)


"""
print(list2)
for i in list1:
    if i not in list2:
        list2.append(i)
        print(list2)
print(list2)


print("==============")

for j in range(len(list1)):#0 1 2 3 -- 8
    for i in range((len(list1))-1): #0 -- 7
        if list1[i]>list1[i+1]:
            list1[i],list1[i+1]=list1[i+1],list1[i]
print(list1)


print("==============")


#out=[1, 2, 3, 5, 7, 9, 12, 15, 18]

list2=[]
value=0
for i in range(len(list1)):
    value=value+list1[i]
    list2.append(value)
print(list2)


list2=[]
value=0
for ele in list1:
    value=value+ele
    list2.append(value)
print(list2)


print("===================")


list2=[]
list3=[]

#Do it in single loop, dnt use step
#Try with slicing

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

print("============")


list2=[[1, 1, 2, 3, 3], [1, 2, 2, 3]]

list5=[]#done
#Think twice before iterating range on list
#Takes singlelist and apply sum to all elememts in list
for list_ele in list2:
    s1=0
    for element in list_ele:
        s1=s1+element
    list5.append(s1)
   
print(list5)"""

