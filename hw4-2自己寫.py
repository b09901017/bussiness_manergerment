# cost = int(input("成本 : "))
# price = int(input("定價 : "))
# demand_N = int(input("可能需求個數 : "))
# order_num = int(input("訂貨量 : "))

c=int(input('進貨成本:'))
p=int(input('賣客價格:'))
d=int(input('需求可能個數:'))
q=int(input('訂貨量:'))
d0=float(input('賣0份機率:'))
d1=float(input('賣一份機率:'))
d2=float(input('賣二份機率:'))
d3=float(input('賣三份機率:'))
d4=float(input('賣4份機率:'))
d5=float(input('賣5份機率:'))
d6=float(input('賣6份機率:'))
d7=float(input('賣7份機率:'))
d8=float(input('賣8份機率:'))

D=[d0,d1,d2,d3,d4,d5,d6,d7,d8]
a=(D[0]!=d0)
print("a= ",a)
if q>=8:
    sum=p*(d0*0+d1*1+d2*2+d3*3+d4*4+d5*5+d6*6+d7*7+d8*8)
else:
    sum=0
    for i in range (0,q):
        sum=sum+(D[i]*i)
    for i in range (q,9):
        sum=sum+q*D[i]
    sum=sum*p
    
print(int(sum-q*c))



