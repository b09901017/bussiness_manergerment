pay=int(input("輸入金額 : "))
turnback = 1000-pay
money500=turnback//500
money100=turnback%500//100
money50=(turnback%500-100*money100)//50
money10=(turnback%500-100*money100-50*money50)//10
money5=(turnback%500-100*money100-50*money50-10*money10)//5
money1=(turnback%500-100*money100-50*money50-10*money10)%5
# print(money500,money100,money50,money10,money5,money1)
if(money500!=0):
  
  if(money500!=0 and money100==0 and money50==0 and money10==0 and money5==0 and money1==0):
    print('500,',money500)
  else: print('500,',money500,end="; ")  
if(money100!=0):
  
  if(money100!=0 and money50==0 and money10==0 and money5==0 and money1==0):
    print('100,',money100)
  else: print("100,",money100,end="; ")
if(money50!=0):
  
  if(money50!=0 and money10==0 and money5==0 and money1==0):
    print('50,',money50)
  else: print("50,",money50,end="; ")     
if(money10!=0):
  
  if(money10!=0 and money5==0 and money1==0):
    print('10,',money10)
  else: print("10,",money10,end="; ") 
if(money5!=0):
  
  if(money5!=0 and money1==0):
    print('5,',money5)
  else:print("5,",money5,end="; ") 
if(money1!=0):
  print("1,",money1)
  
          
# print(money50,end=/n)
# print(money10)
# print(money5)
# print(money1)
#print(money500,'\n','\n',money100)
