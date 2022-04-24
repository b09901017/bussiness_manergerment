from math import sqrt

from numpy import choose


# n = int(input("輸入城鎮數量 : "))
# p = int(input("共要幾個基地台 : "))
# d = int(input("基地台能涵蓋範圍 : "))

input_1 = input(" 城鎮數量 , 共要幾個基地台 , 能涵蓋範圍 ")
list_input_1 = input_1.split()
n=int(list_input_1[0])
p=int(list_input_1[1]) ## n   p   d
d=int(list_input_1[2]) ## 0 list_input_1
 

population_i = []
x_i=[]
y_i=[]
for i in range(0,n):                          ## 輸入值
    input_i = input(" xi , yi , pi ")
    list_input_i = int(input_i.split())
    
    x_i.append(list_input_i[0])
    y_i.append(list_input_i[1])
    population_i.append(list_input_i[2])
    

all_distant = []  ##[  (0-0,0-1,0-2...0-n) , (1-0,1-2,1-3...) , ......    ]        
distant_from_i = []
    
for i in range(0,n):    ##所有之間的距離 
    distant_from_i = [] ## 歸零
    
    for j in range(0,n):
        distant_math = sqrt((x_i[i]-x_i[j])**2+(y_i[i]-y_i[j])**2)
        distant_from_i.append(distant_math)
    
    all_distant.append(distant_from_i)
    
cover_town_for_each = []
towns_is_covered_for_i = []
for i in range(0,n):
    towns_is_covered_for_i=[] ##歸零
    
    for index , element in enumerate(all_distant[i]) :
        if element<=3 and element!=0:
            towns_is_covered_for_i.append(index)
    
    cover_town_for_each.append(towns_is_covered_for_i)
    
    
    
    
remain_town =list(range(0,n+1)) 
max_index = population_i.index(max(population_i))
for i in cover_town_for_each[max_index]:
    remain_town.pop(i)

cover_people_num = {}
for i in range(0,len(remain_town)+1):
    i_and_remain_intersection = cover_town_for_each[i] & remain_town
    i_to_other_distent_in_remain = []
    for j in i_and_remain_intersection:
        
    
  ##  cover_people_num[ remain_town[i] ] = "暫時寫到著" 


    






# choose_order =  [max(population_i)]
# for i in range(0,p):
    