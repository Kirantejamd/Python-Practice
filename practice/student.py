b=open("C:\\Kiranteja\\Learnings\\Python_Practice\\student","w")
print(1,"naresh","python",5000.0,sep=",",end=";",file=b)
print(2,"kiran","jave",6000.0,file=b)
print(3,"teja","sql",2000.0,file=b,flush=True)
