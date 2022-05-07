
A=input()
D = list(A)
#print(D)

reverse_or_not = True

if len(D)%2==0:
    
    for i in range(0,len(D)//2+1):
       if D[i]!=D[-1-i]:
            reverse_or_not=False
           
        
    
else:
    for i in range(0,len(D)//2+1):
        if D[i]!=D[-1-i]:
            reverse_or_not=False
             

print(reverse_or_not)


 # if (a[0] == a[4]) and (a[1] == a[3]):
  #  print('%f是迴文數' % (a))  
b=[[1,1,1],
   [1,1,1],
   [1,1,1]]     