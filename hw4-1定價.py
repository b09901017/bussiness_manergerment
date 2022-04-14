a= int(input("a = "))
b= int(input("b = "))
c= int(input("c = "))

pmax = int(a/b)
p = 0

for i in range(0,pmax+1,1):
    A = (a-b*i)*(i-c)
    print(A)
    if (A>p):
        p=A
print(p)
