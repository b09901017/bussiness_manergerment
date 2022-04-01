pay=int(input("輸入金額 : "))
turnback = 1000-pay
money500=turnback//500
money100=turnback%500//100
money50=(turnback%500-100*money100)//50
money10=(turnback%500-100*money100-50*money50)//10
money5=(turnback%500-100*money100-50*money50-10*money10)//5
money1=(turnback%500-100*money100-50*money50-10*money10)%5
# print(money500,money100,money50,money10,money5,money1)
print("500須找{}張".format(money500))
print("100須找{}張".format(money100))
print("50須找{}張".format(money50))
print("10須找{}張".format(money10))
print("5須找{}張".format(money5))
print("1須找{}張".format(money1))