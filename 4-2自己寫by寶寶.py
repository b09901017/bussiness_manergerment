c=int(input('進貨成本:'))
p=int(input('賣客價格:'))
d=int(input('需求可能個數:'))

D=[]
for i in range(0,d+1):
        
    F=float(input())
    D.append(F)

max=0
qmax=0
for q in range(0,d+1):
    

    if q>=d:
        sum=0
        for i in range (0,d+1):
            sum=sum+i*D[i] 

    else:
        sum=0
        for i in range (0,q):
            sum=sum+i*D[i]
        for i in range (q,d+1):
            sum=sum+q*D[i]


    A=p*sum-q*c #期望利潤
    #print(A)
    
    if A>max:
        max=A
        qmax=q
        
print(int(qmax),int(max))
