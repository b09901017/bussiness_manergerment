cost = int(input("成本 : "))
price = int(input("定價 : "))
demand_N = int(input("可能需求個數 : "))
#order_num = int(input("訂貨量 : "))

PN = []
for p in range(0,demand_N+1):
    p=float(input("第{}個機率 : ".format(p)))
    PN.append(p)
    
    
max_profit = 0
for order_num in range(0,demand_N+1):
    
    if (demand_N >=order_num):
        
        exceptd_num = 0
        sum = 0
        p_sum = 0
        
        for i in range(0,order_num):
            sum = sum+PN[i]*i
            p_sum = p_sum+PN[i]
            
        exceptd_num = sum + order_num*(1-p_sum)
        exceptd_profit = exceptd_num*price-order_num*cost
    else:
        exceptd_num = 0
        sum = 0
        
        for i in range(0,demand_N+1):
            sum = sum+PN[i]*i
            
        exceptd_num = sum 
        exceptd_profit = exceptd_num*price-order_num*cost
    if (exceptd_profit>=max_profit):
        max_profit=exceptd_profit
        best_order = order_num
    
print (best_order,int(max_profit))
    
    
    