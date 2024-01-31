a=20
b=30
c=a+b
print("sum of {} and {} is {}".format(a,b,c))
print("{} is sum of {} and {}".format(c,a,b))

x=10
y=20
z=30
print("{} {} {}".format(x,y,z))
print("{1} {0} {2}".format(c,a,b))
print("{3} {1} {2} {0}".format(10,20,30,40))
print("{a} {b} {c} {d}".format(a=x,b=y,c=z,d=a+b+c))


a=10
print("{:d},{:o},{:x},{:b}".format(a,a,a,a))
print("{1:d},{0:o},{3:x},{2:b}".format(10,20,30,40))
print("{a:d},{b:o},{c:x},{d:b}".format(a=10,b=20,c=30,d=40))

b=1.4567
print("{:f},{:e}".format(b,b))
print("{:.2f},{:.2e}".format(b,b))
