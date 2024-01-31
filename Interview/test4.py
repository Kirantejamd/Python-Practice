str1="a b c a kiran kiran .."
str2=str1.split()
set1=set(str2)
print(str1,str2)

for value in set1:
    k=str2.count(value)

    print(f'{value}-->{k}')



